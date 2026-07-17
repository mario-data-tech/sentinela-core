import streamlit as st
import pandas as pd

# 1. Configuración de página (siempre al inicio)
st.set_page_config(
    page_title="SENTINELA-CORE",
    page_icon="🛡️",
    layout="wide"
)

# 2. Estilo CSS para un toque profesional
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Barra lateral (Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/security-checked.png", width=60) # Puedes cambiar por tu logo
    st.title("🛡️ Panel de Control")
    st.markdown("---")
    opcion = st.radio("Navegación:", ["Carga de Datos", "Análisis", "Configuración"])
    st.markdown("---")
    st.info("Versión: 1.0.0 | Estado: Operativo")

# 4. Lógica principal
st.title("SENTINELA-CORE")
st.markdown("### Sistema avanzado de procesamiento de datos")

if opcion == "Carga de Datos":
    st.subheader("Cargar archivo de entrada")
    archivo = st.file_uploader("Sube tu archivo (CSV, Excel)", type=["csv", "xlsx"])
    
    if archivo:
        df = pd.read_csv(archivo) if archivo.name.endswith('.csv') else pd.read_excel(archivo)
        st.success("Archivo cargado correctamente")
        st.dataframe(df.head(), use_container_width=True)

elif opcion == "Análisis":
    st.subheader("Visualización de resultados")
    st.warning("A la espera de datos para procesar.")
    # Aquí irá tu lógica de procesamiento cuando la tengas lista

elif opcion == "Configuración":
    st.subheader("Configuración del Sistema")
    umbral = st.slider("Umbral de sensibilidad", 0, 100, 50)
    st.write(f"Sensibilidad actual: {umbral}%")
