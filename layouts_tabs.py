import streamlit as st
import pandas as pd

st.title(" Ejemplo con Tabs")

# ============================================
# CREAR TABS
# ============================================
tab1, tab2, tab3 = st.tabs([" Datos", " Gráficos", " Configuración"])

# ============================================
# TAB 1: DATOS
# ============================================
with tab1:
    st.header("Tabla de Datos")
    
    df = pd.DataFrame({
        'Producto': ['Laptop', 'Mouse', 'Teclado'],
        'Precio': [899, 25, 75],
        'Stock': [15, 50, 30]
    })
    
    st.dataframe(df, use_container_width=True)
    
    # Botón de descarga
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        " Descargar CSV",
        data=csv,
        file_name="datos.csv",
        mime="text/csv"
    )

# ============================================
# TAB 2: GRÁFICOS
# ============================================
with tab2:
    st.header("Visualizaciones")
    
    st.line_chart(df.set_index('Producto')['Precio'])
    
    st.bar_chart(df.set_index('Producto')['Stock'])

# ============================================
# TAB 3: CONFIGURACIÓN
# ============================================
with tab3:
    st.header("Opciones")
    
    tema = st.selectbox("Tema:", ["Claro", "Oscuro"])
    mostrar_grid = st.checkbox("Mostrar cuadrícula")
    
    st.write(f"Tema seleccionado: {tema}")
    st.write(f"Grid: {'Activado' if mostrar_grid else 'Desactivado'}")