import streamlit as st
from services.book_service import BookService
from components.book_card import display_book_card
from components.header import show_header
from components.navbar import show_navbar

st.set_page_config(
    page_title="Hiên Chữ - Trang chủ",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()
show_navbar(active_page="home")

from utils.css import load_css

# ===== CSS BỔ SUNG =====
load_css("assets/css/home.css")

# ===== HERO SECTION =====
with st.container():
    h_col1, h_col2 = st.columns([1.1, 1], gap="large")
    
    with h_col1:
        st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Khám phá thế giới<br>qua từng <span>trang sách</span></h1>
            <p class="hero-subtitle">Hiên Chữ là không gian đọc sách điện tử cao cấp, nơi lưu giữ tinh hoa trí thức với hàng ngàn đầu sách thuộc mọi thể loại. Đắm chìm vào không gian văn hoá đọc ngay hôm nay cùng hệ thống gợi ý AI thông minh.</p>
        </div>
        """, unsafe_allow_html=True)
        
        btn_col1, btn_col2 = st.columns([1, 1.5])
        with btn_col1:
            if st.button("📚 Bắt đầu khám phá", type="primary", use_container_width=True):
                st.switch_page("pages/book_list.py")
                
    with h_col2:
        st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=1200&auto=format&fit=crop", 
                 use_container_width=True)

# ===== THỐNG KÊ (STATISTICS) =====
st.markdown("<br>", unsafe_allow_html=True)
s_col1, s_col2, s_col3 = st.columns(3)

with s_col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">1000+</div>
        <div class="stat-label">ĐẦU SÁCH CHẤT LƯỢNG</div>
    </div>
    """, unsafe_allow_html=True)
with s_col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">25+</div>
        <div class="stat-label">THỂ LOẠI PHONG PHÚ</div>
    </div>
    """, unsafe_allow_html=True)
with s_col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">24/7</div>
        <div class="stat-label">BOT TƯ VẤN SÁCH AI</div>
    </div>
    """, unsafe_allow_html=True)

# ===== SÁCH ĐỀ XUẤT =====
st.markdown("<div class='section-title'>Dành Cho Tuần Này</div>", unsafe_allow_html=True)

all_books = BookService.get_books()

if not all_books.empty:
    books_to_show = all_books.head(8) # Lấy 8 cuốn cho trang chủ gọn gàng
    
    # Render thành lưới 4 cột
    for i in range(0, len(books_to_show), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(books_to_show):
                with cols[j]:
                    display_book_card(books_to_show.iloc[i+j])

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Nút bấm trung tâm
    center = st.columns([2, 1, 2])[1]
    with center:
        if st.button("Xem Toàn Bộ Tủ Sách ➡", use_container_width=True):
            st.switch_page("pages/book_list.py")

else:
    st.info("Hiện hệ thống chưa có dữ liệu sách.")

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:#a39991; font-family:\"Inter\", sans-serif; font-size:14px'>© 2026 Hiên Chữ Library. Built for serious readers.</div>", unsafe_allow_html=True)