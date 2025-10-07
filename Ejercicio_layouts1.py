import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import time

st.set_page_config(page_title="Dashboard Pro Pingüinos", layout="wide")

# ========================================
# CARGAR DATOS BASE
# ========================================
df_base = sns.load_dataset('penguins').dropna()

# Esquema esperado
EXPECTED_COLS = {
    'species', 'island', 'sex',
    'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'
}

# ========================================
# SIDEBAR
# ========================================
with st.sidebar:
    st.title(" Panel de Control")

    # Nombre usuario
    nombre = st.text_input("Tu nombre:", value="Investigador")

    st.write("---")

    # File uploader
    archivo = st.file_uploader("Sube tu CSV (opcional):", type=['csv'])
    df = df_base.copy()

    if archivo:
        try:
            df_up = pd.read_csv(archivo)
            # Validar columnas mínimas
            missing = EXPECTED_COLS - set(df_up.columns)
            if missing:
                st.error(
                    "⚠️ El CSV no tiene las columnas requeridas para este dashboard.\n\n"
                    f"Faltan: {sorted(list(missing))}\n\n"
                    "Se usará el dataset por defecto."
                )
            else:
                df = df_up.dropna(subset=list(EXPECTED_COLS))
                st.success("CSV personalizado cargado y validado")
        except Exception as e:
            st.error(f"Error leyendo CSV: {e}. Se usará el dataset por defecto.")

    st.write("---")

    # Filtros (siempre sobre df actual)
    st.subheader("Filtros")

    especies = st.multiselect(
        "Especies:",
        options=sorted(df['species'].dropna().unique()),
        default=list(sorted(df['species'].dropna().unique()))
    )

    islas = st.multiselect(
        "Islas:",
        options=sorted(df['island'].dropna().unique()),
        default=list(sorted(df['island'].dropna().unique()))
    )

    sexo = st.radio(
        "Sexo:",
        options=['Todos', 'Male', 'Female'],
        horizontal=True
    )

    # Guardas límites seguros por si el CSV viene raro
    bm_min = int(df['body_mass_g'].min())
    bm_max = int(df['body_mass_g'].max())

    peso_min, peso_max = st.slider(
        "Peso corporal (g):",
        min_value=bm_min,
        max_value=bm_max,
        value=(bm_min, bm_max)
    )

# ========================================
# APLICAR FILTROS
# ========================================
df_filtrado = df[
    (df['species'].isin(especies)) &
    (df['island'].isin(islas)) &
    (df['body_mass_g'].between(peso_min, peso_max))
]

if sexo != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['sex'] == sexo]

# ========================================
# ÁREA PRINCIPAL
# ========================================

# Mensaje de bienvenida temporal
placeholder = st.empty()
with placeholder.container():
    st.info(f" ¡Bienvenido/a {nombre}! Cargando dashboard...")
    time.sleep(1.5)
placeholder.empty()

# Título
st.title(f" Dashboard de Pingüinos - {nombre}")
st.markdown("*Análisis del dataset Palmer Penguins*")

# Si no hay datos tras filtros, avisa y para
if df_filtrado.empty:
    st.warning("No hay datos para los filtros seleccionados. Ajusta los filtros en el panel lateral.")
    st.stop()

# ========================================
# MÉTRICAS EN COLUMNAS
# ========================================
col1, col2, col3, col4 = st.columns(4)

total_actual = len(df_filtrado)
total_base = len(df)
delta_val = total_actual - total_base

with col1:
    st.metric(
        label=" Total Pingüinos (subset)",
        value=total_actual,
        delta=delta_val  # numérico; positivo/negativo
    )
    st.caption(f"Total dataset actual: {total_base}")

with col2:
    st.metric(
        label=" Islas (distintas)",
        value=int(df_filtrado['island'].nunique())
    )

with col3:
    peso_promedio = df_filtrado['body_mass_g'].mean()
    st.metric(
        label="⚖️ Peso Promedio",
        value=f"{peso_promedio:.0f} g"
    )

with col4:
    st.metric(
        label="📏 Longitud Pico Media",
        value=f"{df_filtrado['bill_length_mm'].mean():.1f} mm"
    )

st.write("---")

# ========================================
# TABS
# ========================================
tab1, tab2, tab3 = st.tabs([" Datos", " Gráficos", " Estadísticas"])

with tab1:
    st.subheader("Datos Filtrados")
    st.dataframe(df_filtrado, use_container_width=True, height=400)

    # Botón descarga
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Descargar CSV filtrado",
        data=csv,
        file_name=f"pinguinos_filtrados_{nombre}.csv",
        mime="text/csv"
    )

with tab2:
    st.subheader("Visualizaciones")

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown("**Dispersión: Longitud vs Profundidad Pico**")
        fig1 = px.scatter(
            df_filtrado,
            x='bill_length_mm',
            y='bill_depth_mm',
            color='species',
            size='body_mass_g',
            hover_data=['island', 'sex'],
            title="bill_length_mm vs bill_depth_mm"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col_g2:
        st.markdown("**Distribución de Peso por Especie**")
        fig2 = px.box(
            df_filtrado,
            x='species',
            y='body_mass_g',
            color='species',
            title="Body mass (g) por especie"
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("**Relación entre todas las medidas**")
    fig3 = px.scatter_matrix(
        df_filtrado,
        dimensions=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
        color='species',
        title="Matriz de dispersión"
    )
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.subheader("Estadísticas Descriptivas")

    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("**Estadísticas Numéricas**")
        st.dataframe(df_filtrado.describe(), use_container_width=True)

    with col_s2:
        st.markdown("**Conteo por Categorías**")
        c1, c2, c3 = st.columns(3)
        c1.write("**Especie**")
        c1.write(df_filtrado['species'].value_counts())
        c2.write("**Isla**")
        c2.write(df_filtrado['island'].value_counts())
        c3.write("**Sexo**")
        c3.write(df_filtrado['sex'].value_counts())

# ========================================
# EXPANDERS
# ========================================
st.write("---")

with st.expander("ℹ️ Información sobre el Dataset"):
    st.markdown("""
    ### 🐧 Palmer Penguins Dataset

    Medidas de 3 especies de pingüinos del Archipiélago Palmer, Antártida.
    """)

with st.expander(" Opciones Avanzadas"):
    st.markdown("**Configuración del análisis:**")

    mostrar_nulos = st.checkbox("Mostrar información de valores nulos (dataset actual)")
    if mostrar_nulos:
        st.write(df.isnull().sum())

    mostrar_correlacion = st.checkbox("Mostrar matriz de correlación (subset)")
    if mostrar_correlacion:
        numcols = df_filtrado.select_dtypes(include=['float64', 'int64'])
        if numcols.shape[1] >= 2:
            st.dataframe(numcols.corr(), use_container_width=True)
        else:
            st.info("No hay suficientes columnas numéricas para correlación.")

# ========================================
# FOOTER
# ========================================
st.write("---")
st.caption(f"Dashboard creado por {nombre} | Datos: Palmer Penguins Dataset")
