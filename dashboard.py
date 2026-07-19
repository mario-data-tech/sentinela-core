import streamlit as st
import plotly.express as px
import pandas as pd
from services.data_service import DataService

def render_dashboard():
    """Renderiza el Dashboard Ejecutivo con visualizaciones interactivas."""
    st.header("📊 Panel de Control Ejecutivo")
    
    # Simulación de carga de datos para el dashboard
    try:
        # Aquí se integrarían los datos reales procesados por DataService
        data = {
            'Categoría': ['Seguridad', 'Rendimiento', 'Red', 'Almacenamiento'],
            'Valor': [85, 92, 78, 88]
        }
        df = pd.DataFrame(data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### Distribución de KPIs")
            fig = px.pie(df, values='Valor', names='Categoría', hole=0.3)
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.write("### Tendencia de Rendimiento")
            fig_bar = px.bar(df, x='Categoría', y='Valor', color='Categoría')
            st.plotly_chart(fig_bar, use_container_width=True)
            
        st.write("### Resumen de Datos")
        st.dataframe(df, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error al cargar el dashboard: {e}")

if __name__ == "__main__":
    render_dashboard()
