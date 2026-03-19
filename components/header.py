import streamlit as st
import streamlit.components.v1 as components
from utils.css import load_css


def show_header():
    load_css("assets/css/global.css")
    load_css("assets/css/header.css")
    load_css("assets/css/book_card.css")

    with st.container():
        st.markdown('<div id="header-container-anchor"></div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 4, 3], gap="large")

        with col1:
            # Fallback if logo doesn't exist
            try:
                st.image("assets/logo.png", width=100)
            except Exception:
                st.markdown("<div style='font-size:50px; text-align:center;'>🏛️</div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
                <div class="site-title">Hiên Chữ</div>
                <div class="site-subtitle">Thư Viện Sách Điện Tử</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            search = st.text_input(
                "Tìm kiếm",
                placeholder="🔎 Tìm sách, tác giả...",
                label_visibility="collapsed"
            )

    return search