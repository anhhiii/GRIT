import streamlit as st


def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show_header():

    load_css()

    st.markdown("""
    <style>
    [data-testid="stSidebar"] {display:none;}
    header {visibility:hidden;}
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.2, 3, 2])

    with col1:
        st.image("assets/logo.png", width=120)

    with col2:
        st.markdown("""
        <div class="site-title">Hiên Chữ</div>
        <div class="site-subtitle">Thư viện sách điện tử</div>
        """, unsafe_allow_html=True)

    with col3:
        search = st.text_input(
            "🔎 Tìm kiếm theo tên sách hoặc tác giả",
            placeholder="Ví dụ: Dế mèn phiêu lưu ký..."
        )

    return search