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
show_navbar()

# ===== HEADER TRANG =====

col1, col2 = st.columns([4,1])

with col1:
    st.markdown("## 📚 Tủ sách")

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

if df_books.empty:
    st.warning("Không tìm thấy sách.")
else:

    st.caption(f"Tìm thấy {len(df_books)} cuốn sách")

    for i in range(0, len(df_books), 4):
        cols = st.columns(4)

        for j in range(4):
            if i + j < len(df_books):
                with cols[j]:
                    display_book_card(df_books.iloc[i+j])