import streamlit as st

st.title(" Dashboard con Columnas")

# ============================================
# 3 COLUMNAS IGUALES
# ============================================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Usuarios",
        value="1,234",
        delta="+10%"
    )

with col2:
    st.metric(
        label="Ventas",
        value="€45K",
        delta="-5%"
    )

with col3:
    st.metric(
        label="Visitas",
        value="9,876",
        delta="+23%"
    )

st.write("---")

# ============================================
# 2 COLUMNAS CON ANCHOS DIFERENTES
# ============================================
col_grande, col_pequeña = st.columns([3, 1])

with col_grande:
    st.subheader("Gráfico Principal")
    st.line_chart([1, 2, 3, 4, 5])

with col_pequeña:
    st.subheader("Info")
    st.write("Datos extra aquí")

st.write("---")

# ============================================
# 4 COLUMNAS
# ============================================
col1, col2, col3, col4 = st.columns(4)

col1.image("https://via.placeholder.com/150", caption="Imagen 1")
col2.image("https://via.placeholder.com/150", caption="Imagen 2")
col3.image("https://via.placeholder.com/150", caption="Imagen 3")
col4.image("https://via.placeholder.com/150", caption="Imagen 4")