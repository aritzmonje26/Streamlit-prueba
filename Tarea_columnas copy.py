import streamlit as st
import pandas as pd
import seaborn as sns

st.title(" Iris - Ejercicio 2: Métricas")

# Cargar datos
df = sns.load_dataset('iris')


min_sepal = df["sepal_length"].min()
max_sepal = df["sepal_length"].max()
# TODO 1: Crear sidebar (igual que ejercicio 1)
with st.sidebar:
# - Título "Filtros"
    st.sidebar.title("Filtros")
# - Multiselect para elegir especies
    especie = st.sidebar.multiselect("Dime una especie de planta",
                                     options=list(df["species"].unique()),
                                     default=["setosa"])
    if not especie:

        st.info("Selecciona al menos una especie")


# - Slider para longitud de sépalo
    largo = st.slider("Longitud minima del sépalo (cm)", 
                              min_value=(min_sepal), 
                              max_value=(max_sepal), 
                              value=(min_sepal)
                              )



# TODO 3: Crear 4 columnas con métricas:
st.header("Métricas")
st.subheader("Total de flores")
col1, col2, col3, col4 = st.columns(4)

# - Columna 1: Total de flores
with col1:
    st.metric(label="Total de flores", value=len(df))
# - Columna 2: Especies diferentes
with col2:
    st.metric(label="Especies diferentes", value=df['species'].nunique())
# - Columna 3: Longitud media de sépalo
with col3:
    st.metric("Longitud media de sépalo", round(df['sepal_length'].mean(), 2))
# - Columna 4: Ancho medio de pétalo
with col4:
    st.metric("Ancho medio de pétalo", round(df['petal_width'].mean(), 2))

# TODO 4: Debajo mostrar la tabla filtrada
if especie:
    df_filtrado = df[df["species"].isin(especie)]
    df_filtrado = df_filtrado[df_filtrado["sepal_length"] >= largo]
    if not df_filtrado.empty:
        st.header("Resultados del Filtro")
        st.dataframe(df_filtrado)
    else:
        st.error("No hay registros que coincidan con los filtros seleccionados.")
else:
    st.info("Selecciona al menos una especie")