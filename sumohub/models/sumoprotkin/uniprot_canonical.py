from models.pipelines import Pipeline, Stage
import pandas as pd
import os


class Uniprot_Canonical(Stage):
    # This Stage is a filter before Uniprot_Fasta. It's mean to add
    url = ""

    def preprocessing(self, data):
        return data

    def processing(self, data):
        data["dataframe"]["id_canonical"] = data["dataframe"]["ID"]
        return data

    def data_adapter(self, data):
        return data
