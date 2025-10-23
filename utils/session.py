import streamlit as st

def init_session():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    if "refresh_interval" not in st.session_state:
        st.session_state.refresh_interval = 60
