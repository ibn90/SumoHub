from models.pipelines import Pipeline, Stage
import pandas as pd
import requests
import json
import os
from multiprocessing import Pool


class Uniprot_PDB(Stage):

    url = "https://www.ebi.ac.uk/pdbe/api/mappings/{}"    

    def preprocessing(self, data):
        # data = {"dataframe": data, "uniprot_ids": data["ID"].to_list()}
        return data

    def processing(self, data):
        # pool=Pool(processes=8)
        pdb_mapping=self.multi_map(Pool(),self.pdb_request,data["uniprot_ids"])
        # pdb_mapping=pool.map(self.pdb_request,data["uniprot_ids"])
        uni_pdb={
            "ID":[],
            "PDB":[]
        }
        no_pdb=[]
        for ID in pdb_mapping:
            for x in ID:
                if x[1]=="no_pdb":
                    no_pdb.append(x[0])
                else:
                    uni_pdb["ID"].append(x[0])
                    uni_pdb["PDB"].append(x[1])
        data["uniprot_pdb"]=pd.DataFrame(uni_pdb)
        data["no_pdb"]=no_pdb
        return data

    def pdb_request(self, uniprot_id):
        response = requests.get(self.url.format(uniprot_id))
        if response.status_code == 200:
            resp_json = json.loads(response.content)
            out = [(uniprot_id, x) for x in resp_json[uniprot_id]["PDB"].keys()]
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
        left_join=data["dataframe"].merge(data["uniprot_pdb"],on="ID",how="left")

        output_data={
            "dataframe":left_join[left_join["PDB"].notnull()],
            "no_pdb_uniprot_ids": left_join[left_join["PDB"].isnull()]["ID"].to_list()
        }
        return output_data
