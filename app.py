import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar clave de API desde .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configurar la API de Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Configuración de la aplicación
st.set_page_config(page_title="Recetas Inteligentes", layout="centered")

# Encabezado
st.title("🥗 Recetas Inteligentes con IA")
st.write("Ingresa los ingredientes que tienes en casa y descubre qué recetas puedes preparar.")

# Entrada del usuario
ingredientes = st.text_area("✏️ Escribe tus ingredientes separados por comas:")

# Función para obtener recetas de Gemini
def obtener_receta(ingredientes_usuario):
    prompt = f"""
    Actúa como un chef experto. Basado en los ingredientes proporcionados por el usuario: {ingredientes_usuario},
    sugiere una receta con pasos detallados de preparación. Si faltan ingredientes esenciales, ofrece sustituciones.
    La respuesta debe ser clara y fácil de seguir.
    """
    respuesta = model.generate_content(prompt)
    return respuesta.text

# Botón para generar la receta
if st.button("🍳 Obtener Receta"):
    if ingredientes.strip():
        with st.spinner("Generando receta..."):
            receta = obtener_receta(ingredientes)
        st.success("¡Aquí tienes tu receta!")
        st.write(receta)
    else:
        st.warning("⚠️ Por favor, ingresa al menos un ingrediente.")
