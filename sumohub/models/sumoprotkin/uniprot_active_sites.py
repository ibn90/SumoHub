from models.pipelines import Pipeline, Stage
import pandas as pd
import os

class Uniprot_active_sites(Stage):
    def preprocessing(self,data):
        return data
    def processing(self,data):
        return data
    def data_adapter(self,data):
        return data
