import streamlit as st
import plotly.express as px
import pandas as pd

class VizualizacaoDados:
    def exibir_pagina(self, df_filtrado: pd.DataFrame, total_do_mes: float) -> None:
        st.write(f"Total do mês: {total_do_mes}")

        col1, col2 = st.columns(2)
        col3 = st.columns(1)[0]
        col4, col5, col6 = st.columns(3)
        col7 = st.columns(1)[0]

        fig_payment_method = px.pie(
            df_filtrado,
            values='ValorTotalVenda',
            names='FormaPagamento',
            title='Faturamento por método de pagamento'
        )
        fig_city_sales = px.bar(
            df_filtrado,
            x='FormaPagamento',
            y='ValorTotalVenda',
            title='Faturamento por forma de pagamento',
            labels={'FormaPagamento': 'Forma de Pagamento', 'ValorTotalVenda': 'Valor Total de Venda'},
            color='FormaPagamento'
        )
        fig_produto_mais_vendido = px.line(
            df_filtrado,
            x='Mes',
            y='Produto',
            color='Produto',
            title='Produto mais vendido'
        )
        fig_venda_x_comissao = px.scatter(
            df_filtrado,
            x='ValorVenda',
            y='ValorComissão',
            color='Status',
            title='Valor da Venda vs Valor da Comissão',
            labels={'ValorVenda': 'Valor da Venda', 'ValorComissão': 'Valor da Comissão'}
        )
        fig_histograma = px.histogram(
            df_filtrado,
            x='ValorVenda',
            title='Distribuição do Valor das Vendas'
        )

        col1.plotly_chart(fig_payment_method)
        col2.plotly_chart(fig_city_sales)
        col3.plotly_chart(fig_produto_mais_vendido)
        col4.plotly_chart(fig_venda_x_comissao)
        col5.plotly_chart(fig_histograma)
