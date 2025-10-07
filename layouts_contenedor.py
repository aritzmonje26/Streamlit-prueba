import streamlit as st

st.title(" Ejemplo con Containers")

# ============================================
# CONTAINER BÁSICO
# ============================================
container1 = st.container()

st.write("Este texto está FUERA del container")

with container1:
    st.info("Este texto está DENTRO del container")
    st.write("Puedes agrupar varios elementos")

# ============================================
# USAR CONTAINERS PARA ORDENAR
# ============================================
st.header("Ordenando con Containers")

# Crear containers
header_container = st.container()
body_container = st.container()
footer_container = st.container()

# Llenar en cualquier orden
with body_container:
    st.write("Cuerpo del documento")

with header_container:
    st.write("Encabezado (pero lo definimos después)")

with footer_container:
    st.write("Pie de página")

# ============================================
# CONTAINER CON BORDER
# ============================================
with st.container(border=True):
    st.subheader("Container con borde")
    st.write("Este container tiene un borde visible")
    st.button("Botón dentro del container")