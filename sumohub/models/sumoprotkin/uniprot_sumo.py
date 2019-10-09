from models.pipelines import Pipeline, Stage
from models.sumoprotkin.predictors import SumoGo, GPSSumo, Jassa
import pandas as pd
import os
import requests


class Uniprot_Sumo(Stage):
    """
    Three predictors from now:
        - GPSSumo: Online. Seems to work OK
        - SumoGo: Online. Some Uniprot_ids create failed or never finished jobs. Probably some of the tools they use crash.
        - Jassa: Offline script. It needs some testing to be sure values are good

    """

    gpssumo = GPSSumo()
    sumogo = SumoGo()
    jassa = Jassa()

    def preprocessing(self, data):
        self.s = requests.session()
        return data

    def processing(self, data):
        UNIPROT_IDs = self.get_id_fasta(data["fasta"])
        data["gpssumo"] = self.gpssumo.multiquery(UNIPROT_IDs)
        data["sumogo"] = self.sumogo.multiquery(UNIPROT_IDs)
        data["jassa"] = self.jassa.multiquery(UNIPROT_IDs)
        return data

    def data_adapter(self, data):
        data["gpssumo"] = pd.DataFrame(data["gpssumo"])
        data["sumogo"] = pd.DataFrame(data["sumogo"])
        data["jassa"] = pd.DataFrame(data["jassa"])
        data["jassa"].rename(columns={"Seq_Name": "ID"}, inplace=True)
        return data

    def get_id_fasta(self, data):
        UNIPROT_IDs = ["\n".join((">" + x[0], x[1])) for x in data.values.tolist()]
        return UNIPROT_IDs
