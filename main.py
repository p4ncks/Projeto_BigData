import streamlit as st
from controller import SalesDataController

def main():
    st.title("Análise de Vendas")

    # upload do csv
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=['csv'])

    if uploaded_file is not None:
        controller = SalesDataController(uploaded_file)
        controller.process_data()

if __name__ == "__main__":
    main()
