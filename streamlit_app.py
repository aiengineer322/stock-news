import streamlit as st
from client.sidebar import sidebar
from client.loadData import loadData
from client.home import home
from client.chat import chat

st.set_page_config(layout="wide")
router = sidebar()

if(router == "Home"):
    home()
if(router == "Load Data"):
    loadData()
if(router == "Chat"):
    chat()