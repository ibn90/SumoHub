from models.pipelines import Pipeline, Stage
import pandas as pd
import os
import json


class Uniprot_PDB_Fasta(Stage):
    def preprocessing(self, data):
        data["jassa"].rename(columns={"Seq_Name": "ID"}, inplace=True)
        data["jassa"].rename(columns={"Pos_K": "Position"}, inplace=True)
        return data

    def processing(self, data):

        data["dataframe"] = data["dataframe"].merge(data["sites"], on="ID", how="left")

        ID_loc = data["dataframe"].columns.get_loc("ID")
        PDB_loc = data["dataframe"].columns.get_loc("PDB")
        CHAIN_loc = data["dataframe"].columns.get_loc("CHAIN")
        Site_loc = data["dataframe"].columns.get_loc("Site")

        data["dataframe"]["Site_map"] = pd.Series(
            [
                data["uniprot_pdb_map"][x[ID_loc]][x[PDB_loc] + "_" + x[CHAIN_loc]].get(
                    x[Site_loc]
                )
                for x in data["dataframe"].values
            ]
        )

        gpssumo = (
            data["dataframe"][["ID", "PDB", "CHAIN","Type","Site"]]
            .drop_duplicates()
            .merge(data["gpssumo"], on="ID", how="left").reset_index(drop=True)
        )
        sumogo = (
            data["dataframe"][["ID", "PDB", "CHAIN","Type","Site"]]
            .drop_duplicates()
            .merge(data["sumogo"], on="ID", how="left").reset_index(drop=True)
        )
        jassa = (
            data["dataframe"][["ID", "PDB", "CHAIN","Type","Site"]]
            .drop_duplicates()
            .merge(data["jassa"], on="ID", how="left").reset_index(drop=True)
        )

        gpssumo["Position_map"] = self.map_sumo(gpssumo, data["uniprot_pdb_map"])
        sumogo["Position_map"] = self.map_position(sumogo, data["uniprot_pdb_map"])
        jassa["Position_map"] = self.map_position(jassa, data["uniprot_pdb_map"])

        data["gpssumo"] = gpssumo
        data["sumogo"] = sumogo
        data["jassa"] = jassa

        return data

    def map_position(self, position, mappings):
        pos_map = []
        for row in position.values:
            map_entry = mappings[row[0]][row[1] + "_" + row[2]]
            pos_map.append([row[0], row[1], row[2], str(map_entry.get(int(row[5])))])
        data = pd.Series([x[3] for x in pos_map])
        return data

    def map_sumo(self, sumo, mappings):
        sumo_map = []
        for row in sumo.values:
            map_entry = mappings[row[0]][row[1] + "_" + row[2]]
            row_map = None
            if " - " in row[5]:
                # Its a Motif(SIM), we have to deal with it
                position = row[5].split(" - ")
                pos_map = " - ".join(
                    [
                        str(map_entry.get(int(position[0]))),
                        str(map_entry.get(int(position[1]))),
                    ]
                )
            else:
                pos_map = str(map_entry.get(int(row[5])))
            sumo_map.append([row[0], row[1], row[2], pos_map])

        data = pd.Series([x[3] for x in sumo_map])
        return data

    def data_adapter(self, data):
        output_data = {
            "dataframe": data["dataframe"].reset_index(drop=True),
            "no_pdb_uniprot_ids": data["no_pdb_uniprot_ids"],
            "uniprot_pdb_map": data["uniprot_pdb_map"],
            "gpssumo": data["gpssumo"].reset_index(drop=True),
            "sumogo": data["sumogo"].reset_index(drop=True),
            "jassa": data["jassa"].reset_index(drop=True),
        }
        return output_data
