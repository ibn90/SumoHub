import asyncio
import itertools
import os
import re
from multiprocessing.pool import Pool

import aiohttp
import numpy
import pandas as pd
import requests
import uvloop

from models.pipelines import Pipeline, Stage
from models.sumoprotkin.predictors import predictors


# import numpy
class Distances_Map(Stage):
    def preprocessing(self, data):
        # # print(data["dataframe"][data["dataframe"]["PDB"]=="4tnd"][["UNIP_START","UNIP_END"]])
        # # print(data["sumogo"])
        # print(data["sumogo"][data["sumogo"]["PDB"]=="4wb8"]['Site'].values)
        # print(len(data["sumogo"][data["sumogo"]["PDB"]=="4wb8"]['Site'].values))
        # input()
        return data

    def processing(self, data):
        PDBs = data["dataframe"]["PDB"].drop_duplicates().to_list()
        # For now only consider Sumoylation Concensus
        data["gpssumo"] = data["gpssumo"][
            data["gpssumo"]["Type_y"] == "Sumoylation Concensus"
        ].reset_index(drop=True)

        # We have nested list for multiproc, joining them in a single list
        pdb_coordinates = self.get_coordinates(PDBs)
        pdb_coordinates_map = {[*x][0]: x[[*x][0]] for x in pdb_coordinates}
        # data["gpssumo"]["Distance"]=self.calculate_distance(data["gpssumo"][["PDB","CHAIN","Site","Position_map"]].values,pdb_coordinates_map)
        for predictor in predictors:
            pred_vector=self.calculate_distance(
                data[predictor][["PDB", "CHAIN", "Site", "Position_map"]].values,
                pdb_coordinates_map,
            )
            data[predictor]["Distance"] = pred_vector

        return data

    def get_coordinates(self, PDBs):
        return list(
            itertools.chain.from_iterable(
                self.multi_map(
                    Pool(processes=16), self.multiquery, self.slice_list(PDBs)
                )
            )
        )

    def multiquery(self, data):
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)
        out = loop.run_until_complete(self.get_and_process_pdb(data))
        return out

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def get_and_process_pdb(self, PDBs):
        async with aiohttp.ClientSession() as session:
            regex = re.compile(r"^ATOM.*$", re.MULTILINE)
            html = [
                [
                    PDB,
                    await self.fetch(
                        session,
                        "http://www.ebi.ac.uk/pdbe/entry-files/download/pdb{}.ent".format(
                            PDB.lower()
                        ),
                    ),
                ]
                for PDB in PDBs
            ]
            pdb_dicts = [self.parse_pdb(regex, x[0], x[1]) for x in html]
            return pdb_dicts

    def parse_pdb(self, regex, PDB, response):
        data = [
            (
                x[6:11].strip(),  # 0.Atom serial number
                x[12:16].strip(),  # 1.Atom name
                # x[16:17], # Alternate location indicator
                x[17:20].strip(),  # 2.Residue name
                x[21:22].strip(),  # 3.Chain identifier
                x[22:26].strip(),  # 4.Residue sequence number
                # x[26:27],#Code for insertion of residues
                x[30:38].strip(),  # 5.Orthogonal coordinates for X in Angstroms
                x[38:46].strip(),  # 6.Orthogonal coordinates for Y in Angstroms
                x[46:54].strip(),  # 7.Orthogonal coordinates for Z in Angstroms
                # x[54:60].strip(),  # Occupancy
                # x[60:66].strip(),  # Temperature factor
                # x[76:78],  # Element symbol, right-justified
                # x[78:79],  # Charge on the atom
            )
            for x in regex.findall(response)
        ]
        out = {}
        for x in data:
            chain = out.get(x[3])
            if chain:
                residue = chain.get(x[4])
                if residue:
                    residue[x[1]] = (float(x[5]), float(x[6]), float(x[7]))
                else:
                    chain[x[4]] = {x[1]: (float(x[5]), float(x[6]), float(x[7]))}
            else:
                out[x[3]] = {x[4]: {x[1]: (float(x[5]), float(x[6]), float(x[7]))}}
        # El Limit tiene que estar por cadena, A o B o las que haya TODO
        out["Limit"] = {
            x: (min(out[x].keys(), key=int), max(out[x].keys(), key=int))
            for x in out.keys()
        }
        return {PDB: out}

    def calculate_distance(self, data, coordinates_map):
        out = []
        
        for x in data:
            upper = int(coordinates_map[x[0]]["Limit"][x[1]][1])
            lower = int(coordinates_map[x[0]]["Limit"][x[1]][0])
            site = int(x[2])
            
            if site > lower and site < upper and x[3] is not "None":
                try:
                    a = numpy.array(coordinates_map[x[0]][x[1]][str(x[2])]["CA"])
                    b = numpy.array(coordinates_map[x[0]][x[1]][str(x[3])]["CA"])
                    distance = numpy.linalg.norm(a - b)+0.00001
                    out.append(distance)
                except:
                    out.append(None)
            else:
                out.append(None)
        # counter=0
        # for x in out:
        #     if x == None:
        #         print("Fail Type: "+str(type(x))+" Value: "+str(x))
        #     else:
        #         counter=counter+1
        #         print("OK Type: " +str(type(x)) + " Value: "+str(x))
        # print("Numero de valores OK: "+str(counter))
        # print(pd.Series(out))
        # print(pd.Series(out).dropna())
        # input()
        return pd.Series(out)

    def data_adapter(self, data):
        return data
