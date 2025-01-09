import streamlit as st
from datetime import datetime

def sidebar():
    st.sidebar.title("Navigation")
    router = st.sidebar.radio("Go to", ["Home", "Load Data", "Chat"])
    return router