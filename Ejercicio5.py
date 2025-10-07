# ejercicio_2_selectbox.py
"""
ELEMENTOS:
- ENTRADA: st.selectbox()
- LÓGICA: Filtrado de DataFrame
- SALIDAS: st.write(), st.dataframe(), st.metric()
"""

import streamlit as st
import seaborn as sns

st.title("🐧 Ejercicio 5: Selectbox")
st.write("**Objetivo**: Filtrar datos por especie")

# Cargar datos
penguins = sns.load_dataset('penguins')

# ═══════════════════════════════════════════
# ENTRADA: Selectbox
# ═══════════════════════════════════════════
especie = st.selectbox(
    "Selecciona una especie:",
    ["Todas"] + list(penguins['species'].unique())
)

# ═══════════════════════════════════════════
# LÓGICA: Filtrado
# ═══════════════════════════════════════════
if especie == "Todas":
    datos_filtrados = penguins
else:
    datos_filtrados = penguins[penguins['species'] == especie]

# ═══════════════════════════════════════════
# SALIDAS (una tras otra, sin layouts)
# ═══════════════════════════════════════════
st.subheader(f" Datos de: {especie}")
st.write(f"**Pingüinos encontrados**: {len(datos_filtrados)}")

# Mostrar datos
st.dataframe(datos_filtrados)

# Estadísticas (si no es "Todas")
if especie != "Todas":
    st.divider()
    st.subheader(f" Estadísticas {especie}")
    
    # Métricas una debajo de otra
    st.metric("Masa Corporal Promedio", f"{datos_filtrados['body_mass_g'].mean():.0f} g")
    st.metric("Longitud Pico Promedio", f"{datos_filtrados['bill_length_mm'].mean():.1f} mm")
    st.metric("Longitud Aleta Promedio", f"{datos_filtrados['flipper_length_mm'].mean():.1f} mm")
