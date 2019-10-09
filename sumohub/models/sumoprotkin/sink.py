from models.pipelines import Pipeline, Stage
from models.sumoprotkin.predictors import predictors
import pandas as pd
import os


class Sink(Stage):
    def preprocessing(self, data):
        return data

    def processing(self, data):
        return data

    def data_adapter(self, data):
        return data
