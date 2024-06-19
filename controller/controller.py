from model import SalesDataLoader
from view import VizualizacaoDados

class SalesDataController:
    def __init__(self, file_path):
        self.data_loader = SalesDataLoader(file_path)
        self.view = VizualizacaoDados()

    def process_data(self):
        data = self.data_loader.df
        total_do_mes = data['ValorTotalVenda'].sum()
        self.view.exibir_pagina(data, total_do_mes)
