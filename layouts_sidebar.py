import streamlit as st

st.title("🏠 Página Principal")

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.title("🎛️ Panel de Control")
    
    # Widgets en el sidebar
    nombre = st.text_input("Tu nombre:")
    edad = st.slider("Tu edad:", 0, 100, 25)
    
    st.write("---")
    
    # Menú de navegación
    st.subheader("📋 Menú")
    opcion = st.radio(
        "Ir a:",
        ["Inicio", "Análisis", "Configuración"]
    )

    st.write("---")
    with st.expander("Sección 1"):
        st.write("Opciones 1")
    
    with st.expander("Sección 2"):
        st.write("Opciones 2")

# ============================================
# CONTENIDO PRINCIPAL
# ============================================
st.write(f"Hola {nombre}, tienes {edad} años")
st.write(f"Has seleccionado: {opcion}")