import streamlit as st

# Configuración de seguridad: Define tu usuario y contraseña
USER_CORRECT = "admin"
PASS_CORRECT = "sentinela2026"

def check_password():
    """Devuelve True si el usuario ingresó la contraseña correcta."""
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if st.session_state.password_correct:
        return True

    # Formulario de login
    login_container = st.container()
    with login_container:
        st.subheader("🔒 Acceso Restringido - Sentinela Core")
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        if st.button("Ingresar"):
            if username == USER_CORRECT and password == PASS_CORRECT:
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
    return False

# Ejecución principal
if check_password():
    st.title("🛡️ Sentinela Core - Panel de Control")
    st.write("Bienvenido al sistema protegido.")
    # Aquí iría el resto de tu código de análisis...
