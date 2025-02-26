import streamlit as st

st.set_page_config(layout="wide", page_title="Tutorial de Formulário")


st.title("TechSchool 2025 - Tutorial Streamlit - Formulário")

st.header("Preencha o formulário abaixo")

st.markdown("""---""")

nome = st.text_input("Informe seu nome:", placeholder="Preencha o seu nome")

idade = st.number_input("Informe sua idade:", min_value=8, max_value=18, step=1)

dataNascimento = st.date_input("Dt. Nascimento", format="DD/MM/YYYY")

horaAtual = st.time_input("Selecione a hora:", step=60)

corPerfil = st.color_picker("Selecione a cor do perfil")

st.write("Nome:", nome)
st.write("Idade:", idade)
st.write("Data Nascimento:", dataNascimento)
st.write("Horal Atual:", horaAtual)

html_code = """
        <h1 style='color: {};'>Essa é a cor que você escolheu para o seu perfil</h1>
""".format(corPerfil)
st.markdown(html_code, unsafe_allow_html=True)


