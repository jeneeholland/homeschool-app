import streamlit as st

st.title("My First Streamlit App")

st.write("Hello Jenee!")

name = st.text_input("What is your name?")

if name:
    st.write(f"Hello, {name}!")