from collections import OrderedDict
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool as Pool
import time

import bs4
import requests


class SumoGo:
    def __init__(self):
        self.sumogo_result = "http://predictor.nchu.edu.tw/SUMOgo/result.php"
        self.pool = None

        # We need to wait to deal with delays on the server side
        self.delay_job_results = 0.5

    def query(self, ID):

        table = {}
        r = requests.post(
            self.sumogo_result,
            data={"seq": ID},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        uni_id = ID.split("\n")[0][1::]
        if r.status_code == 200:
            # cookie = {
            #     "PHPSESSID": requests.utils.dict_from_cookiejar(r.cookies)["PHPSESSID"]
            # }
            soup = bs4.BeautifulSoup(r.content.decode(), features="html.parser")
            # Getting jobid which is used to retrieve the query results
            jobid = soup.input["value"]

            # We sleep thread to avoid picking results to early
            # time.sleep(self.delay_job_results)

            s = requests.post(self.sumogo_result, data={"jid": jobid})
            if s.status_code == 200:
                try:
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
                        "ID": [uni_id] * len(results[1::]),
                        results[0][0]: [x[0] for x in results[1::]],
                        results[0][1]: [x[1] for x in results[1::]],
                    }
                except:
                    table = {
                        "ID": [uni_id],
                        "Position": ["*"],
                        "Confidence Score": ["*"],
                    }
            else:
                print("Error en get")
        else:
            print("Error en post")
        return OrderedDict(table)

    def multiquery(self, IDs):
        if self.pool is None:
            self.n_threads = cpu_count()
            self.pool = Pool(processes=int(self.n_threads))
        table = self.pool.map(self.query, IDs)
        out_table = table[0]
        for x in table[1:]:
            for key, value in zip(x.keys(), x.values()):
                out_table[key].extend(value)
        return out_table
