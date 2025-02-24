import streamlit as st 

st.image("img/logo.gif")

st.title("Imagens no Streamlit")

imagem = st.file_uploader("Escolha uma imagem", type=["jpg","jpeg","gif","png"])

if imagem:
    st.image(imagem)
    
st.write("Nos siga nas nossas redes sociais!")
colunas = st.columns(3)

# 0, 1, 2, 3, 4 .....


colunas[0].image("imagens/Insta-white.png")
colunas[1].image("img/Twitter-white.png")
colunas[2].image("img/Youtube-white.png")

st.image("img/Medal.gif")
