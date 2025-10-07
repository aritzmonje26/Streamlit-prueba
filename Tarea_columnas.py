# ██╗██████╗ ██╗ ██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗██╗   ██╗███████╗
# ██║╚════██╗██║██╔═══██╗    ████╗  ██║╚██╗ ██╔╝╚██╗██╔╝╚██╗ ██╔╝██╔════╝
# ██║ █████╔╝██║██║   ██║    ██╔██╗ ██║ ╚████╔╝  ╚███╔╝  ╚████╔╝ ███████╗
# ██║ ╚═══██╗██║██║   ██║    ██║╚██╗██║  ╚██╔╝   ██╔██╗   ╚██╔╝  ╚════██║
# ██║██████╔╝██║╚██████╔╝    ██║ ╚████║   ██║   ██╔╝ ██╗   ██║   ███████║
# ╚═╝╚═════╝ ╚═╝ ╚═════╝     ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝
#              BIENVENIDO A LA INTERFAZ DE ANÁLISIS V9.7

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from streamlit_plotly_events import plotly_events
import time

# --- CONFIGURACIÓN DE PÁGINA: MODO PANTALLA COMPLETA ---
st.set_page_config(
    page_title="IRIS-NEXUS 9",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- EL NÚCLEO GRÁFICO: CSS DE CIENCIA FICCIÓN EXTREMA ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

/* --- Variables de Color de Neón --- */
:root {
    --glow-cyan: #00ffff;
    --glow-magenta: #ff00ff;
    --glow-green: #00ff00;
    --bg-dark: #020011;
    --glass-bg: rgba(20, 25, 80, 0.5);
    --glass-border: rgba(0, 255, 255, 0.2);
}

/* --- Animaciones Keyframes --- */
@keyframes flicker { 0%, 100% { opacity: 1; } 50% { opacity: 0.8; } }
@keyframes scanline {
    0% { background-position: 0 0; }
    100% { background-position: 0 100%; }
}
@keyframes text-glitch {
    2%, 64% { transform: translate(2px, -2px) skew(0deg); }
    4%, 60% { transform: translate(-2px, 2px) skew(0deg); }
    62% { transform: translate(0, 0) skew(5deg); }
}
@keyframes pulse-neon {
    0%, 100% { box-shadow: 0 0 5px 2px var(--glow-cyan), 0 0 10px 5px var(--glow-magenta); }
    50% { box-shadow: 0 0 10px 5px var(--glow-cyan), 0 0 20px 10px var(--glow-magenta); }
}

/* --- Estilo del Cuerpo (Body) --- */
body {
    background-color: var(--bg-dark);
    font-family: 'Orbitron', sans-serif;
    color: var(--glow-cyan);
}

/* --- Contenedor Principal con Efecto Scanline --- */
.main .block-container {
    background: var(--bg-dark);
    border-radius: 10px;
    border: 1px solid var(--glow-magenta);
    box-shadow: 0 0 20px var(--glow-magenta);
    position: relative;
    overflow: hidden;
}
.main .block-container::before {
    content: ' ';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(0deg, rgba(0, 255, 255, 0.05), rgba(0, 255, 255, 0.05) 1px, transparent 1px, transparent 4px);
    animation: scanline 2s linear infinite;
    pointer-events: none;
}

/* --- Título con Efecto Glitch --- */
h1 {
    font-weight: 900;
    animation: text-glitch 1s linear infinite;
    text-shadow: 0 0 10px var(--glow-cyan);
}

/* --- Barra Lateral de Cristal --- */
[data-testid="stSidebar"] {
    background: rgba(10, 5, 30, 0.7);
    backdrop-filter: blur(5px);
    border-right: 2px solid var(--glow-cyan);
}

/* --- Métricas Interactivas --- */
[data-testid="stMetric"] {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 10px;
    transition: all 0.3s ease-in-out;
}
[data-testid="stMetric"]:hover {
    transform: scale(1.05);
    border-color: var(--glow-cyan);
    box-shadow: 0 0 25px var(--glow-cyan);
}

/* --- Botones y Widgets de Neón --- */
.stButton>button, .stDownloadButton>button {
    border: 2px solid var(--glow-green);
    background: rgba(0, 255, 0, 0.1);
    color: var(--glow-green);
    border-radius: 10px;
    transition: all 0.3s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    box-shadow: 0 0 20px var(--glow-green);
    background: rgba(0, 255, 0, 0.3);
}
</style>
""", unsafe_allow_html=True)

# --- CARGA DE DATOS Y MODELO ---
@st.cache_data
def load_data():
    return sns.load_dataset('iris')

@st.cache_resource
def train_classifier(df):
    X = df[['sepal_length', 'sepal_width']]
    y = df['species']
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X, y)
    return model

df = load_data()
model = train_classifier(df)

# --- SIDEBAR: CONSOLA DE OPERACIONES ---
st.sidebar.markdown("<h1 style='text-align: center; font-size: 2rem; animation: none;'>IRIS-NEXUS 9</h1>", unsafe_allow_html=True)
st.sidebar.image("https://i.imgur.com/vI4fA2b.gif")

with st.sidebar:
    st.header("🧬 Filtros Genómicos")
    species = st.multiselect("Filtrar por Linaje:", df["species"].unique(), df["species"].unique())
    
    st.header("📏 Calibradores Biométricos")
    sepal_len = st.slider("Rango Sépalo (L)", float(df["sepal_length"].min()), float(df["sepal_length"].max()), (3.0, 8.0))
    petal_len = st.slider("Rango Pétalo (L)", float(df["petal_length"].min()), float(df["petal_length"].max()), (1.0, 7.0))
    
    st.header("⚙️ Config. de Sistema")
    if st.button("🔄 Resetear Filtros"):
        st.session_state.clear()
        st.toast("✅ ¡Sistema reseteado a parámetros de fábrica!", icon="⚙️")
        time.sleep(1); st.rerun()

    st.markdown("---")
    st.markdown(f"<p style='text-align:center; color: var(--glow-green)'>STATUS: ONLINE ✅</p>", unsafe_allow_html=True)

# --- LÓGICA DE FILTRADO ---
df_filtered = df[
    (df["species"].isin(species)) &
    (df["sepal_length"].between(sepal_len[0], sepal_len[1])) &
    (df["petal_length"].between(petal_len[0], petal_len[1]))
]
if df_filtered.empty:
    st.error("❌ ERROR CRÍTICO: No se encontraron bio-firmas. Reajuste los parámetros."); st.stop()

# --- INTERFAZ PRINCIPAL ---
st.title("IRIS-NEXUS 9")
st.markdown("### 📈 Interfaz de Análisis de Datos Biométricos Cuánticos")

# --- PESTAÑAS ---
tab_list = ["**📡 Dashboard**", "**📊 Análisis de Distribución**", "**🤖 Simulador Predictivo**", "**⚛️ Matriz de Correlación**", "**💾 Data-Stream**"]
tabs = st.tabs(tab_list)

with tabs[0]: # Dashboard
    st.header("🛰️ Telemetría en Tiempo Real")
    m1, m2, m3, m4 = st.columns(4)
    avg_sepal_len = df['sepal_length'].mean()
    avg_petal_len = df['petal_length'].mean()
    
    m1.metric("Bio-Firmas Activas", len(df_filtered), f"{len(df_filtered) - len(df)} Total")
    m2.metric("Linajes Detectados", df_filtered['species'].nunique(), f"{df_filtered['species'].nunique() - df['species'].nunique()} vs Total")
    m3.metric("Sépalo Prom. (cm)", f"{df_filtered['sepal_length'].mean():.2f}", f"{df_filtered['sepal_length'].mean() - avg_sepal_len:.2f} vs Global")
    m4.metric("Pétalo Prom. (cm)", f"{df_filtered['petal_length'].mean():.2f}", f"{df_filtered['petal_length'].mean() - avg_petal_len:.2f} vs Global")
    
    st.markdown("---")
    st.header("🗺️ Mapa de Dispersión de Sépalo")
    fig_scatter = px.scatter(df_filtered, x="sepal_length", y="sepal_width", color="species", size='petal_length',
                             color_discrete_sequence=px.colors.qualitative.Vivid)
    fig_scatter.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white", legend_title_text='')
    st.plotly_chart(fig_scatter, use_container_width=True)

with tabs[1]: # Análisis de Distribución
    st.header("🔬 Análisis de Distribución por Característica")
    feature = st.selectbox("Seleccionar Característica Biométrica:", ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Histograma de Frecuencia")
        fig_hist = px.histogram(df_filtered, x=feature, color="species", marginal="box",
                                color_discrete_sequence=px.colors.qualitative.Prism)
        fig_hist.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig_hist, use_container_width=True)
    with c2:
        st.subheader("Diagrama de Violín")
        fig_violin = px.violin(df_filtered, y=feature, x="species", color="species",
                               color_discrete_sequence=px.colors.qualitative.G10)
        fig_violin.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig_violin, use_container_width=True)
        
with tabs[2]: # Simulador Predictivo
    st.header("🤖 Simulador de Clasificación Neuronal")
    st.info("Haz clic en el gráfico para simular una nueva bio-firma y predecir su linaje.", icon="💡")
    
    c1, c2 = st.columns([2,1])
    with c1:
        plot_fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species")
        plot_fig.update_layout(plot_bgcolor='rgba(0,0,0,0.5)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        selected_points = plotly_events(plot_fig, click_event=True)

    with c2:
        st.subheader("Resultados de la Simulación")
        if selected_points:
            point = selected_points[0]
            new_x, new_y = point['x'], point['y']
            
            with st.spinner("Quantum CPU calculando..."):
                time.sleep(1)
                new_point = np.array([[new_x, new_y]])
                prediction = model.predict(new_point)
                prediction_proba = model.predict_proba(new_point)
            
            st.success(f"**Linaje Predicho:** {prediction[0]}")
            st.write("**Probabilidades:**")
            st.dataframe(pd.DataFrame(prediction_proba, columns=model.classes_, index=["Prob."]))
            
            st.write(f"**Coordenadas de la muestra:** ({new_x:.2f}, {new_y:.2f})")
            st.image("https://i.imgur.com/krBaA28.png") # ASCII art of a flower
        else:
            st.write("Esperando coordenadas del usuario...")

with tabs[3]: # Matriz de Correlación
    st.header("⚛️ Matriz de Correlación de Quarks Biológicos")
    corr_matrix = df_filtered.select_dtypes(include=np.number).corr()
    
    fig_corr = go.Figure(data=go.Heatmap(
                   z=corr_matrix.values,
                   x=corr_matrix.columns,
                   y=corr_matrix.columns,
                   colorscale='Cividis',
                   colorbar=dict(title="Nivel de Correlación", tickfont=dict(color="white"))))
    fig_corr.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_corr, use_container_width=True)

with tabs[4]: # Data-Stream
    st.header("💾 Data-Stream Crudo")
    st.dataframe(df_filtered)

    @st.cache_data
    def convert_df_to_csv(df_to_convert):
        return df_to_convert.to_csv(index=False).encode('utf-8')
    csv = convert_df_to_csv(df_filtered)
    st.download_button("📲 Descargar Data-Packet", csv, "iris_nexus9_data.csv", "text/csv")