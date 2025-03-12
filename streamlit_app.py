import streamlit as st 
from streamlit_option_menu import option_menu



st.set_page_config(layout="wide", page_title="TechSchool 2025 - Tutorial Streamlit")

semMenuLateralStyle = """
     <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
"""
st.markdown(semMenuLateralStyle, unsafe_allow_html=True)

st.header("Sobre")

st.markdown("""
Meninas, esta é a página principal do tutorial. 
            **Usem o menu na esquerda** para navegar entre os exemplos. """)


"---"

#opção padrão

optionMenu = option_menu(
    menu_title="Tutorial Option Menu", # obrigatorio
    options=["Logar","Cadastrar"], # obrigatorio 
    icons=["house", "ghost"], # opcional
    menu_icon="cast",
    default_index=1

)


#opção customizada e na horizontal
optionMenu2 = option_menu(
    menu_title="",
    options=["Logar", "Cadastrar"],
    icons=["house", "envelope"],
    menu_icon="alien",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "purple",
            "color": "black"
        },
        "nav-link-selected": {"background-color": "#e31033"}
    }
)


if optionMenu2 == "Logar":
    with st.form("formLogar"):
        usuario = st.text_input("Usuário:", placeholder="Informe seu usuário...")
        senha = st.text_input("Senha:", placeholder="Informe sua senha...", type="password")
        btnLogarUsuario = st.form_submit_button("Logar", use_container_width=True)

        if btnLogarUsuario:
            st.success("Você clicou no botão de logar!")


if optionMenu2 == "Cadastrar":
    with st.form("formFirebase"):
        nome = st.text_input("Nome:", placeholder="Informe seu nome...")
        apelido = st.text_input("Apelido:", placeholder="Informe seu apelido...")
        idade = st.number_input("Idade:", step=1, min_value=8, max_value=100)
        senha = st.text_input("Senha:", placeholder="Informe sua senha...", type="password")
        btnCadastrarUsuario = st.form_submit_button("Cadastrar", use_container_width=True)
