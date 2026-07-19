import os
import subprocess
import sys

def run_app():
    """Script para ejecutar la aplicación de forma profesional."""
    try:
        print("Iniciando SENTINELA-CORE...")
        subprocess.check_call([sys.executable, "-m", "streamlit", "run", "app.py"])
    except subprocess.CalledProcessError as e:
        print(f"Error al iniciar la aplicación: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    run_app()
