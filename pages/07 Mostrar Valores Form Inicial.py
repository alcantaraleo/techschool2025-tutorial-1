import streamlit as st 


st.title("Mostrando os valores do Form Inicial")


st.write("Você disse no form inicial que o seu nome é ", st.session_state["nomeUsuario"])