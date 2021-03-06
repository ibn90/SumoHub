from models.pipelines import Pipeline, Stage
import pandas as pd
import os
from multiprocessing import Pool
import requests
import re


class Uniprot_Fasta(Stage):
    s = None

    def preprocessing(self, data):
        self.s = requests.session()
        return data

    def processing(self, data):
        uniprot_ids = data["dataframe"]["id_canonical"].drop_duplicates().to_list()
        fasta_ids = self.multi_map(Pool(), self.get_fasta, uniprot_ids)
        data["fasta_ids"] = pd.DataFrame({"ID": uniprot_ids, "FASTA": fasta_ids})
        return data

    def data_adapter(self, data):
        output_data = {
            "dataframe": data["dataframe"].merge(
                data["fasta_ids"], on="ID", how="inner"
            ).reset_index(drop=True),
            "fasta": data["fasta_ids"],
            "no_pdb_uniprot_ids": data["no_pdb_uniprot_ids"],
            "uniprot_pdb_map": data["uniprot_pdb_map"],
        }
        return output_data

    def get_fasta(self, UNIPROT_ID):
        fasta_id = UNIPROT_ID
        regex = re.compile(r"(|)[A-Z0-9]+(|)")
        url = "".join(["https://www.uniprot.org/uniprot/", fasta_id, ".fasta"])
        resp = requests.get(url)
        # return resp.text[resp.text.find('\n')::]

        # We got rip of ">UNI_ID" we have to mind it with sumo services
        fasta = "".join(resp.text.split("\n")[1::])
        return fasta

    # Uniprot closes connections if we reuse sessions, we need another method
    def get_fasta_session(self, UNIPROT_ID):
        s, fasta_id = UNIPROT_ID[0], UNIPROT_ID[1]
        regex = re.compile(r"(|)[A-Z0-9]+(|)")
        url = "".join(["https://www.uniprot.org/uniprot/", fasta_id, ".fasta"])
        resp = s.get(url)
        # return resp.text[resp.text.find('\n')::]
        fasta = (
            ">"
            + regex.search(resp.text).group()
            + "\n"
            + "".join(resp.text.split("\n")[1::])
        )
        return fasta
