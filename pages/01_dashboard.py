import streamlit as st
from components.kpi_card import mostrar_kpi
from models.dashboard import Kpi

st.set_page_config(page_title="Dashboard Ejecutivo", layout="wide")

st.title("🛡️ Dashboard Ejecutivo")
st.markdown("---")

# Simulamos datos (más adelante vendrán de una base de datos)
kpi1 = Kpi(nombre="Alertas Activas", valor="12", estado="crítico")
kpi2 = Kpi(nombre="Eventos Recientes", valor="48", estado="normal")

col1, col2 = st.columns(2)

with col1:
    mostrar_kpi(kpi1.nombre, kpi1.valor)

with col2:
    mostrar_kpi(kpi2.nombre, kpi2.valor)
