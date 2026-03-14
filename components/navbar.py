import streamlit as st

def show_navbar():

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        if st.button("🏠 Trang chủ", use_container_width=True):
            st.switch_page("pages/home.py")

    with col2:
        if st.button("📚 Tủ sách", use_container_width=True):
            st.switch_page("pages/book_list.py")

    with col3:
        if st.button("🤖 Chatbot", use_container_width=True):
            st.switch_page("pages/chatbot.py")

    st.divider()