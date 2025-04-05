# Nome da pagina: Teste

import streamlit as st
import requests
from frontend.components.mycomponent import react_counter
st.set_page_config(page_title="Meu App", layout="wide")
st.sidebar.success("Aqui está a página principal do projeto, com a apresentação da proposta")


st.title("Bem vindo ao site!")

st.markdown("""
Foi desenvolvido uma aplicação realizando a integração da biblioteca Streamlit com React com muito auxilio de:
- João Victor Assaoka
- João Vitor Mâncio Chaves
- Chat GPT
- DeepSeek
""")

st.write("Abaixo está o exemplo desenvolvido durante o treinamento da integração entre Streamlit e React:")
count = react_counter(count = 5)
st.write(f"Recebendo os dados do react sobre o valor do contador: {count}")

st.divider()
st.write("Autor: Gabriel G. A.")