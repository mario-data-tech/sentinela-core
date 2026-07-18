import streamlit as st
from components.kpi_card import mostrar_kpi
from models.dashboard import Kpi

# Ejemplo de uso
mi_kpi = Kpi(nombre="Alertas Activas", valor="12", estado="crítico")
mostrar_kpi(mi_kpi.nombre, mi_kpi.valor)
