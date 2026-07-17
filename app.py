import streamlit as st
from config.settings import APP_NAME, APP_VERSION
from core.logger import logger

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

logger.info("Iniciando SENTINELA-CORE")

st.title("🛡️ SENTINELA-CORE")

st.caption(f"Versión {APP_VERSION}")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Eventos", "0")

with col2:
    st.metric("Alertas", "0")

with col3:
    st.metric("Riesgo", "Bajo")

with col4:
    st.metric("Estado", "Operativo")

st.divider()

st.subheader("Panel Principal")

st.info(
    "Bienvenido a SENTINELA-CORE. "
    "La arquitectura base se ha iniciado correctamente."
)

with st.sidebar:
    st.header("Navegación")

    opcion = st.radio(
        "Módulos",
        [
            "Dashboard",
            "Datos",
            "Análisis",
            "Configuración",
        ],
    )

st.success(f"Módulo seleccionado: {opcion}")
