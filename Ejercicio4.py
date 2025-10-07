# ejercicio_4_radio.py
"""
ELEMENTOS BÁSICOS:
- ENTRADA: st.radio()
- LÓGICA: Filtrado por selección única
- SALIDAS: st.dataframe(), st.metric()
"""

import streamlit as st
import seaborn as sns


st.title(" Ejercicio 4: Radio (selección única)")
st.write("**Objetivo**: Filtrar por especie y mostrar datos/contador")

# Cargar datos
penguins = sns.load_dataset('penguins')

# ENTRADA: Radio
especie = st.radio("Elige especie", sorted(penguins["species"].unique()))

# LÓGICA: Filtrar por especie
sub = penguins[penguins["species"] == especie]

# SALIDAS
st.subheader(f" Datos de {especie}")
st.dataframe(sub) 
st.metric("Nº registros", len(sub))
