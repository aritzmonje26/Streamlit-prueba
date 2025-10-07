# ejercicio_3_selectbox.py
"""
ENTRADA: st.selectbox()
SALIDAS: st.write(), st.dataframe(), st.metric()
OBJETIVO: Seleccionar de un menú desplegable
"""

import streamlit as st
import seaborn as sns


st.title(" Ejercicio 3: Selectbox")

# Cargar datos
penguins = sns.load_dataset('penguins')

st.write("El selectbox es como un menú desplegable:")

# ═══════════════════════════════════════════
# ENTRADA 1: Selectbox para isla
# ═══════════════════════════════════════════
st.subheader("Filtrar por Isla")

isla = st.selectbox(
    "Selecciona una isla:",
    ["Todas"] + list(penguins['island'].unique())
)

# Lógica de filtrado
if isla == "Todas":
    datos = penguins
else:
    datos = penguins[penguins['island'] == isla]

# ═══════════════════════════════════════════
# SALIDAS: Información de la isla
# ═══════════════════════════════════════════
st.subheader(f" Isla: {isla}")
st.write(f"**Pingüinos en esta isla**: {len(datos)}")

# Mostrar datos
st.dataframe(datos)

# Especies en esta isla
if isla != "Todas":
    st.divider()
    st.subheader(" Especies en esta Isla")
    especies_en_isla = datos['species'].value_counts()
    
    for especie, cantidad in especies_en_isla.items():
        st.metric(f"{especie}", cantidad)

st.divider()

# ═══════════════════════════════════════════
# ENTRADA 2: Selectbox para variable a explorar
# ═══════════════════════════════════════════
st.subheader("Explorar Variables")

variable = st.selectbox(
    "Selecciona una variable numérica:",
    ['body_mass_g', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
)

# Mostrar estadísticas de la variable
st.write(f"**Estadísticas de {variable}:**")
st.metric("Media", f"{datos[variable].mean():.2f}")
st.metric("Mediana", f"{datos[variable].median():.2f}")
st.metric("Mínimo", f"{datos[variable].min():.2f}")
st.metric("Máximo", f"{datos[variable].max():.2f}")

st.divider()
st.info(" El selectbox ahorra espacio cuando hay muchas opciones")