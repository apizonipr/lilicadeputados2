import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')

st.title("🏛️ Consulta de Deputados por Partido")

with col1:
    lista_partidos = sorted(df['partido'].unique().tolist())
    partido_sel = st.selectbox("Partido:", ["Todos"] + lista_partidos)

with col2:
    # Ajuste 'sexo' para o nome exato da coluna no seu CSV (ex: 'genero', 'Sexo')
    lista_sexo = sorted(df['sexo'].unique().tolist())
    sexo_sel = st.selectbox("Sexo:", ["Todos"] + lista_sexo)

# --- LÓGICA DE FILTRAGEM COMBINADA ---
df_filtrado = df.copy()

if partido_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado['partido'] == partido_sel]

if sexo_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado['sexo'] == sexo_sel]

# --- EXIBIÇÃO DOS RESULTADOS ---
st.write(f"Encontrados **{len(df_filtrado)}** deputados com esses critérios.")
st.dataframe(df_filtrado, use_container_width=True)
