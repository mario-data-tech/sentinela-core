import streamlit as st
import pandas as pd
from data_processor import filtrar_datos  # Importamos tu módulo de filtrado

# Configuración de la página
st.set_page_config(page_title="Sentinela Core", layout="wide")

st.title("🛡️ Sentinela Core - Panel de Control")

# Simulamos carga de datos (En el futuro, aquí conectarás a tu base o API)
data = [
    {"id": 1, "status": "activo", "valor": 100},
    {"id": 2, "status": "inactivo", "valor": 50},
    {"id": 3, "status": "activo", "valor": 200}
]

st.sidebar.header("Filtros de Sistema")
filtro = st.sidebar.selectbox("Seleccionar Estado", ["activo", "inactivo"])

# Ejecución del procesador
if st.button("Ejecutar Análisis"):
    resultado = filtrar_datos(data, "status", filtro)
    st.write("Resultados filtrados:", pd.DataFrame(resultado))
else:
    st.info("Presiona el botón para procesar los datos.")

# Esto mantiene al servicio "vivo" y reportando actividad
st.sidebar.success("Sistema Sentinela Online")
