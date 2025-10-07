import streamlit as st
import pandas as pd
from datetime import datetime, date, time

st.title("🎮 Cheat Sheet - Widgets de Entrada")

# ========================================
# 1. CHECKBOX
# ========================================
st.header("1️⃣ Checkbox")
st.caption("Retorna: True o False")

aceptar = st.checkbox("Acepto los términos y condiciones")
mostrar_datos = st.checkbox("Mostrar datos", value=True)  # Activado por defecto

if aceptar:
    st.success("✅ Términos aceptados")
if mostrar_datos:
    st.write("Aquí están los datos...")

st.write(f"Valor de aceptar: `{aceptar}`")
st.write(f"Valor de mostrar_datos: `{mostrar_datos}`")

st.write("---")

# ========================================
# 2. RADIO
# ========================================
st.header("2️⃣ Radio Buttons")
st.caption("Retorna: El valor seleccionado")

# Vertical (por defecto)
genero = st.radio(
    "Selecciona tu género:",
    options=["Masculino", "Femenino", "Otro", "Prefiero no decir"]
)

# Horizontal
nivel = st.radio(
    "Nivel de experiencia:",
    options=["Principiante", "Intermedio", "Avanzado"],
    horizontal=True
)

st.write(f"Género: `{genero}`")
st.write(f"Nivel: `{nivel}`")

st.write("---")

# ========================================
# 3. SELECTBOX
# ========================================
st.header("3️⃣ Select Box (Desplegable)")
st.caption("Retorna: El valor seleccionado")

ciudad = st.selectbox(
    "Elige tu ciudad:",
    options=["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
)

# Con índice por defecto
pais = st.selectbox(
    "Elige tu país:",
    options=["España", "Francia", "Alemania", "Italia"],
    index=0  # España por defecto
)

st.write(f"Ciudad: `{ciudad}`")
st.write(f"País: `{pais}`")

st.write("---")

# ========================================
# 4. MULTISELECT
# ========================================
st.header("4️⃣ Multi Select")
st.caption("Retorna: Lista con las opciones seleccionadas")

# Sin valores por defecto
hobbies = st.multiselect(
    "Selecciona tus hobbies:",
    options=["Leer", "Deporte", "Música", "Viajar", "Cocinar", "Programar"]
)

# Con valores por defecto
idiomas = st.multiselect(
    "Idiomas que hablas:",
    options=["Español", "Inglés", "Francés", "Alemán", "Italiano"],
    default=["Español"]  # Español seleccionado por defecto
)

st.write(f"Hobbies: `{hobbies}` (tipo: {type(hobbies)})")
st.write(f"Idiomas: `{idiomas}`")

st.write("---")

# ========================================
# 5. SLIDER (Numérico)
# ========================================
st.header("5️⃣ Slider")
st.caption("Retorna: int, float o tupla (min, max)")

# Slider simple
edad = st.slider(
    "Tu edad:",
    min_value=0,
    max_value=100,
    value=25,  # Valor por defecto
    step=1
)

# Slider de rango (devuelve tupla)
rango_precio = st.slider(
    "Rango de precio (€):",
    min_value=0,
    max_value=1000,
    value=(100, 500),  # Rango por defecto
    step=10
)

# Slider decimal
temperatura = st.slider(
    "Temperatura (°C):",
    min_value=-10.0,
    max_value=40.0,
    value=20.0,
    step=0.5
)

st.write(f"Edad: `{edad}` (tipo: {type(edad)})")
st.write(f"Rango precio: `{rango_precio}` (tipo: {type(rango_precio)})")
st.write(f"Temperatura: `{temperatura}` (tipo: {type(temperatura)})")

st.write("---")

# ========================================
# 6. SELECT_SLIDER
# ========================================
st.header("6️⃣ Select Slider")
st.caption("Retorna: El valor seleccionado (puede ser string, número, etc)")

# Con strings
talla = st.select_slider(
    "Selecciona tu talla:",
    options=["XS", "S", "M", "L", "XL", "XXL"],
    value="M"
)

# Con números
calificacion = st.select_slider(
    "Califica del 1 al 5:",
    options=[1, 2, 3, 4, 5],
    value=3
)

# Rango con select_slider
rango_meses = st.select_slider(
    "Rango de meses:",
    options=["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
    value=("Ene", "Dic")  # Rango completo por defecto
)

st.write(f"Talla: `{talla}`")
st.write(f"Calificación: `{calificacion}`")
st.write(f"Rango meses: `{rango_meses}`")

st.write("---")

# ========================================
# 7. NUMBER_INPUT
# ========================================
st.header("7️⃣ Number Input")
st.caption("Retorna: int o float")

# Entero
cantidad = st.number_input(
    "Cantidad de productos:",
    min_value=0,
    max_value=100,
    value=1,
    step=1
)

# Decimal
precio = st.number_input(
    "Precio (€):",
    min_value=0.0,
    max_value=10000.0,
    value=9.99,
    step=0.01,
    format="%.2f"  # Formato con 2 decimales
)

st.write(f"Cantidad: `{cantidad}` (tipo: {type(cantidad)})")
st.write(f"Precio: `{precio}` (tipo: {type(precio)})")

st.write("---")

# ========================================
# 8. TEXT_INPUT
# ========================================
st.header("8️⃣ Text Input")
st.caption("Retorna: String")

# Simple
nombre = st.text_input(
    "Tu nombre:",
    value="",
    placeholder="Ej: María García"
)

# Con valor por defecto
email = st.text_input(
    "Tu email:",
    value="usuario@ejemplo.com",
    help="Introduce un email válido"
)

# Para contraseñas
password = st.text_input(
    "Contraseña:",
    type="password"
)

st.write(f"Nombre: `{nombre}` (longitud: {len(nombre)})")
st.write(f"Email: `{email}`")
st.write(f"Password: `{'*' * len(password)}` (no mostrar nunca la contraseña real)")

st.write("---")

# ========================================
# 9. TEXT_AREA
# ========================================
st.header("9️⃣ Text Area")
st.caption("Retorna: String (multilinea)")

comentarios = st.text_area(
    "Tus comentarios:",
    value="",
    placeholder="Escribe aquí tus comentarios...",
    height=150,
    max_chars=500  # Límite de caracteres
)

st.write(f"Comentarios: `{comentarios}`")
st.write(f"Caracteres: {len(comentarios)}/500")

st.write("---")

# ========================================
# 10. DATE_INPUT
# ========================================
st.header("🔟 Date Input")
st.caption("Retorna: datetime.date o tupla de fechas")

# Fecha simple
fecha_nacimiento = st.date_input(
    "Fecha de nacimiento:",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# Rango de fechas
rango_fechas = st.date_input(
    "Rango de fechas:",
    value=(date(2024, 1, 1), date(2024, 12, 31)),
    min_value=date(2020, 1, 1),
    max_value=date(2030, 12, 31)
)

st.write(f"Fecha nacimiento: `{fecha_nacimiento}` (tipo: {type(fecha_nacimiento)})")
st.write(f"Rango: `{rango_fechas}` (tipo: {type(rango_fechas)})")

st.write("---")

# ========================================
# 11. TIME_INPUT
# ========================================
st.header("1️⃣1️⃣ Time Input")
st.caption("Retorna: datetime.time")

hora_reunion = st.time_input(
    "Hora de la reunión:",
    value=time(14, 30)
)

st.write(f"Hora: `{hora_reunion}` (tipo: {type(hora_reunion)})")

st.write("---")

# ========================================
# 12. FILE_UPLOADER
# ========================================
st.header("1️⃣2️⃣ File Uploader")
st.caption("Retorna: Objeto archivo o None")

# Un solo archivo
archivo = st.file_uploader(
    "Sube un archivo CSV:",
    type=['csv', 'txt', 'xlsx']
)

if archivo is not None:
    st.success(f"✅ Archivo cargado: {archivo.name}")
    st.write(f"Tipo: {archivo.type}")
    st.write(f"Tamaño: {archivo.size} bytes")
    
    # Si es CSV, leerlo
    if archivo.name.endswith('.csv'):
        df = pd.read_csv(archivo)
        st.dataframe(df.head())

# Múltiples archivos
archivos = st.file_uploader(
    "Sube múltiples imágenes:",
    type=['jpg', 'png', 'jpeg'],
    accept_multiple_files=True
)

if archivos:
    st.write(f"Has subido {len(archivos)} archivo(s)")
    for archivo in archivos:
        st.write(f"- {archivo.name}")

st.write("---")

# ========================================
# 13. COLOR_PICKER
# ========================================
st.header("1️⃣3️⃣ Color Picker")
st.caption("Retorna: String (código hexadecimal)")

color = st.color_picker(
    "Elige un color:",
    value="#FF5733"
)

st.write(f"Color seleccionado: `{color}`")

# Mostrar el color
st.markdown(f"""
<div style="background-color: {color}; padding: 20px; border-radius: 10px; color: white; text-align: center;">
    <h3>Este es el color seleccionado</h3>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ========================================
# 14. TOGGLE (Nuevo en versiones recientes)
# ========================================
st.header("1️⃣4️⃣ Toggle")
st.caption("Retorna: True o False")

modo_oscuro = st.toggle("🌙 Modo oscuro", value=False)
notificaciones = st.toggle("🔔 Activar notificaciones", value=True)

st.write(f"Modo oscuro: `{modo_oscuro}`")
st.write(f"Notificaciones: `{notificaciones}`")

st.write("---")

# ========================================
# 15. BUTTON
# ========================================
st.header("1️⃣5️⃣ Button")
st.caption("Retorna: True solo cuando se pulsa")

if st.button("🚀 Ejecutar"):
    st.success("¡Botón pulsado!")
    st.snow()

# Button con tipo
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Confirmar", type="primary"):
        st.success("Confirmado")

with col2:
    if st.button("❌ Cancelar"):
        st.error("Cancelado")

st.write("---")

# ========================================
# 16. DOWNLOAD_BUTTON
# ========================================
st.header("1️⃣6️⃣ Download Button")
st.caption("Retorna: True cuando se pulsa, pero descarga el archivo")

# Crear datos de ejemplo
df_ejemplo = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'María'],
    'Edad': [25, 30, 28]
})

csv = df_ejemplo.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Descargar CSV",
    data=csv,
    file_name="datos.csv",
    mime="text/csv"
)

# Texto
texto = "Este es un archivo de texto de ejemplo"
st.download_button(
    label="📄 Descargar TXT",
    data=texto,
    file_name="ejemplo.txt",
    mime="text/plain"
)