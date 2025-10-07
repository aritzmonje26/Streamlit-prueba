import streamlit as st

st.title(" Ejemplo con Expanders")

# ============================================
# EXPANDER BÁSICO (cerrado por defecto)
# ============================================
with st.expander("ℹ Ver más información"):
    st.write("""
    Esta es información adicional que está oculta por defecto.
    
    - Punto 1
    - Punto 2
    - Punto 3
    """)
    
    st.image("https://via.placeholder.com/400x200")

# ============================================
# EXPANDER ABIERTO (expanded=True)
# ============================================
with st.expander("⚠️ Información importante", expanded=True):
    st.warning("Este mensaje es importante y está visible desde el inicio")
    st.write("Pero el usuario puede cerrarlo si quiere")

# ============================================
# MÚLTIPLES EXPANDERS
# ============================================
with st.expander("📊 Estadísticas detalladas"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Media", "45.6")
    
    with col2:
        st.metric("Mediana", "42.1")

with st.expander("📈 Gráficos adicionales"):
    st.line_chart([1, 2, 3, 4, 5])

with st.expander("⚙️ Configuración avanzada"):
    opcion1 = st.checkbox("Opción 1")
    opcion2 = st.checkbox("Opción 2")