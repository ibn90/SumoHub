from models.pipelines import Pipeline, Stage
import pandas as pd
import requests
import json
import os
from multiprocessing import Pool


class Uniprot_PDB(Stage):

    url = "https://www.ebi.ac.uk/pdbe/api/mappings/best_structures/{}"

    def preprocessing(self, data):
        # data = {"dataframe": data, "uniprot_ids": data["ID"].to_list()}
        return data

    def processing(self, data):
        # pool=Pool(processes=8)
        pdb_mapping = self.multi_map(Pool(), self.pdb_request, data["uniprot_ids"])
        # pdb_mapping=pool.map(self.pdb_request,data["uniprot_ids"])
        uni_pdb = {
            "ID": [],
            "PDB": [],
            "CHAIN": [],
            "COV": [],
            "RES": [],
            "UNIP_START": [],
            "UNIP_END": [],
            "PDB_START": [],
            "PDB_END": [],
        }
        uni_pdb_map = {}
        no_pdb = []
        for ID in pdb_mapping:
            for x in ID:
                if x[1] == "no_pdb":
                    no_pdb.append(x[0])
                else:
                    uni_pdb["ID"].append(x[0])
                    uni_pdb["PDB"].append(x[1])
                    uni_pdb["CHAIN"].append(x[2])
                    uni_pdb["COV"].append(x[3])
                    uni_pdb["RES"].append(x[4])
                    uni_pdb["UNIP_START"].append(int(x[5]))
                    uni_pdb["UNIP_END"].append(int(x[6]))
                    uni_pdb["PDB_START"].append(int(x[7]))
                    uni_pdb["PDB_END"].append(int(x[8]))
                    uni_pdb_map[x[0]] = uni_pdb_map.get(x[0], {})
                    uni_pdb_map[x[0]]["_".join((x[1], x[2]))] = {
                        x: y
                        for x, y in zip(
                            range(int(x[5]), int(x[6]) + 1),
                            range(int(x[7]), int(x[8]) + 1),
                        )
                    }

        data["uniprot_pdb_map"] = uni_pdb_map
        data["uniprot_pdb"] = pd.DataFrame(uni_pdb)
        data["no_pdb"] = no_pdb
        return data

    def pdb_request(self, uniprot_id):
        response = requests.get(self.url.format(uniprot_id))
        if response.status_code == 200:
            resp_json = json.loads(response.content)
            out = [
                (
                    uniprot_id,
                    x["pdb_id"],
                    x["chain_id"],
                    x["coverage"],
                    x["resolution"],
                    x["unp_start"],
                    x["unp_end"],
                    x["start"],
                    x["end"],
                )
                for x in resp_json[uniprot_id]
                if (x.get("coverage", 0.00) or 0.00) > 0.90
                and (x.get("resolution", 3.00) or 3.00) < 2.00
            ]
        else:
            out = [(uniprot_id, "no_pdb")]
        return out

    def data_adapter(self, data):
        # Output Data:
        # "dataframe" => Primary Dataframe:
        # ID GENE HUGO_SYMBOL FAMILY PDB
        # *    *       *         *    *
        # *    *       *         *    *
        # *    *       *         *    *
        # ==============================
        # "no_pdb" => Failed Uniprot-PDB mappings (UNIPROT ID)
        left_join = data["dataframe"].merge(data["uniprot_pdb"], on="ID", how="left")

        output_data = {
            "dataframe": left_join[left_join["PDB"].notnull()],
            "no_pdb_uniprot_ids": left_join[left_join["PDB"].isnull()]["ID"].to_list(),
            "uniprot_pdb_map": data["uniprot_pdb_map"],
        }
        return output_data
