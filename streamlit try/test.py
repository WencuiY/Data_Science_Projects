import streamlit as st
def app():
    st.write("This is a button test app.")
    button= st.button
    if button("Click!"):
        st.write("TEST IS SUCCESSFUL!")

app()