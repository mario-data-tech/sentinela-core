import streamlit as st
import logging
from pathlib import Path

# Configuración inicial de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/app.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

# Configuración de página
st.set_page_config(
    page_title="SENTINELA-CORE | Dashboard Ejecutivo",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Punto de entrada principal de la aplicación."""
    st.title("🛡️ SENTINELA-CORE Enterprise Edition")
    st.markdown("---")
    
    st.success("Sistema inicializado correctamente.")
    
    # Placeholder para dashboard
    st.subheader("Vista General")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Usuarios Activos", "1,234", "+12%")
    with col2:
        st.metric("Sistemas Monitoreados", "85", "0")
    with col3:
        st.metric("Alertas Críticas", "2", "-5")
        
    logger.info("Dashboard principal cargado.")

if __name__ == "__main__":
    main()
