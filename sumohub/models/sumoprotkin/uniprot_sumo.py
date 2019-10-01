from models.pipelines import Pipeline, Stage
from models.sumoprotkin.predictors import SumoGo,GPSSumo,Jassa
import pandas as pd
import os
import requests

class Uniprot_Sumo(Stage):

    def preprocessing(self,data):
        self.s=requests.session()
        return data
    def processing(self,data):
        IDs=self.get_id_fasta(data["fasta"])
        gpssumo=GPSSumo()
        out=pd.DataFrame(gpssumo.multiquery(IDs))
        print(out)
        input()
        return data
    def data_adapter(self,data):
        return data
    def get_id_fasta(self,data):
        IDs=["\n".join((">"+x[0],x[1])) for x in data.values.tolist()]
        return IDs
