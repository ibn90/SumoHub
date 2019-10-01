import os
import pickle


class Data:
    data = None

    def __init__(self, data):
        self.data = data

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def print_data(self):
        print(self.data)

    def export(self):
        print("Export Not Implemented")
        raise NotImplementedError

    def save(self, name=None):
        print("Save Not Implemented")
        raise NotImplementedError

    def load(self, name=None):
        print("Load Not Implemented")
        raise NotImplementedError


class Stage:
    """
    Base Stage class.
    Three parameters:
        __data_in -> Stage's input
        __data_out -> Stages's output
        __name -> Identifier, for logging or diagram purposes
    """

    __data_in = None
    __data_out = None
    name = "Stage"
    cache_path = "sumohub/cache/"
    caching = False
    cache_file = ""
    cache_file_format = ".pickle"
    s = None

    def __init__(self, name, caching=False):
        if name:
            self.name = str(name).replace(" ", "_")
        else:
            self.name = "STAGE"
            print('Stage created with generic name "STAGE"')
        self.caching = caching
        self.cache_file = self.cache_path + self.name + self.cache_file_format

    def rx(self, data=None):
        if self.caching and os.path.exists(self.cache_file):
            self.__data_out = self.cache()

        else:
            if data is not None:
                input_data = data.get_data()
                self.__data_out = self.inner_pipeline(input_data)
            else:
                input_data = self.source()
                self.__data_out = self.inner_pipeline(input_data)

    def tx(self):
        if self.s:
            self.s.close()
        return Data(self.__data_out)

    def source(self):
        print("Not a Source Stage, maybe the input is not connected to any other stage")
        raise NotImplementedError

    def inner_pipeline(self, data):
        preproc_data = self.preprocessing(data)
        proc_data = self.processing(preproc_data)
        output_data = self.data_adapter(proc_data)
        if self.caching:
            with open(
                self.cache_path + self.name + self.cache_file_format, "wb"
            ) as fwrite:
                pickle.dump(output_data, fwrite, protocol=pickle.HIGHEST_PROTOCOL)
        return output_data

    def preprocessing(self, data):
        return data

    def processing(self, data):
        return data

    def data_adapter(self, data):
        return data

    def cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "rb") as fread:
                data = pickle.load(fread)
        else:
            data = None
        return data

    def multi_map(self, pool, func, data):
        out = pool.map(func, data)
        pool.close()
        pool.join()
        return out

    def get_name(self):
        return self.name


class Pipeline:
    """
    Pipeline class.
    Pipe the data through all the stages and collect the outputs.
    Expected to grow in the future, adding multithreading, logging and
    more features.
    """

    data = ""
    stage_dict = {}
    cache_path = "sumohub/cache/{}.pickle"

    def __init__(self, stages):
        print("Initializing the pipeline")
        print("Entering " + stages[0].get_name() + " stage")
        stages[0].rx(None)
        data = stages[0].tx()
        for stage in stages[1::]:
            print("Entering " + stage.get_name() + " stage")
            stage.rx(data)
            data = stage.tx()
            self.backup(stage.get_name(), data)
        self.data = data
        print("Exiting the pipeline")

    def backup(self, name, data):
        self.stage_dict.update({name: data})

    def clear_cache(self):
        print("Cache cleaning...")
        for stage in self.stage_dict.keys():
            cache_file = self.cache_path.format(stage.get_name())
            if os.path.exists(cache_file):
                os.remove(cache_file)
        print("Cache cleared...")


if __name__ == "__main__":
    stage = Stage("Uniprot->PDB")
    pipe = Pipeline([stage, stage])

