import streamlit as st
import requests
from frontend.components.mycomponent import react_counter

st.title("Integração Streamlit + React")
st.title("Abaixo está um componente React dentro do Streamlit: ")

count = react_counter(count = 5)

st.write(f"O contador atual é: {count}")
