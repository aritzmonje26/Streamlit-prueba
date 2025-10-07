import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo de Widgets de Salida")

# ========================================
# 1. TEXTOS Y TÍTULOS
# ========================================
st.header("1- Textos y Títulos")

st.title("Título Principal")
st.header("Encabezado de Sección")
st.subheader("Sub-encabezado")
st.text("Texto plano simple")
st.write("Write puede mostrar texto, números, dataframes...")
st.markdown("**Negrita**, *cursiva*, y `código`")
st.caption("Esto es una nota pequeñita")

st.write("---")

# ========================================
# 2. MARKDOWN AVANZADO
# ========================================
st.header("2- Markdown con Parámetros")

# Markdown básico
st.markdown("### Título nivel 3 con markdown")

# Markdown con HTML (unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #ff6b6b; padding: 15px; border-radius: 5px; color: white;">
    <h3> Caja roja personalizada</h3>
    <p>Esto usa HTML dentro de markdown</p>
</div>
""", unsafe_allow_html=True)


st.markdown("### Esto es Markdown nivel 3")
st.markdown("Puedes usar **negrita**, *cursiva* y `código`")
st.markdown("""
- Lista item 1
- Lista item 2
- Lista item 3
""")



# CAPTION (texto pequeño)
st.caption("Esto es un caption - texto pequeño para aclaraciones")

st.write("---")



# Caption con HTML
st.caption("""
<span style="color: blue; font-weight: bold;"> Esto usa HTML dentro de caption </span>
""", unsafe_allow_html=True)



st.write("---")

# ========================================
# 3. DATOS Y TABLAS
# ========================================
st.header("3 Datos y Tablas")

# Crear dataframe de ejemplo
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'María'],
    'Edad': [25, 30, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataframe (interactivo)")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("Table (estático)")
    st.table(df)

st.write("---")

# ========================================
# 4. MÉTRICAS
# ========================================
st.header("4- Métricas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Temperatura",
        value="24°C",
        delta="1.2°C"
    )

with col2:
    st.metric(
        label="Usuarios",
        value="1,234",
        delta="-12"
    )

with col3:
    st.metric(
        label="Ventas",
        value="€45K",
        delta="5%"
    )

st.write("---")

# ========================================
# 5. CÓDIGO
# ========================================
st.header("5️ Código")

st.code("""
def saludar(nombre):
    return f"Hola {nombre}!"
    
print(saludar("Ana"))
""", language="python")

st.write("---")

# ========================================
# 6. LATEX (Matemáticas)
# ========================================
st.header("6️ Fórmulas LaTeX")

st.latex(r"\sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n")
st.latex(r"E = mc^2")

st.write("---")

# ========================================
# 7. MENSAJES Y ALERTAS
# ========================================
st.header("7️ Mensajes y Alertas")

st.success("✅ Operación completada con éxito")
st.info("ℹ️ Esta es una información importante")
st.warning("⚠️ Cuidado con esto")
st.error("❌ Ha ocurrido un error")

st.write("---")

# ========================================
# 8. JSON
# ========================================
st.header("8️ JSON (expandible)")

datos_json = {
    "usuario": "Ana",
    "edad": 25,
    "hobbies": ["leer", "nadar", "programar"],
    "direccion": {
        "ciudad": "Madrid",
        "pais": "España"
    }
}

st.json(datos_json)

st.write("---")

# ========================================
# 9. GRÁFICOS
# ========================================
st.header("9️ Gráficos")

# Datos de ejemplo
df_grafico = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 25, 15, 30, 20],
    'z': [5, 15, 10, 20, 25]
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Line Chart (nativo)")
    st.line_chart(df_grafico)

with col2:
    st.subheader("Bar Chart (nativo)")
    st.bar_chart(df_grafico)

# Gráfico Plotly
st.subheader("Gráfico Plotly")
fig = px.scatter(
    df_grafico, 
    x='x', 
    y='y', 
    size='z',
    title="Gráfico de dispersión"
)
st.plotly_chart(fig, use_container_width=True)

st.write("---")

# ========================================
# 10. MULTIMEDIA
# ========================================
st.header("10  Multimedia")

st.subheader("Imagen")
st.image(
    "https://images.unsplash.com/photo-1551522435-a13afa10f103?w=400",
    caption="Imagen de ejemplo",
    use_container_width=True
)

st.write("---")

# ========================================
# 11. PROGRESO Y ANIMACIONES
# ========================================
st.header("1️2 Progreso y Animaciones")

st.subheader("Barra de progreso")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    import time
    time.sleep(0.01)

st.subheader("Spinner de carga")
with st.spinner("Procesando..."):
    time.sleep(2)
st.success("¡Listo!")

st.subheader("Animaciones festivas")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎈 Globos"):
        st.balloons()

with col2:
    if st.button("❄️ Nieve"):
        st.snow()