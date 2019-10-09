from models.pipelines import Pipeline, Stage
from multiprocessing.pool import Pool
from multiprocessing import cpu_count
import requests
import re
import pandas as pd
import os


class Uniprot_active_sites(Stage):

    url = "https://www.uniprot.org/uniprot/?query=id:{}&columns=feature(ACTIVE SITE),feature(BINDING SITE)&format=tab"

    def preprocessing(self, data):
        return data

    def processing(self, data):
        UNIPROT_IDS = data["dataframe"]["ID"].drop_duplicates().to_list()
        data["sites"] = self.multiquery(UNIPROT_IDS, data)
        return data

    def data_adapter(self, data):
        data["sites"] = pd.DataFrame(data["sites"]).drop_duplicates().reset_index(drop=True)
        data["sites"]["Site"] = data["sites"]["Site"].apply(
            lambda x: int(x.split("-")[0])
        )
        return data

    def multiquery(self, UNIPROT_IDs, data):
        pool = Pool(processes=cpu_count())
        out = pool.map(self.retrieve_sites, UNIPROT_IDs)
        out_dict = {"ID": [], "Type": [], "Site": []}
        for UNIPROT_ID in out:
            for site in UNIPROT_ID:
                out_dict["ID"].extend((site[0],))
                out_dict["Type"].extend((site[1],))
                out_dict["Site"].extend((site[2],))
        return out_dict

    def retrieve_sites(self, UNIPROT_ID):
        regex = [
            re.compile("(ACT_SITE) ([0-9]*) ([0-9]*)"),
            re.compile("(BINDING) ([0-9]*) ([0-9]*)"),
        ]

        url = self.url.format(UNIPROT_ID)
        resp = requests.get(url).content.decode()
        sites = []
        for x in [y for y in regex[0].findall(resp)]:
            sites.extend([[UNIPROT_ID, x[0], "-".join([x[1], x[2]])]])
        for x in [y for y in regex[1].findall(resp)]:
            sites.extend([[UNIPROT_ID, x[0], "-".join([x[1], x[2]])]])
        return sites
