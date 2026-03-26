import streamlit as st
import pandas as pd

# URL da sua planilha
url = "https://docs.google.com/spreadsheets/d/1y06RxnrltG1VqHS1pomuY-ZoeND0jBPU8S41OHnUSHc/export?format=csv"

# Ler dados
df = pd.read_csv(url)

st.title("📊 Controle de Contas")

st.dataframe(df)
