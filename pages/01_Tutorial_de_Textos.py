import streamlit as st

# titulo 
st.title("Título da página - Tutorial de Textos")

# cabeçalho
st.header("Cabeçalho do Streamlit")

# subcabeçalho
st.subheader("Sub Cabeçalho para ver como é")

st.subheader("Primeira seção")

# texto qualquer 
st.text("Essa é a primeira seção e isso aqui é só um texto")

st.subheader("Segunda Seção")

# escrever - write 
st.write("Isso aqui é só uma escrita de texto")



# markdown 
st.markdown("""---""")
st.markdown("Esse é um texto usando Markdown")
st.markdown("# Esse é um cabeçalho em markdown ")
st.markdown("## Esse é um subtítulo")
st.markdown("### Terceiro nível de titulo em markdown")

st.markdown("Esse aqui é um tutorial, **preste atenção** *é importante*")

st.markdown("[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)")

st.text("Lista de tarefas:")
st.markdown("""
            1. Criar uma conta no [streamlit.io](www.streamlit.io)
            2. Criar uma conta no [github.com](www.github.com) 
            3. Criar um projeto no streamlit 
            4. Assistir os vídeos do tutorial :) 
            5. Praticar, praticar, praticar
            """)

st.markdown("""---""")

# Emojis 
st.markdown("### Emojis")
st.markdown("[Emojis](https://share.streamlit.io/streamlit/emoji-shortcodes)")
st.markdown(":thumbsup: :heart: :books: :rocket: :smile: :checkered_flag:")

st.markdown("""---""")

# HTML 
st.markdown("### HTML")

html_code = """
    <h1 style='color: blue;'>Esse é um cabeçalho rosa</h1>
    <p style='color: purple;'> Esse é um parágrafo</p>
"""

st.markdown(html_code, unsafe_allow_html=True)


st.markdown("""---""")
