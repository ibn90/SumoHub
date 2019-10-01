from models.pipelines import Pipeline, Stage
import pandas as pd
import requests
import re
import bs4
import os
import pyarrow.feather as feather



class Source(Stage):
    # URL's:
    url_1 = "https://www.uniprot.org/docs/pkinfam"


    def source(self):

        # Code to download human kinases list updated in html format
        response = requests.get(self.url_1)

        # Obtain page in utf-8 xml format
        html_doc = bs4.BeautifulSoup(response.content, "html.parser")
        # Get text from html <pre> block
        html_data = html_doc.pre.get_text()
        # Getting and processing URL data
        doc_title, data = self.parse_data(html_data)

        reg_exp = re.compile(r"([a-zA-Z0-9]+).HUMAN\(([a-zA-Z0-9]+)\)")

        dict_df = {"ID": [], "Gene": [], "Hugo_Symbol": [], "Family": []}
        for family, table in data.items():
            [
                (
                    dict_df["ID"].append(row.group(2)),
                    dict_df["Gene"].append(row.group(1)),
                    dict_df["Hugo_Symbol"].append(row.group(1) + "_HUMAN"),
                    dict_df["Family"].append(family),
                )
                for row in [reg_exp.search(";".join(row[1::])) for row in table]
                if row
            ]
        data_df = pd.DataFrame(dict_df)

        return data_df

    # Parse document from url_1 with protein kinases GENES names.
    # Input document: pfam with protein kinases data (Uniprot ID, Gene names, Families).
    def parse_data(self, response_doc):
        # Regex for cleaning text
        # Doc title
        regex_title = re.compile(r"^\s\s*====*$", re.MULTILINE)
        # Cleaning first and last chunks
        regex_peel = re.compile(r"^\s*---*$", re.MULTILINE)
        # Slicing data and data_titles
        regex_data = re.compile(r"^===*$", re.MULTILINE)
        # Dealing with whitespaces inside table rows
        spaces_regex = re.compile(r"\s\s*(?![\(.*\s*\)])")

        title_html = regex_title.split(response_doc)[1].lstrip().rstrip()
        peel_html = [x for x in regex_peel.split(response_doc) if x.find("====") > 0][0]
        data_html = regex_data.split(peel_html)[1 : len(response_doc)]
        data_titles = [x.replace("\n", "") for x in data_html[0::2]]
        data_tables = [x.replace("\n\n", "").split("\n") for x in data_html[1::2]]

        # Creating a dictionary with uniprot ID, Gene Names and Family names of protein kinases titles and content.
        data = {}
        for title, data_table in zip(data_titles, data_tables):
            data[title] = [
                [
                    y.strip().replace(" ", "")
                    for y in spaces_regex.split(x)
                    if len(y) > 1
                ]
                for x in data_table
                if len(x) > 0
            ]

        return title_html, data

    # def preprocessing(self, data):
    #     return data

    # def processing(self, data):
    #     return data

    def data_adapter(self, data):
        # OUTPUT DATA:
        # "dataframe" => Primary dataframe:
        # ID GENE HUGO_SYMBOL FAMILY PDB
        # *    *       *         *    *
        # *    *       *         *    *
        # *    *       *         *    *
        # ==============================
        # "ID" => UNIPROT_ID list
        return {"dataframe": data,"uniprot_ids":data["ID"].to_list()}

