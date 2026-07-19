import streamlit as st

def render_sidebar():
    """Renderiza la barra lateral de navegación y configuración."""
    with st.sidebar:
        st.image("assets/images/logo.png", use_column_width=True) # Requiere archivo
        st.title("🛡️ Sentinela Core")
        st.markdown("---")
        
        st.write("### Navegación")
        page = st.radio("Ir a:", ["Dashboard", "Analítica", "Configuración"])
        
        st.markdown("---")
        st.write("### Estado del Sistema")
        st.status("Conectado", expanded=True)
        
        st.markdown("---")
        st.write("© 2026 SENTINELA-CORE")
        
    return page
