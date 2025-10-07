import streamlit as st
import seaborn as sns



"""
OBJETIVO: Aprender los elementos básicos de SALIDA en Streamlit
- st.title()
- st.write()
- st.dataframe()
- st.metric()
"""

import streamlit as st
import seaborn as sns

# SALIDAS: Títulos y texto
st.title(" Mi Primera App con Penguins")
st.write("Análisis de pingüinos")

# Cargar datos
penguins = sns.load_dataset('penguins')

# SALIDA: Información básica
st.write(f"Este dataset tiene {len(penguins)} pingüinos")
st.write(f"Con {len(penguins.columns)} columnas")

# SALIDA: Mostrar datos en tabla
st.subheader(" Datos de Pingüinos")
st.dataframe(penguins.head(10))

# SALIDA: Métricas
st.subheader(" Información General")
st.metric("Total de Pingüinos", len(penguins))
st.metric("Número de Especies", penguins['species'].nunique())