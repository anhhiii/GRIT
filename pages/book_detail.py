import streamlit as st
from services.book_service import BookService
from components.header import show_header
from components.navbar import show_navbar

# Cấu hình trang
st.set_page_config(
    page_title="Chi tiết sách",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()
show_navbar(active_page="book_list")

from utils.css import load_css

# CSS Bổ Sung cho trang chi tiết
load_css("assets/css/book_detail.css")

# ========================
# LẤY ID SÁCH
# ========================
book_id = st.session_state.get("selected_book_id", None)

if book_id is None:
    st.warning("⚠️ Bạn chưa chọn cuốn sách nào.")
    if st.button("← Quay lại tủ sách"):
        st.switch_page("pages/book_list.py")
    st.stop()

# ========================
# LẤY DỮ LIỆU
# ========================
book = BookService.get_book_details(book_id)

if book is None:
    st.error("Không tìm thấy thông tin cuốn sách.")
    st.stop()

# ========================
# HIỂN THỊ CHI TIẾT
# ========================

st.markdown('<div class="book-detail-container">', unsafe_allow_html=True)

col_img, col_info = st.columns([1, 2.5], gap="large")

with col_img:
    img_url = book["img_url"] if book["img_url"] else "https://via.placeholder.com/400x600?text=No+Cover"
    st.markdown(f"""
    <div class="book-cover-wrapper">
        <img src="{img_url}" alt="{book['title']}">
    </div>
    """, unsafe_allow_html=True)

with col_info:
    st.markdown(f'<div class="bd-title">{book["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bd-author">Viết bởi: {book["author"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bd-meta">📚 ISBN: <strong>{book["isbn"]}</strong></div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="margin: 1.5rem 0;">', unsafe_allow_html=True)
    
    st.markdown('<div class="bd-desc-title">Nội Dung Tóm Tắt</div>', unsafe_allow_html=True)
    description = book["description"] if book["description"] else "Chưa có mô tả chi tiết cho cuốn sách này."
    st.markdown(f'<div class="bd-desc-text">{description}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

col_btn = st.columns([1, 4])[0]
with col_btn:
    if st.button("← Quay lại Tủ sách", use_container_width=True):
        st.switch_page("pages/book_list.py")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:#a39991; font-family:\"Inter\", sans-serif; font-size:14px'>© 2026 Hiên Chữ Library. Built for serious readers.</div>", unsafe_allow_html=True)