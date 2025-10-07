"""
ENTRADA: st.slider()
SALIDAS: st.write(), st.dataframe(), st.metric()
OBJETIVO: Seleccionar un valor o rango numérico
"""

import streamlit as st
import seaborn as sns

st.title(" Ejercicio 7: Slider")

# Cargar datos
penguins = sns.load_dataset('penguins')


st.write("Los sliders permiten elegir valores numéricos:")

# ═══════════════════════════════════════════
# ENTRADA 1: Slider para masa corporal mínima
# ═══════════════════════════════════════════
st.subheader("Filtrar por Masa Corporal")

masa_minima = st.slider(
    "Masa corporal mínima (gramos):",
    min_value=int(penguins['body_mass_g'].min()),
    max_value=int(penguins['body_mass_g'].max()),
    value=int(penguins['body_mass_g'].min()),
    step=100
)

# Filtrar datos
datos_filtrados = penguins[penguins['body_mass_g'] >= masa_minima]

# ═══════════════════════════════════════════
# SALIDAS: Resultados del filtro
# ═══════════════════════════════════════════
st.write(f"**Pingüinos con masa ≥ {masa_minima}g:** {len(datos_filtrados)}")
st.dataframe(datos_filtrados)

st.divider()

# ═══════════════════════════════════════════
# ENTRADA 2: Slider para rango de longitud de pico
# ═══════════════════════════════════════════
st.subheader("Filtrar por Rango de Longitud de Pico")

rango_pico = st.slider(
    "Rango de longitud del pico (mm):",
    min_value=float(penguins['bill_length_mm'].min()),
    max_value=float(penguins['bill_length_mm'].max()),
    value=(float(penguins['bill_length_mm'].min()), float(penguins['bill_length_mm'].max())),
    step=0.5
)

# Filtrar por rango
datos_rango = penguins[
    (penguins['bill_length_mm'] >= rango_pico[0]) &
    (penguins['bill_length_mm'] <= rango_pico[1])
]

st.write(f"**Pingüinos con pico entre {rango_pico[0]}mm y {rango_pico[1]}mm:** {len(datos_rango)}")

# Estadísticas del rango
st.metric("Masa Promedio", f"{datos_rango['body_mass_g'].mean():.0f} g")
st.metric("Especies Diferentes", datos_rango['species'].nunique())

st.divider()

# ═══════════════════════════════════════════
# ENTRADA 3: Slider para número de filas a mostrar
# ═══════════════════════════════════════════
st.subheader("Controlar Visualización")

num_filas = st.slider(
    "¿Cuántas filas mostrar?",
    min_value=5,
    max_value=50,
    value=10,
    step=5
)

st.write(f"**Mostrando {num_filas} filas:**")
st.dataframe(datos_rango.head(num_filas))

st.divider()
st.info(" Los sliders son perfectos para valores numéricos y rangos")