import streamlit as st
from components.header import show_header
from components.navbar import show_navbar
from services.book_service import BookService
from components.book_card import display_book_card

# Bắt buộc nằm đầu tiên
st.set_page_config(page_title="Hiên Chữ - Home", layout="wide", initial_sidebar_state="collapsed")

show_header()
show_navbar()

st.subheader("📚 Sách mới cập nhật")

# Logic lấy data và Grid 3 cột
all_books = BookService.get_books()
if not all_books.empty:
    books_to_show = all_books.head(15)
    # Chia Grid 3 cột
    for i in range(0, len(books_to_show), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(books_to_show):
                with cols[j]:
                    display_book_card(books_to_show.iloc[i + j])