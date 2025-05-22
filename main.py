import streamlit as st
from src.tutor_virtual import generar_respuesta

st.title("Tutor Virtual Inteligente")
pregunta = st.text_input("Escribe tu pregunta:")

if st.button("Responder"):
    if pregunta:
        respuesta = generar_respuesta(pregunta, api_key="TU_API_KEY")
        st.markdown(f"**Respuesta:** {respuesta}")
