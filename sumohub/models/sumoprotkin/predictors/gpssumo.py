from collections import OrderedDict
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool as Pool
import json

import bs4
import requests
from requests_toolbelt import MultipartEncoder


class GPSSumo:
    def __init__(
        self, config={"sum": "Medium", "bin": "Medium"}, tpool=None, n_threads=2
    ):
        """
        
        """
        self.config = config
        self.gps_sumo_online = "http://sumosp.biocuckoo.org/online.php"
        self.gps_sumo_transfer = "http://sumosp.biocuckoo.org/transfer.php"
        self.gps_sumo_show = "http://sumosp.biocuckoo.org/showResult.php"

        self.n_threads = n_threads
        self.pool=Pool(processes=int(self.n_threads)) 

    def query(self, ID):

        """
        config={
            "sum":"Medium", # High, Medium, Low, All, None
            "bin":"Medium", # High, Medium, Low, All, None
        }
        """

        m = MultipartEncoder(
            fields={
                "text": (None, ID),
                "sum": (None, self.config["sum"]),
                "bin": (None, self.config["bin"]),
                "bool": (None, "on"),
                "submit": (None, "Submit"),
                "upfile": ("", json.dumps({"filename": ""})),
            }
        )
        table = {}
        r = requests.post(
            self.gps_sumo_transfer, data=m, headers={"Content-Type": m.content_type}
        )
        if r.status_code == 200:
            cookie = {
                "PHPSESSID": requests.utils.dict_from_cookiejar(r.cookies)["PHPSESSID"]
            }
            p = 1
            NEXT_PAGE = True
            table = None
            while NEXT_PAGE:
                r = requests.get(self.gps_sumo_show + "?p=" + str(p), cookies=cookie)
                if r.status_code == 200:
                    soup = bs4.BeautifulSoup(r.content.decode(), features="html.parser")

                    keys = [
                        x.text
                        for x in soup.table.find("tr", attrs={"class": "top"}).findAll(
                            "th"
                        )
                    ]
                    seq_pos_string = [
                        x.replace_with("#" + x.text + "#")
                        for x in soup.find_all("font", attrs={"color": "red"})
                        if x.text != ""
                    ]

                    values = [
                        [y.find("font").text for y in x.findAll("td")]
                        for x in soup.table.findAll("tr", attrs={"class": False})
                    ]

                    if len(values) >= 1:
                        if table:
                            for key, value in zip(
                                keys, [[y for y in x if y != ""] for x in zip(*values)]
                            ):
                                table[key].extend(value)
                        else:
                            table = {
                                key: value
                                for key, value in zip(
                                    keys,
                                    [[y for y in x if y != ""] for x in zip(*values)],
                                )
                            }
                        p = p + 1
                    else:
                        NEXT_PAGE = False
                else:
                    print("Error en get")
        else:
            print("Error en post")
        return OrderedDict(table)

    def multiquery(self, IDs):
        if not self.pool:
            self.n_threads = cpu_count()
            self.pool = Pool(processes=int(self.n_threads))
        n = int(len(IDs) / (self.n_threads))
        # Ids=[print("IF: " + str(i)) if i+n<len(IDs) else print("ELSE: " + str(i)) for i in range(0,len(IDs),n)]
        Ids = [
            "\n".join(IDs[i : i + n]) if i + n < len(IDs) else "\n".join(IDs[i::])
            for i in range(0, len(IDs), n)
        ]
        table = self.pool.map(self.query, Ids)
        out_table = table[0]
        for x in table[1:]:
            for key, value in zip(x.keys(), x.values()):
                out_table[key].extend(value)
        return out_table
