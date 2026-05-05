import streamlit as st
import pandas as pd
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

st.title("🏛️ Consulta de Deputados por Partido")

lista_partidos = sorted(df['partido'].unique().tolist()) 

st.sidebar.header("Filtros")
partido_selecionado = st.sidebar.selectbox(
    "Escolha um partido para filtrar:",
    ["Todos"] + lista_partidos
)

if partido_selecionado != "Todos":
    df_filtrado = df[df['partido'] == partido_selecionado]
else:
    df_filtrado = df

st.subheader(f"Resultados: {partido_selecionado}")
st.write(f"Encontrados {len(df_filtrado)} deputados.")

st.dataframe(df_filtrado, use_container_width=True)
