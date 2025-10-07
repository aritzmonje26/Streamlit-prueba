import streamlit as st
import pandas as pd
import numpy as np

st.title("Ejercicio 1: Mi primera aplicación web con Streamlit")  # "El comando st.title() crea un título grande en la parte superior de la app


datos = pd.DataFrame(
	np.random.randn(20, 3), #20 filas y 3 columnas , valores entre -1 y 1
	columns = ['a', 'b', 'c'])
st.write("Este es un ejemplo de una tabla interactiva")
st.table(datos)  #Tabla interactiva con scroll, Muestra los datos en formato tabla.
st.line_chart(datos)  #Gráfico de líneas
st.dataframe(datos)  #Tabla interactiva con scroll, Muestra los datos en formato tabla. 




st.error("Este es un mensaje de error 💣")
st.warning("Cuidado, esta acción no se puede deshacer ⚠️")
st.info("Información: La base de datos se actualiza cada 24 horas ℹ️")
st.success("¡El proceso ha finalizado con éxito! 🎉")

if st.button('Lánzame unos globos'):
    st.balloons() # ¡Una de las funciones más divertidas!
    
opcion = st.selectbox(
    '¿Cuál es tu película favorita de Studio Ghibli?',
    ('El viaje de Chihiro', 'Mi vecino Totoro', 'La princesa Mononoke')
)
st.write('Tu película favorita es:', opcion)

edad = st.slider('¿Cuántos años tienes?', 0, 130, 25) # min, max, valor por defecto
st.write("Tengo ", edad, ' años.')

nombre = st.text_input('Escribe tu nombre', 'Gandalf')
st.write(f'¡Hola, {nombre}!')

# Usando el DataFrame 'datos' de tu ejemplo
if st.checkbox('Mostrar gráfico de líneas'):
    st.line_chart(datos)
    
	# Este slider aparecerá en la barra lateral
valor_sidebar = st.sidebar.slider('Selecciona un valor en la barra lateral', 0, 100)

# Y este texto aparecerá en la página principal
st.write("El valor seleccionado en la barra lateral es:", valor_sidebar)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Un gato")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Un perro")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Un búho")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    
tab1, tab2 = st.tabs(["📈 Gráfico", "🗃️ Datos"])

with tab1:
    st.header("Un gráfico de área")
    st.area_chart(datos)

with tab2:
    st.header("Los datos del DataFrame")
    st.dataframe(datos)
    
with st.expander("Haz clic aquí para ver los datos crudos"):
    st.write("Aquí están los datos de la tabla que generaste al principio:")
    st.dataframe(datos)
    
"Mostrando el DataFrame con 'magia':" # Esto funciona como st.write()
datos # Esto funciona como st.dataframe(datos)

@st.cache_data # Este es el "decorador" mágico
def cargar_datos_pesados(url):
    # Esta función simula una carga lenta
    df = pd.read_csv(url)
    return df

# La primera vez tardará en cargar, pero las siguientes será instantáneo
datos_csv = cargar_datos_pesados("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
st.dataframe(datos_csv)


import time

with st.spinner('Calculando algo complejo...'):
    time.sleep(3) # Simula un proceso largo
st.success('¡Terminado!')