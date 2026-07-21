import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/shield.png", width=64)
        st.title("SENTINELA-CORE")
        st.caption("v2.4.0 - Enterprise Edition")
        
        st.markdown("---")
        
        # Menú de navegación principal
        st.subheader("Navegación")
        selected_page = st.radio(
            "Seleccione un módulo",
            ["📊 Dashboard", "📡 Monitoreo", "🚨 Alertas", "🖥️ Activos", "📈 Reportes", "⚙️ Configuración", "🛠️ Administración"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Filtros rápidos o estado de sesión en la barra lateral
        st.subheader("Filtros Globales")
        st.selectbox("Entorno", ["Producción", "Staging", "Desarrollo"])
        st.slider("Rango de tiempo (horas)", 1, 24, 6)
        
        st.markdown("---")
        st.markdown("🟢 **Conectado al Nodo Central**")
        
        return selected_page
