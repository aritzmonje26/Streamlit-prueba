# ejercicio_5_multiselect.py
"""
ENTRADA: st.multiselect() + st.checkbox()
SALIDAS: st.write(), st.dataframe(), st.metric()
OBJETIVO: Seleccionar MÚLTIPLES opciones + personalizar interfaz
"""

import streamlit as st
import seaborn as sns

st.title(" Ejercicio 8: Multiselect")

st.divider()
st.info(" Multiselect es útil cuando quieres comparar múltiples categorías")
# ═══════════════════════════════════════════
# CHECKBOX: Activar/desactivar fondo de color
# ═══════════════════════════════════════════
usar_color_fondo = st.checkbox(" Activar fondos de color en las cabeceras", value=True)

# Cargar datos
penguins = sns.load_dataset('penguins')

st.write("Multiselect permite elegir VARIAS opciones a la vez:")

# ═══════════════════════════════════════════
# ENTRADA 1: Multiselect para especies
# ═══════════════════════════════════════════

# Cabecera con o sin fondo según checkbox
if usar_color_fondo:
    st.markdown("""
    <div style='background-color: #e3f2fd; padding: 10px; border-radius: 5px;'>
        <h3 style='color: #1976d2; margin: 0;'>🐧 Seleccionar Especies</h3>
    </div>
    """, unsafe_allow_html=True)
else:
    st.subheader(" Seleccionar Especies")

st.write("")  # Espacio

especies_seleccionadas = st.multiselect(
    "Elige una o más especies:",
    options=list(penguins['species'].unique()),
    default=["Adelie"]  # Por defecto, Adelie está seleccionado
)

# Validar selección
if especies_seleccionadas:
    datos_especies = penguins[penguins['species'].isin(especies_seleccionadas)]
    
    st.success(f" Has seleccionado {len(especies_seleccionadas)} especie(s)")
    st.write(f"**Total de pingüinos**: {len(datos_especies)}")
    
    st.dataframe(datos_especies)
    
    # Estadísticas por especie
    st.divider()
    
    if usar_color_fondo:
        st.markdown("""
        <div style='background-color: #fff3e0; padding: 10px; border-radius: 5px;'>
            <h3 style='color: #f57c00; margin: 0;'> Estadísticas por Especie Seleccionada</h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.subheader(" Estadísticas por Especie Seleccionada")
    
    st.write("")  # Espacio
    
    for especie in especies_seleccionadas:
        datos_esp = datos_especies[datos_especies['species'] == especie]
        st.write(f"**{especie}**: {len(datos_esp)} pingüinos")
        st.write(f"   - Masa promedio: {datos_esp['body_mass_g'].mean():.0f}g")
        st.write(f"   - Pico promedio: {datos_esp['bill_length_mm'].mean():.1f}mm")
else:
    st.warning(" Selecciona al menos una especie")

st.divider()

# ═══════════════════════════════════════════
# ENTRADA 2: Multiselect para islas
# ═══════════════════════════════════════════

if usar_color_fondo:
    st.markdown("""
    <div style='background-color: #e8f5e9; padding: 10px; border-radius: 5px;'>
        <h3 style='color: #388e3c; margin: 0;'>🏝️ Seleccionar Islas</h3>
    </div>
    """, unsafe_allow_html=True)
else:
    st.subheader(" Seleccionar Islas")

st.write("")  # Espacio

islas_seleccionadas = st.multiselect(
    "Elige una o más islas:",
    options=list(penguins['island'].unique()),
    default=list(penguins['island'].unique())  # Todas por defecto
)

if islas_seleccionadas:
    datos_islas = penguins[penguins['island'].isin(islas_seleccionadas)]
    
    st.write(f"**Pingüinos en isla(s) seleccionada(s)**: {len(datos_islas)}")
    
    # Distribución por isla
    for isla in islas_seleccionadas:
        cantidad = len(datos_islas[datos_islas['island'] == isla])
        st.metric(f"Isla {isla}", cantidad)

