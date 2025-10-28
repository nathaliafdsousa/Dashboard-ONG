import streamlit as st
import random
import pandas as pd
import plotly.express as px

# ---- Título ----
st.title("📊 Dashboard de Doações - ONG")

meses = ["Janeiro", "Fevereiro", "Março"]
dados = []

for mes in meses:
    dinheiro = random.randint(5000, 15000)
    alimento = random.randint(3000, 12000)
    dados.append({"Mês": mes, "Dinheiro": dinheiro, "Alimentos": alimento})

df = pd.DataFrame(dados)


st.subheader("Distribuição de Doações por Mês")


for i, row in df.iterrows():
    valores = {"Dinheiro": row["Dinheiro"], "Alimentos": row["Alimentos"]}
    grafico = px.pie(
        names=valores.keys(),
        values=valores.values(),
        title=f"Doações em {row['Mês']}",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(grafico, use_container_width=True)


st.markdown("---")
st.subheader("Resumo Geral")
st.write(df)
st.success(f"Total arrecadado: R$ {df['Dinheiro'].sum() + df['Alimentos'].sum():,.2f}")

