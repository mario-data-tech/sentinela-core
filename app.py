import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="SENTINELA-CORE",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para un look moderno tipo Datadog/Splunk
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .metric-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 15px;
            border-radius: 8px;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo principal
st.title("🛡️ SENTINELA-CORE")
st.markdown("**Plataforma inteligente de monitoreo, análisis y respuesta para entornos empresariales.**")
st.markdown("---")

# Indicador de estado del sistema
st.success("🟢 **Estado del Sistema:** Todos los servicios operativos (0 incidentes activos)")

# Panel de Métricas Principales (Tarjetas)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="👥 Usuarios Activos", value="1,245", delta="+12%")
with col2:
    st.metric(label="⚙️ Sistemas Monitoreados", value="48", delta="0")
with col3:
    st.metric(label="🚨 Alertas Recientes", value="3", delta="-2", delta_color="inverse")
with col4:
    st.metric(label="⚡ Latencia Promedio", value="24 ms", delta="-4 ms")

st.markdown("---")
st.info("💡 Bienvenido al núcleo de análisis empresarial. Selecciona una opción en el menú lateral para navegar.")
