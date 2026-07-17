import streamlit as st
import plotly.express as px

from config.settings import APP_NAME, APP_VERSION
from core.logger import logger
from services.data_service import obtener_datos_demo
from utils.helpers import obtener_fecha_actual

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🛡️",
    layout="wide",
)

logger.info("SENTINELA-CORE iniciado")

st.title("🛡️ SENTINELA-CORE")
st.caption(f"Versión {APP_VERSION}")

st.write(f"Última actualización: {obtener_fecha_actual()}")

st.divider()

df = obtener_datos_demo()

col1, col2, col3 = st.columns(3)

col1.metric("Eventos", len(df))
col2.metric("Alertas", int(df["Cantidad"].sum()))
col3.metric("Estado", "Operativo")

st.divider()

fig = px.bar(
    df,
    x="Categoría",
    y="Cantidad",
    title="Distribución de Eventos"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df, use_container_width=True)

with st.sidebar:
    st.header("Centro de Control")
    st.success("Sistema Operativo")
