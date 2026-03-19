import streamlit as st
from services.book_service import BookService
from components.book_card import display_book_card
from components.header import show_header
from components.navbar import show_navbar

st.set_page_config(
    page_title="Hiên Chữ - Tủ sách",
    layout="wide",
    initial_sidebar_state="collapsed"
)

search = show_header()
show_navbar(active_page="book_list")

from utils.css import load_css

# ===== CSS BỔ SUNG =====
load_css("assets/css/book_list.css")

# ===== HEADER TRANG =====

col1, col2 = st.columns([4,1])

with col1:
    st.markdown("""
    <div class="page-title">Tủ sách Hiên Chữ</div>
    <div class="page-subtitle">Khám phá và đắm chìm trong không gian tri thức bất tận.</div>
    """, unsafe_allow_html=True)

# map category_id -> tên thể loại
category_map = {
    1: "Văn học",
    2: "Kinh tế",
    3: "Kỹ năng",
    4: "Lịch sử",
    5: 'tâm lý',
    6: 'khoa học', 
    7: 'trinh thám', 
    8: 'novel', 
    9: 'fiction', 
    10:'finance', 
    11: 'history', 
    12: 'science', 
    13: 'mystery',
    14: 'nấu ăn', 
    15: 'biện chứng', 
    16: 'startup', 
    17: 'marketing', 
    18: 'leadôn tình', 
    20: 'kiếm hiệp', 
    21: 'tiểu thuyết', 
    22: 'bi kịch', 
    23: 'hài kịch',
    24: 'physics', 
    25: 'biology'
}

with col2:
    genre = st.selectbox(
        "Thể loại",
        ["Tất cả"] + list(category_map.values())
    )

# ===== LẤY DỮ LIỆU =====

df_books = BookService.get_books()

if df_books.empty:
    st.warning("⚠️ Hiện chưa có dữ liệu sách trong hệ thống.")
    st.stop()

# ===== SEARCH =====

if search:
    df_books = df_books[
        df_books["title"].str.contains(search, case=False, na=False) |
        df_books["author"].str.contains(search, case=False, na=False)
    ]

# ===== FILTER THEO THỂ LOẠI =====

if genre != "Tất cả":

    # tìm category_id tương ứng
    selected_id = [k for k, v in category_map.items() if v == genre][0]

    df_books = df_books[df_books["category_id"] == selected_id]

# ===== HIỂN THỊ =====

import math

if df_books.empty:
    st.warning("Không tìm thấy sách.")
else:
    # --- Xử lý State Phân Trang ---
    if "current_page" not in st.session_state:
        st.session_state.current_page = 1

    # Reset trang về 1 khi người dùng tìm kiếm hoặc đổi thể loại
    if "last_search" not in st.session_state:
        st.session_state.last_search = search
    if "last_genre" not in st.session_state:
        st.session_state.last_genre = genre
        
    if st.session_state.last_search != search or st.session_state.last_genre != genre:
        st.session_state.current_page = 1
        st.session_state.last_search = search
        st.session_state.last_genre = genre

    ITEMS_PER_PAGE = 20
    total_pages = max(1, math.ceil(len(df_books) / ITEMS_PER_PAGE))

    # Đảm bảo trang hiện tại không vượt quá giới hạn
    if st.session_state.current_page > total_pages:
        st.session_state.current_page = total_pages
    elif st.session_state.current_page < 1:
        st.session_state.current_page = 1
        
    page = st.session_state.current_page

    st.caption(f"Tìm thấy {len(df_books)} cuốn sách")

    # Phân trang dữ liệu
    start_idx = (page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    books_to_show = df_books.iloc[start_idx:end_idx]

    # Render danh sách sách
    for i in range(0, len(books_to_show), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(books_to_show):
                with cols[j]:
                    display_book_card(books_to_show.iloc[i+j])
                    
    # Render thanh điều hướng phân trang ở dưới cùng
    if total_pages > 1:
        st.markdown("<hr style='border: none; border-top: 1px solid rgba(136, 115, 96, 0.15); margin: 3rem 0 2rem 0;'>", unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
        
        with col2:
            if st.button("← Lùi lại", disabled=(page == 1), use_container_width=True):
                st.session_state.current_page -= 1
                st.rerun()
                
        with col3:
            def on_page_change():
                st.session_state.current_page = st.session_state.page_input
                
            st.number_input(
                "Trang", min_value=1, max_value=total_pages, 
                value=page, label_visibility="collapsed",
                key="page_input", on_change=on_page_change
            )
            
        with col4:
            if st.button("Tiếp theo →", disabled=(page == total_pages), use_container_width=True):
                st.session_state.current_page += 1
                st.rerun()

        st.markdown(f"<div style='text-align: center; color: #8c8279; font-family: \"Inter\", sans-serif; font-size: 0.95rem; margin-top: 20px;'>Đang hiển thị trang {page} / {total_pages}</div><br><br>", unsafe_allow_html=True)