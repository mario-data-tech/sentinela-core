import streamlit as st

def mostrar_kpi(nombre: str, valor: str):
    """
    Muestra una tarjeta KPI utilizando el componente st.metric.
    """
    st.metric(
        label=nombre,
        value=valor
    )
