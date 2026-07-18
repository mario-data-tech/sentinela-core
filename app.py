import streamlit as st

st.set_page_config(
    page_title="SENTINELA-CORE",
    page_icon="🛡️",
    layout="wide"
)

st.title("Bienvenido a SENTINELA-CORE")
st.subheader("Sistema de Gestión y Monitoreo Empresarial")

st.info("Utiliza el menú lateral para navegar a través de los módulos del sistema.")

# Un pequeño resumen o mensaje de bienvenida
st.markdown("""
### Módulos disponibles:
- 🛡️ **Dashboard Ejecutivo**: Vista general de KPIs y métricas clave.
""")
