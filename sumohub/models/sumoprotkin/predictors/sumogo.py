from collections import OrderedDict
from multiprocessing import cpu_count
from multiprocessing.pool import Pool

import bs4
import requests


class SumoGo:
    def __init__(self):
        self.sumogo_result = "http://predictor.nchu.edu.tw/SUMOgo/result.php"
        self.pool = None

    def query(self, ID):

        table = {}
        r = requests.post(
            self.sumogo_result,
            data={"seq": ID},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if r.status_code == 200:
            # cookie = {
            #     "PHPSESSID": requests.utils.dict_from_cookiejar(r.cookies)["PHPSESSID"]
            # }
            soup = bs4.BeautifulSoup(r.content.decode(), features="html.parser")
            # Getting jobid which is used to retrieve the query results
            jobid = soup.input["value"]
            s = requests.post(self.sumogo_result, data={"jid": jobid})
            if s.status_code == 200:
                soup = bs4.BeautifulSoup(s.content.decode(), features="html.parser")
                results = [
                    a
                    for a in [
                        [y.text for y in x.findAll("td") if y.text != ""]
                        for x in soup.table.findAll("tr")
                    ]
                    if a
                ]
                table = {
                    results[0][0]: [x[0] for x in results[1::]],
                    results[0][1]: [x[1] for x in results[1::]],
                }
            else:
                print("Error en get")
        else:
            print("Error en post")
        return OrderedDict(table)

    def multiquery(self, IDs):
        if not self.pool:
            self.n_threads = cpu_count()
            self.pool = Pool(processes=int(self.n_threads))
        table = self.pool.map(self.query, IDs)
        return table
