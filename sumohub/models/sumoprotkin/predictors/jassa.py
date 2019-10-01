from multiprocessing import cpu_count
from multiprocessing.pool import Pool
import requests
from requests_toolbelt import MultipartEncoder
import json
import re
import bs4

class Jassa:
    def __init__(self, sequence, mode="single"):
        # ,uniprot_id,filename,name,pdb_id,sumo_filter,
        self.config = {
            "sequence": sequence.split("\n")[1],
            "upload_id_uniprot": "",
            "fichier": ("", json.dumps({"filename": ""})),
            "name": sequence.split("\n")[0].replace(">", "_"),
            "upload_pdb": "Unspecified",
            "table": "beauclair2012",
            "select_type": "interesting",  # all, interesting, cutoff1, cutoff2, concensus, hit
            "select_type_sim": "all-HM",  # all-HM, all
            "select_cutoff_sim": "interesting",  # all, interesting, cutoff_sim1, cutoff_sim2, cutoff_sim3, cutoff_sim4
            "special_color": "none",
            "nb_ligne_aff": "",
            "nb_aa_ff": "60",
            "submit": "Submit",
        }

        self.jassa = "http://www.jassa.fr/index.php?m=jassa"

        if mode == "threaded":
            self.n_threads = cpu_count()
            self.pool = Pool(processes=int(self.n_threads))
        # elif:
        # pass
        else:
            pass

    def query(self, ID=""):

        """
        config={
            "sum":"Medium", # High, Medium, Low, All, None
            "bin":"Medium", # High, Medium, Low, All, None
        }
        """

        m = MultipartEncoder(fields=self.config)
        table = {}
        with requests.Session() as s:
            import pprint

            r = s.post(self.jassa, data=m, headers={"Content-Type": m.content_type})

            soup = bs4.BeautifulSoup(r.content.decode(), features="html.parser")
            x = soup.find("div", {"id": "results"}).table.td.table.findAll("tr")

            # Getting the score info
            score_info = (
                re.search(r"PSmax=(.{6,7}?)", x[0].text).group(1),
                re.search(r"Cut-off High=(.{6,7}?)", x[0].text).group(1),
                re.search(r"Cut-off Low=(.{6,7}?)", x[0].text).group(1),
            )
            print(score_info)

        # if r.status_code == 200:
        #     cookie = {
        #         "PHPSESSID": requests.utils.dict_from_cookiejar(r.cookies)["PHPSESSID"]
        #     }
        #     r = requests.get(self.gps_sumo_show, cookies=cookie)
        #     if r.status_code == 200:
        #         soup = bs4.BeautifulSoup(r.content.decode(), features="html.parser")
        #         keys = [
        #             x.text
        #             for x in soup.table.find("tr", attrs={"class": "top"}).findAll("th")
        #         ]
        #         seq_pos_string = soup.find_all("font", attrs={"color": "red"})
        #         [x.replace_with("#" + x.text + "#") for x in seq_pos_string]
        #         values = [
        #             [y.find("font").text for y in x.findAll("td")]
        #             for x in soup.table.findAll("tr", attrs={"class": False})
        #         ]
        #         table = {
        #             key: value
        #             for key, value in zip(
        #                 keys, [[y for y in x if y != ""] for x in zip(*values)]
        #             )
        #         }
        #     else:
        #         print("Error en get")
        # else:
        #     print("Error en post")

        # return OrderedDict(table)

    def multiquery(self):
        if not self.pool:
            self.n_threads = cpu_count()
            self.pool = MTPool(processes=int(self.n_threads))
        table = self.pool.map(self.query, IDs)
        return table
