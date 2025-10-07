import streamlit as st
import time

st.title(" Ejemplo con Empty")

# ============================================
# EMPTY BÁSICO
# ============================================
placeholder = st.empty()

# Mostrar algo inicialmente
placeholder.text("⏳ Cargando...")

# Simular procesamiento
time.sleep(2)

# Reemplazar el contenido
placeholder.success("✅ ¡Cargado!")

# ============================================
# EMPTY PARA ACTUALIZAR CONTENIDO
# ============================================
st.subheader("Contador dinámico")

contador_placeholder = st.empty()

if st.button("▶️ Iniciar contador"):
    for i in range(10):
        contador_placeholder.metric(
            label="Contador",
            value=i + 1
        )
        time.sleep(0.5)
    
    contador_placeholder.success("✅ ¡Completado!")

# ============================================
# EMPTY PARA BORRAR CONTENIDO
# ============================================
mensaje = st.empty()
mensaje.info("Este mensaje desaparecerá...")

if st.button("🗑️ Borrar mensaje"):
    mensaje.empty()  # Borra todo el contenido