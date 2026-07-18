import sys
import os
import streamlit as st

# Añadir la raíz del proyecto al path de Python para asegurar que encuentre los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.kpi_card import mostrar_kpi
from models.dashboard import Kpi

st.set_page_config(page_title="Dashboard Ejecutivo", layout="wide")
# ... resto de tu código ...
