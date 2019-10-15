from models.pipelines import Pipeline, Stage
from models.sumoprotkin.predictors import predictors
import pandas as pd
import numpy as np
import os


class Sink(Stage):
    def preprocessing(self, data):
        gpssumo = (
            data["gpssumo"][["ID", "PDB", "CHAIN", "Position", "Score"]]
            .drop_duplicates()
            .reset_index(drop=True)
        )
        sumogo = (
            data["sumogo"][["ID", "PDB", "CHAIN", "Position", "Confidence Score"]]
            .rename(columns={"Confidence Score": "Score"})
            .drop_duplicates()
            .reset_index(drop=True)
        )
        jassa = (
            data["jassa"][["ID", "PDB", "CHAIN", "Position", "DB_All_Score_Cons"]]
            .rename(columns={"DB_All_Score_Cons": "Score"})
            .drop_duplicates()
            .reset_index(drop=True)
        )

        gpssumo["Score"] = gpssumo["Score"].astype("float64") / np.max(
            gpssumo["Score"].astype("float64")
        )
        sumogo["Score"] = sumogo["Score"].astype("float64") / np.max(
            sumogo["Score"].astype("float64")
        )
        jassa["Score"] = jassa["Score"] / np.max(jassa["Score"].astype("float64"))

        gpssumo["Position"] = gpssumo["Position"].astype("int32")
        sumogo["Position"] = sumogo["Position"].astype("int32")
        jassa["Position"] = jassa["Position"].astype("int32")

        gpssumo["Predictor"] = "GPSSumo"
        sumogo["Predictor"] = "SumoGo"
        jassa["Predictor"] = "Jassa"
        total = pd.concat([jassa, gpssumo, sumogo], ignore_index=True)

        data["total"] = total

        return data

    def processing(self, data):
        import altair as alt

        chart = (
            alt.Chart(data["total"][data["total"]["ID"] == "P34947"])
            .mark_point()
            .encode(x="Position:O", y="Score:Q", color="Predictor:N",tooltip=["Position","Score","Predictor"])
            .interactive()
        )

        source2 = alt.pd.DataFrame(
            [{"start": "100", "end": "200", "domain": "Kinase Domain"}]
        )

        rect = (
            alt.Chart(source2)
            .mark_rect( fillOpacity=0.15)
            .encode(x="start:O", x2="end:O", color="domain:N")
        )
        text = rect.mark_text(
            align="left",
            baseline="middle",
            fontSize=10,
            fontWeight=700
        ).encode(text="domain:N", opacity=alt.value(1))
        Chart = (rect + text + chart).properties(width=600, height=300)
        Chart.configure(autosize="fit").save('chart.html')
        print(data["sumogo"]["ID"].drop_duplicates())

        print(data["dataframe"])
        print(data["gpssumo"])
        print(data["sumogo"])
        print(data["jassa"])
        return data

    def data_adapter(self, data):
        return data
