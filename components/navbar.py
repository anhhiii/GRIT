import streamlit as st
from utils.css import load_css

def show_navbar(active_page="home"):
    load_css("assets/css/navbar.css")
    
    with st.container():
        st.markdown('<div id="navbar-container-anchor"></div>', unsafe_allow_html=True)
        
        # We use roughly centered columns for the navbar
        spacer_left, col1, col2, col3, spacer_right = st.columns([1, 2, 2, 2, 1])

        with col1:
            if st.button("Trang chủ", use_container_width=True, type="primary" if active_page=="home" else "secondary"):
                st.switch_page("pages/home.py")

        with col2:
            if st.button("Tủ sách", use_container_width=True, type="primary" if active_page=="book_list" else "secondary"):
                st.switch_page("pages/book_list.py")

        with col3:
            if st.button("AI Trợ lý", use_container_width=True, type="primary" if active_page=="chatbot" else "secondary"):
                st.switch_page("pages/chatbot.py")
                
        st.divider()