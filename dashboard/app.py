import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.title("📊 Dashboard de Doações - ONG")

# --- CONEXÃO COM A API ---
API_URL = "http://api:5000/doacoes"   # nome do serviço do docker-compose

try:
    response = requests.get(API_URL)
    response.raise_for_status()  # dispara erro caso status != 200
    df = pd.DataFrame(response.json())  # transforma JSON → DataFrame
except:
    st.error("❌ Erro ao conectar com a API. Verifique se o container da API está rodando.")
    st.stop()

# --- GRÁFICOS DOS MESES ---
st.subheader("Distribuição de Doações por Mês")

for _, row in df.iterrows():
    valores = {
        "Dinheiro": row["Dinheiro"],
        "Alimentos": row["Alimentos"],
        "Produtos de Limpeza": row["Produtos de Limpeza"]
    }

    fig = px.pie(
        names=valores.keys(),
        values=valores.values(),
        title=f"Doações em {row['Mês']}",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig, use_container_width=True)

# --- RESUMO GERAL ---
st.markdown("---")
st.subheader("Resumo Geral")
st.write(df)

total = df["Dinheiro"].sum() + df["Alimentos"].sum() + df["Produtos de Limpeza"].sum()
st.success(f"💰 Total arrecadado: R$ {total:,.2f}")

