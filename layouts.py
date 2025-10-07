import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title(" Los 6 Layouts de Streamlit")

# Cargar datos
df = sns.load_dataset('penguins')

st.write("---")

# ========================================
# 1. SIDEBAR (Panel lateral)
# ========================================
st.header("1️ SIDEBAR - Panel Lateral")

with st.sidebar:
    st.title(" Panel de Control")
    st.write("Este es el sidebar")
    especie_sidebar = st.selectbox("Especie:", df['species'].unique())
    st.info("El sidebar siempre está visible a la izquierda")
    with st.sidebar:
        st.title(" Panel de Control")
        st.write("Este es el sidebar")
        especie_sidebar = st.selectbox("Especie:", df['bill_depth_mm'].unique())
        st.info("El sidebar siempre está visible a la izquierda")

st.write(f"Especie seleccionada en sidebar: **{especie_sidebar}**")

st.write("---")

# ========================================
# 2. COLUMNS (Columnas)
# ========================================
st.header("2️ COLUMNS - Dividir en Columnas")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Columna 1")
    st.metric("Total Pingüinos", len(df))

with col2:
    st.subheader("Columna 2")
    st.metric("Especies", df['species'].nunique())

with col3:
    st.subheader("Columna 3")
    st.metric("Islas", df['island'].nunique())

st.write("---")

# ========================================
# 3. TABS (Pestañas)
# ========================================
st.header("3️ TABS - Pestañas")

tab1, tab2, tab3 = st.tabs(["📊 Datos", "📈 Gráficos", "📋 Info"])

with tab1:
    st.subheader("Vista de Datos")
    st.dataframe(df.head(10))

with tab2:
    st.subheader("Gráfico")
    fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Información del Dataset")
    st.write(df.describe())

st.write("---")

# ========================================
# 4. EXPANDER (Secciones colapsables)
# ========================================
st.header("4️ EXPANDER - Secciones Colapsables")

with st.expander(" Ver descripción del dataset"):
    st.write("""
    El dataset de Palmer Penguins contiene medidas de 3 especies de pingüinos:
    - **Adelie**
    - **Chinstrap** 
    - **Gentoo**
    """)
    st.dataframe(df.describe())

with st.expander(" Ver datos crudos"):
    st.dataframe(df)

st.write("---")

# ========================================
# 5. CONTAINER (Contenedor para agrupar)
# ========================================
st.header("5️ CONTAINER - Contenedor")

container1 = st.container()
st.write("Este texto está FUERA del container")

with container1:
    st.info("Todo esto está DENTRO del container")
    st.write("Los containers permiten agrupar elementos")
    st.dataframe(df.head(3))

st.write("---")

# ========================================
# 6. EMPTY (Placeholder que se puede llenar después)
# ========================================
st.header("6️ EMPTY - Placeholder Dinámico")

placeholder = st.empty()

# Primero mostramos una cosa
placeholder.text("⏳ Cargando datos...")

# Simulamos procesamiento
import time
time.sleep(2)

# Luego lo reemplazamos
placeholder.success(" ¡Datos cargados correctamente!")