import requests 
import streamlit as st
from streamlit_lottie import st_lottie

st.title("Animações do Lottie no Streamlit")


def carregar_animacao(url: str):
   requisicao = requests.get(url)
   if requisicao.status_code != 200:
      return None
   return requisicao.json()


url_animacao = "https://lottie.host/a611e837-5349-4dd9-ac12-808d4e9152c1/KsNWjGPpbb.json"

animacaoChat = carregar_animacao(url_animacao)

st_lottie(animacaoChat, key="animacaoChat", speed=1, loop=True)