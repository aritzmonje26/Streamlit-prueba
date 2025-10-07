import streamlit as st
import pandas as pd
import seaborn as sns

st.title(" Iris - Ejercicio 1: Sidebar")

# Cargar datos
df = sns.load_dataset('iris')
min_sepal = df["sepal_length"].min()
max_sepal = df["sepal_length"].max()
# TODO 1: Crear un sidebar con:

with st.sidebar:
# - Título "Filtros"
    st.sidebar.title("Filtros")
# - Multiselect para elegir especies
    especie = st.sidebar.multiselect("Dime una especie de planta",
                                     options=list(df["species"].unique()),
                                     default=["setosa"])

# - Slider para longitud de sépalo
    largo = st.slider("Longitud minima del sépalo (cm)", 
                              min_value=(min_sepal), 
                              max_value=(max_sepal), 
                              value=(min_sepal)
                              )

# TODO 2: Filtrar el dataframe según las selecciones

df_filtrado = df[df["species"].isin(especie)]
df_filtrado = df_filtrado[df_filtrado["sepal_length"] >= largo]



# TODO 3: Mostrar:
# - Cuántas flores cumplen los filtros
st.write(f"Se filtraron {len(df_filtrado)} flores")

# - La tabla filtrada
st.dataframe(df_filtrado)
