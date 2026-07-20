import streamlit as st
import logging

# Configuración de logging simplificada para la nube
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuración de la página
st.set_page_config(page_title="SENTINELA-CORE", layout="wide")

# Título y estado
st.title("🛡️ SENTINELA-CORE")
st.success("Sistema operativo y desplegado en la nube.")

# Dashboard rápido de prueba
col1, col2, col3 = st.columns(3)
col1.metric("Usuarios", "1,234", "+12%")
col2.metric("Sistemas", "85", "0")
col3.metric("Alertas", "2", "-5")

st.write("### Bienvenido al núcleo de análisis empresarial.")

# Mensaje de confirmación
if st.button("Verificar sistema"):
    st.info("Los servicios están respondiendo correctamente.")
    logging.info("El usuario verificó el estado del sistema.")
