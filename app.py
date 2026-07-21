import streamlit as st
from Sidebar import render_sidebar
from dashboard import render_dashboard

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
    </style>
""", unsafe_allow_html=True)

# Renderizar la barra lateral y capturar la página seleccionada
selected_page = render_sidebar()

# Contenido principal según la opción seleccionada
if selected_page == "📊 Dashboard":
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
    
    # Cargar el contenido del dashboard con gráficos y alertas
    render_dashboard()

else:
    # Vista genérica para los demás módulos en desarrollo
    st.title(selected_page)
    st.markdown("---")
    st.info(f"🚧 El módulo **{selected_page}** se encuentra cargando los servicios de red y modelos de datos...")
