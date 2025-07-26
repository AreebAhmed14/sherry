from agent import sherry
import streamlit as st

st.set_page_config(page_title="sherry.assistant")
st.header("SHERRY 🍭 ASSISTANT ")

user = st.chat_input("shaheer...")

if user:
  st.info(f"{user}")

if user:
    result = sherry(user)
    st.write(result)
