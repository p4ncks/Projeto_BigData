import pandas as pd
from pyspark.sql import SparkSession

class SalesDataLoader:
    def __init__(self, file_path):
        self.spark = SparkSession.builder \
            .appName("Sales Visualization") \
            .getOrCreate()
        self.file_path = file_path
        self.df = None
        self.load_data()

    def load_data(self):
        self.df = self.spark.read.csv(self.file_path, header=True, inferSchema=True).toPandas()
        self.df["DataVenda"] = pd.to_datetime(self.df["DataVenda"], errors="coerce")
        self.df = self.df.dropna(subset=["DataVenda"])
        self.df = self.df.sort_values("DataVenda")
        self.criar_coluna_mes()

    def criar_coluna_mes(self) -> None:
        self.df["Mes"] = self.df["DataVenda"].dt.strftime("%Y-%m")

    def obter_dados_por_mes(self, mes: str) -> pd.DataFrame:
        return self.df[self.df["Mes"] == mes]

    def calcular_total_do_mes(self, mes: str, coluna_alvo: str = "Total") -> float:
        df_mes = self.obter_dados_por_mes(mes)
        total_mes = df_mes[coluna_alvo].sum()
        return total_mes
