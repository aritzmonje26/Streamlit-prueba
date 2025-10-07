# ==============================================================================
# 1. IMPORTACIONES GLOBALES
# Todas las librerías necesarias para todas las secciones de la aplicación.
# ==============================================================================
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pydeck as pdk

# ==============================================================================
# 2. CONFIGURACIÓN DE LA PÁGINA
# Debe ser el primer comando de Streamlit.
# ==============================================================================
st.set_page_config(
    page_title="Global Data-Verse Explorer",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 3. FUNCIONES DE CACHÉ
# Funciones que cargan datos o entrenan modelos. Se cachean para mejorar
# el rendimiento de la aplicación.
# ==============================================================================

@st.cache_data
def cargar_grimorio_antiguo(url):
    """Carga un CSV desde una URL y lo guarda en cache."""
    df = pd.read_csv(url)
    return df

@st.cache_data
def load_penguins():
    """Carga el dataset de pingüinos y lo limpia."""
    url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
    df = pd.read_csv(url).dropna()
    return df

@st.cache_data
def load_geo_data():
    """Carga datos de terremotos de USGS."""
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv"
    df = pd.read_csv(url)
    df = df[['time', 'latitude', 'longitude', 'depth', 'mag']]
    df.rename(columns={'latitude': 'lat', 'longitude': 'lon'}, inplace=True)
    return df

@st.cache_resource
def train_model(X_train, y_train, n_est, m_depth, min_samples):
    """Entrena un modelo RandomForestClassifier y lo guarda en cache."""
    model = RandomForestClassifier(n_estimators=n_est, max_depth=m_depth, 
                                   min_samples_leaf=min_samples, random_state=42)
    model.fit(X_train, y_train)
    return model

# ==============================================================================
# 4. BARRA LATERAL Y NAVEGACIÓN
# Usamos un radio button para simular la navegación entre páginas.
# ==============================================================================
st.sidebar.title("🚀 Navegación")
page = st.sidebar.radio("Elige un módulo:", 
                        ["🏠 Página Principal", 
                         "📈 Explorador Interactivo", 
                         "🤖 Playground Machine Learning", 
                         "🌍 Visualizador Geoespacial", 
                         "⚙️ Componentes Avanzados"])

st.sidebar.markdown("---")

# ==============================================================================
# 5. CONTENIDO DE LAS PÁGINAS
# Un bloque if/elif/else para mostrar el contenido de la página seleccionada.
# ==============================================================================

# ---------------------------------
# PÁGINA 1: PÁGINA PRINCIPAL
# ---------------------------------
if page == "🏠 Página Principal":
    st.title("🌌 Global Data-Verse Explorer")
    st.markdown("### ¡Bienvenido al nexo de datos del universo! Explora, visualiza y predice.")
    st.markdown("---")

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.image("https://i.imgur.com/8NfA3Kk.gif", caption="Navegando a través de los datos estelares")
        st.info("Utiliza el menú de la izquierda para navegar entre los diferentes módulos del explorador.")

    with col2:
        st.header("¿Qué puedes hacer aquí?")
        st.markdown("""
        Este es tu centro de comando para el análisis de datos. Hemos reunido un conjunto de herramientas poderosas para que puedas:

        - **📊 Explorar Datos Interactivamente:** Sube tus propios conjuntos de datos y desentraña sus secretos con gráficos dinámicos.
        - **🤖 Entrenar Modelos de Machine Learning:** Experimenta con modelos de clasificación en tiempo real y ajusta sus hiperparámetros.
        - **🌍 Visualizar Información Geoespacial:** Viaja por el mundo a través de mapas 3D interactivos que dan vida a los datos de ubicación.
        - **⚙️ Descubrir Componentes Avanzados:** Observa una demostración de algunos de los widgets y elementos de diseño más sofisticados de Streamlit.
        """)

    st.markdown("---")
    st.header("Estado Actual del Data-Verse")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Conjuntos de Datos Analizados", value="1,337", delta="12%")
    m2.metric(label="Modelos Entrenados Hoy", value="42", delta="5")
    m3.metric(label="Visualizaciones Generadas", value="2.1M", delta="2.5%")
    m4.metric(label="Anomalías Cósmicas Detectadas", value="3", delta="-1", delta_color="inverse")

    with st.expander("Haz clic para conocer la filosofía detrás de este proyecto"):
        st.write("""
        Creemos que el acceso a los datos y la capacidad de analizarlos no debería estar restringido a unos pocos elegidos. 
        Esta herramienta fue construida con la filosofía de la democratización de datos, utilizando el poder y la simplicidad 
        de Streamlit para crear una experiencia intuitiva y potente. ¡Explora, aprende y crea!
        """)

# ---------------------------------
# PÁGINA 2: EXPLORADOR INTERACTIVO
# ---------------------------------
elif page == "📈 Explorador Interactivo":
    st.title("📈 Explorador de Datos Interactivo")
    st.markdown("Sube tu propio archivo CSV y comienza a explorar tus datos como nunca antes.")

    uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

    if uploaded_file is not None:
        st.session_state.df = pd.read_csv(uploaded_file)
    
    if 'df' in st.session_state:
        df = st.session_state.df

        st.header("Vista Previa y Estadísticas Descriptivas")
        if st.checkbox("Mostrar vista previa de los datos"):
            st.dataframe(df.head())
        if st.checkbox("Mostrar estadísticas descriptivas"):
            st.write(df.describe())

        st.header("Constructor de Gráficos Dinámicos")
        st.markdown("Selecciona las columnas para crear gráficos sobre la marcha.")

        col1, col2, col3 = st.columns(3)
        with col1:
            plot_type = st.selectbox("Elige el tipo de gráfico", ["Dispersión (Scatter)", "Líneas", "Barras", "Histograma", "Caja (Boxplot)"])
        with col2:
            numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
            categorical_columns = df.select_dtypes(include='object').columns.tolist()
            x_axis = st.selectbox("Elige la columna para el eje X", df.columns)
        with col3:
            y_axis = st.selectbox("Elige la columna para el eje Y", numeric_columns if plot_type not in ["Histograma"] else [None])

        try:
            if plot_type == "Dispersión (Scatter)":
                color_encoding = st.selectbox("Codificar por color (opcional)", [None] + categorical_columns + numeric_columns)
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{plot_type}: {x_axis} vs {y_axis}", color=color_encoding)
            elif plot_type == "Líneas":
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{plot_type}: {x_axis} vs {y_axis}")
            elif plot_type == "Barras":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{plot_type}: {x_axis} vs {y_axis}")
            elif plot_type == "Histograma":
                fig = px.histogram(df, x=x_axis, title=f"Histograma de {x_axis}")
            elif plot_type == "Caja (Boxplot)":
                fig = px.box(df, x=x_axis, y=y_axis, title=f"{plot_type}: {x_axis} vs {y_axis}")
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"No se pudo generar el gráfico. Error: {e}")
    else:
        st.warning("Por favor, sube un archivo CSV para comenzar.")

# ---------------------------------
# PÁGINA 3: PLAYGROUND ML
# ---------------------------------
elif page == "🤖 Playground Machine Learning":
    st.title("🤖 Playground de Machine Learning: Clasificador de Pingüinos")
    st.markdown("Entrena un modelo para clasificar especies de pingüinos y haz predicciones en tiempo real.")

    penguins_df = load_penguins()
    X = penguins_df.drop('species', axis=1)
    X = pd.get_dummies(X)
    y = penguins_df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    st.sidebar.header("Ajuste de Hiperparámetros")
    n_estimators = st.sidebar.slider("Número de árboles", 10, 500, 100)
    max_depth = st.sidebar.slider("Profundidad máxima", 2, 20, 5)
    min_samples_leaf = st.sidebar.slider("Muestras mínimas por hoja", 1, 10, 2)

    model = train_model(X_train, y_train, n_estimators, max_depth, min_samples_leaf)

    st.header("Evaluación del Modelo")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.metric("Precisión (Accuracy) del Modelo", f"{accuracy:.2%}")

    st.subheader("Matriz de Confusión")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
    plt.xlabel('Predicho')
    plt.ylabel('Verdadero')
    st.pyplot(fig)

    st.header("Haz una Predicción en Tiempo Real")
    col1, col2, col3 = st.columns(3)
    with col1:
        bill_length = st.slider("Longitud del pico (mm)", float(X['bill_length_mm'].min()), float(X['bill_length_mm'].max()), float(X['bill_length_mm'].mean()))
        bill_depth = st.slider("Profundidad del pico (mm)", float(X['bill_depth_mm'].min()), float(X['bill_depth_mm'].max()), float(X['bill_depth_mm'].mean()))
    with col2:
        flipper_length = st.slider("Longitud de la aleta (mm)", float(X['flipper_length_mm'].min()), float(X['flipper_length_mm'].max()), float(X['flipper_length_mm'].mean()))
        body_mass = st.slider("Masa corporal (g)", float(X['body_mass_g'].min()), float(X['body_mass_g'].max()), float(X['body_mass_g'].mean()))
    with col3:
        island = st.selectbox("Isla", options=penguins_df['island'].unique())
        sex = st.selectbox("Sexo", options=penguins_df['sex'].unique())

    island_Torgersen = 1 if island == 'Torgersen' else 0
    island_Dream = 1 if island == 'Dream' else 0
    sex_male = 1 if sex == 'male' else 0
    
    prediction_df = pd.DataFrame([[bill_length, bill_depth, flipper_length, body_mass, island_Dream, island_Torgersen, sex_male]],
                              columns=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'island_Dream', 'island_Torgersen', 'sex_male'])

    prediction = model.predict(prediction_df)
    prediction_proba = model.predict_proba(prediction_df)

    st.subheader("Resultado de la Predicción:")
    st.success(f"La especie predicha es: **{prediction[0]}**")
    st.write("Probabilidades:")
    st.write(pd.DataFrame(prediction_proba, columns=model.classes_, index=["Probabilidad"]))

# ---------------------------------
# PÁGINA 4: VISUALIZADOR GEOESPACIAL
# ---------------------------------
elif page == "🌍 Visualizador Geoespacial":
    st.title("🌍 Visualizador Geoespacial 3D")
    st.markdown("Explora datos de terremotos en un globo terráqueo interactivo.")

    earthquake_df = load_geo_data()

    st.sidebar.header("Filtros del Mapa")
    min_mag = st.sidebar.slider("Filtrar por magnitud mínima", 2.5, 8.0, 4.5)
    filtered_df = earthquake_df[earthquake_df['mag'] >= min_mag]

    st.header(f"Mostrando {len(filtered_df)} terremotos con magnitud >= {min_mag}")

    layer = pdk.Layer(
        'HexagonLayer', data=filtered_df, get_position='[lon, lat]', radius=100000,
        elevation_scale=4000, elevation_range=[0, 100000], pickable=True, extruded=True,
    )
    view_state = pdk.ViewState(longitude=-100, latitude=40, zoom=2, pitch=50)

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "Magnitud: {mag}\nProfundidad: {depth} km"}
    ))
    st.caption("La altura de las barras representa la concentración y magnitud de los terremotos.")

# ---------------------------------
# PÁGINA 5: COMPONENTES AVANZADOS
# ---------------------------------
elif page == "⚙️ Componentes Avanzados":
    st.title("⚙️ Escaparate de Componentes Avanzados")
    st.markdown("Una demostración de otros widgets, contenedores y funcionalidades.")

    st.header("Formularios para agrupar inputs")
    with st.form("mi_formulario"):
        st.write("Dentro del formulario")
        slider_val = st.slider("Valor")
        checkbox_val = st.checkbox("Checkbox")
        submitted = st.form_submit_button("Enviar")
        if submitted:
            st.success(f"Formulario enviado con valor {slider_val} y checkbox {checkbox_val}")

    st.header("Manejo de Audio y Video")
    col1, col2 = st.columns(2)
    with col1:
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    with col2:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    st.header("Contenedores y Elementos Dinámicos")
    placeholder = st.empty()
    with placeholder.container():
        st.write("¡Iniciando secuencia de lanzamiento! 🚀")
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.02)
    placeholder.success("¡Despegue completado!")

    st.header("Comandos Mágicos")
    "**Este texto se muestra con magia:**"
    df_magico = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    df_magico