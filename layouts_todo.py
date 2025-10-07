import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

# ============================================
# SIDEBAR - Controles
# ============================================
with st.sidebar:
    st.title("🎛️ Controles")
    
    fecha_inicio = st.date_input("Fecha inicio")
    fecha_fin = st.date_input("Fecha fin")
    
    st.write("---")
    
    filtros = st.multiselect(
        "Filtros:",
        ["Ventas", "Marketing", "Soporte"]
    )

# ============================================
# HEADER - Título y métricas
# ============================================
st.title("📊 Dashboard Empresarial")

# COLUMNS para métricas
col1, col2, col3, col4 = st.columns(4)

col1.metric("Ingresos", "€123K", "+12%")
col2.metric("Usuarios", "45.2K", "+5%")
col3.metric("Conversión", "3.2%", "-0.5%")
col4.metric("Satisfacción", "4.8/5", "+0.2")

st.write("---")

# ============================================
# TABS - Diferentes vistas
# ============================================
tab1, tab2, tab3 = st.tabs(["📊 Resumen", "📈 Análisis", "📋 Datos"])

with tab1:
    # COLUMNS para gráficos lado a lado
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Ventas por Mes")
        st.line_chart([10, 20, 30, 25, 35, 40])
    
    with col_right:
        st.subheader("Distribución por Categoría")
        st.bar_chart([15, 25, 35, 25])

with tab2:
    st.subheader("Análisis Detallado")
    
    # EXPANDER con info adicional
    with st.expander("Ver metodología"):
        st.write("Aquí va la explicación de cómo se calculan las métricas...")
    
    # Gráfico principal
    df = pd.DataFrame({
        'mes': ['Ene', 'Feb', 'Mar', 'Abr'],
        'ventas': [100, 150, 120, 180]
    })
    fig = px.line(df, x='mes', y='ventas')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Tabla de Datos")
    
    df_completo = pd.DataFrame({
        'Producto': ['A', 'B', 'C', 'D'],
        'Ventas': [100, 150, 120, 180],
        'Stock': [50, 30, 45, 60]
    })
    
    st.dataframe(df_completo, use_container_width=True)

# ============================================
# FOOTER - Información adicional
# ============================================
with st.expander("ℹ️ Acerca de este dashboard"):
    st.write("Dashboard creado con Streamlit")
    st.write("Última actualización: 2024")