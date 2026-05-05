import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')

st.title("🏛️ Consulta de Deputados por Partido")

col1, col2, col3 = st.columns(3)

with col1:
    lista_partidos = sorted(df['partido'].unique().tolist())
    partido_sel = st.selectbox("Partido:", ["Todos"] + lista_partidos)

with col2:
    lista_sexo = sorted(df['sexo'].unique().tolist())
    sexo_sel = st.selectbox("Sexo:", ["Todos"] + lista_sexo)

with col3:
    lista_uf = sorted(df['uf'].unique().tolist())
    uf_sel = st.selectbox("UF:", ["Todos"] + lista_uf)

df_filtrado = df.copy()

if partido_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado['partido'] == partido_sel]

if sexo_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado['sexo'] == sexo_sel]

if uf_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado['uf'] == uf_sel]

if df_filtrado.empty:
    st.warning("Nenhum deputado encontrado para essa combinação de filtros.")


    
st.write(f"Encontrados **{len(df_filtrado)}** deputados com esses critérios.")
st.dataframe(df_filtrado, use_container_width=True)
