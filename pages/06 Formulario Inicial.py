import streamlit as st 

st.title("Tutorial para compartilhar dados entre páginas - Parte 1")

if "nomeUsuario" not in st.session_state:
    st.session_state["nomeUsuario"] = ""


with st.form("formInicial"):
    nomeUsuario = st.text_input("Preencha o seu nome:", placeholder="Seu nome vai aqui...")

    btnEnviarFormInicial = st.form_submit_button("Salvar")

    if btnEnviarFormInicial:
        st.session_state["nomeUsuario"] = nomeUsuario

st.write("Seu nome de usuário é", nomeUsuario)        