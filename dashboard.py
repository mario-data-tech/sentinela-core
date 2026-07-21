import streamlit as st
import pandas as pd
import numpy as np

def render_dashboard():
    st.subheader("📊 Panel General de Operaciones")
    
    # Simulación de datos para gráficos en tiempo real
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Eventos de Red", "Intentos de Acceso", "Anomalías Detectadas"]
    )
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("##### 📈 Tendencia de Eventos (Últimas 24 Horas)")
        st.line_chart(chart_data)
        
    with col2:
        st.markdown("##### 🌐 Distribución Geográfica")
        # Simulación de un mapa o métricas por región
        regions_data = pd.DataFrame({
            "Región": ["Norteamérica", "Europa", "Latinoamérica", "Asia-Pacífico"],
            "Incidentes": [12, 8, 24, 5]
        })
        st.dataframe(regions_data, hide_index=True, use_container_width=True)

    st.markdown("---")
    
    # Tabla de Alertas Recientes con Severidad
    st.markdown("##### 🚨 Alertas Recientes y Severidad")
    alerts_data = pd.DataFrame({
        "ID Alerta": ["ALT-9021", "ALT-9022", "ALT-9023", "ALT-9024"],
        "Timestamp": ["2026-07-20 21:15:02", "2026-07-20 21:18:45", "2026-07-20 21:22:10", "2026-07-20 21:25:30"],
        "Origen": ["192.168.1.45", "10.0.4.12", "172.16.8.99", "192.168.2.11"],
        "Tipo": ["Fuerza Bruta", "Tráfico Anómalo", "Inyección SQL", "Puerto Abierto"],
        "Severidad": ["🔴 Crítica", "🟠 Alta", "🟡 Media", "🟢 Baja"]
    })
    
    st.dataframe(alerts_data, hide_index=True, use_container_width=True)
