import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')

col1, col2 = st.columns(2)

st.title("🏛️ Consulta de Deputados por Partido")

with col1:
    lista_partidos = sorted(df['partido'].unique().tolist())
    partido_sel = st.selectbox("Partido:", ["Todos"] + lista_partidos)

with col2:
    lista_genero = sorted(df['genero'].unique().tolist())
    genero_sel = st.selectbox("Genero:", ["Todos"] + lista_genero)
    
df_filtrado = df.copy()

if partido_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado['partido'] == partido_sel]

if genero_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado['genero'] == genero_sel]

st.write(f"Encontrados **{len(df_filtrado)}** deputados com esses critérios.")
st.dataframe(df_filtrado, use_container_width=True)
