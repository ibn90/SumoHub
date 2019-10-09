from models.pipelines import Pipeline, Stage
import pandas as pd
import os
import json
import re
import requests
from multiprocessing import Pool as Pool
import asyncio


class PDB_Filter(Stage):

    url_pdbe = "https://www.ebi.ac.uk/pdbe/api/pdb/entry/experiment/{}"
    url_pdb = "https://www.rcsb.org/pdb/rest/getEntityInfo?structureId={}"

    def preprocessing(self, data):
        self.s = requests.session()
        return data

    def processing(self, data):
        # pool = MTPool(processes=16)
        list_pdb = data["dataframe"]["PDB"].to_list()

        # unfiltered = self.multi_map(
        #     Pool(),
        #     self.get_resolution,
        #     [x for x in list_pdb if len(x) > 1],
        # )
        # Big speed up, we need to test it and refactor get_resolution_session to get_resolution
        unfiltered_session = self.multi_map(
            Pool(),
            self.get_resolution_session,
            [[self.s, x] for x in list_pdb if len(x) > 1],
        )

        # unfiltered = pool.map(self.get_resolution, [x for x in list_pdb if len(x) > 1])
        # pool.close()
        # pool.join()
        high_res = [x for x in unfiltered_session if x[1] <= 2.00]
        low_res = [x for x in unfiltered_session if x[1] >= 2.00]
        # out=[self.get_resolution(x) for x in list_pdb]

        # We're savin "low_resolution" pdb entries for utility or logging purposes
        data["high_res"] = pd.DataFrame(
            {"PDB": [x[0] for x in high_res], "RES": [x[1] for x in high_res]}
        )
        data["low_res"] = pd.DataFrame(
            {"PDB": [x[0] for x in low_res], "RES": [x[1] for x in low_res]}
        )
        return data

    def data_adapter(self, data):
        # There are PDB associated to many UNIPROT ID, we need to check it

        filtered_dataframe = data["dataframe"].merge(
            data["high_res"], on="PDB", how="inner"
        )
        dropped_low_res = data["dataframe"].merge(
            data["low_res"], on="PDB", how="inner"
        )
        output_data = {
            "dataframe": filtered_dataframe,
            "no_pdb_uniprot_ids": data["no_pdb_uniprot_ids"],
            "uniprot_same_pdb": data["dataframe"][
                data["dataframe"]["PDB"].isin(
                    data["dataframe"][data["dataframe"].duplicated(["PDB"])]["PDB"]
                )
            ],
            "dropped_low_res": dropped_low_res,
        }

        # data["dropped_low_res"]=data["dataframe"][~data["dataframe"]["ID"]==filtered_dataframe["ID"]]
        # data["dataframe"]=filtered_dataframe
        return output_data

    def get_resolution(self, pdb_id):
        def get_resolution2(pdb_id):
            url = self.url_pdb.format(pdb_id.lower())
            resp = requests.get(url).content
            res = re.search(r"resolution=\"([0-9.0-9]*)\"", resp.decode())
            if res:
                out = float(res.group(1))
            else:
                out = 9.00
            return out

        url = self.url_pdbe.format(pdb_id.lower())
        msg = requests.get(url)
        resp = json.loads(msg.content)
        out = [pdb_id, 9.00]
        if msg.status_code == 200:
            if resp.get(pdb_id.lower(), None):
                out = [
                    pdb_id,
                    [x.get("resolution", 9.00) or 9.00 for x in resp[pdb_id.lower()]][
                        0
                    ],
                ]
            else:
                out = [pdb_id, get_resolution2(pdb_id)]
        return out

    def get_resolution_session(self, pdb_id):
        def get_resolution2(pdb_id, s):
            url = self.url_pdb.format(pdb_id.lower())
            resp = s.get(url).content
            res = re.search(r"resolution=\"([0-9.0-9]*)\"", resp.decode())
            if res:
                out = float(res.group(1))
            else:
                out = 9.00
            return out

        s, pdb_id = pdb_id[0], pdb_id[1]
        url = self.url_pdbe.format(pdb_id.lower())
        msg = s.get(url)
        resp = json.loads(msg.content)
        out = [pdb_id, 9.00]
        if msg.status_code == 200:
            if resp.get(pdb_id.lower(), None):
                out = [
                    pdb_id,
                    [x.get("resolution", 9.00) or 9.00 for x in resp[pdb_id.lower()]][
                        0
                    ],
                ]
            else:
                out = [pdb_id, get_resolution2(pdb_id, s)]
        return out
