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
show_navbar()

# ===== GIỚI THIỆU WEB =====

st.markdown("## 📖 Chào mừng đến với Hiên Chữ")

st.markdown(
"""
**Hiên Chữ** là thư viện sách điện tử giúp bạn khám phá những cuốn sách hay  
thuộc nhiều thể loại khác nhau như:

- 📚 Văn học
- 💼 Kinh tế
- 🧠 Kỹ năng
- 📜 Lịch sử

Bạn có thể tìm kiếm, khám phá và đọc mô tả của từng cuốn sách  
để tìm ra cuốn sách phù hợp với mình.
"""
)

st.divider()

# ===== SÁCH ĐỀ XUẤT =====

st.subheader("⭐ Sách đề xuất")

all_books = BookService.get_books()

if not all_books.empty:

    # Lấy 12 cuốn đầu
    books_to_show = all_books.head(12)

    cols = st.columns(4)

    for index, row in books_to_show.iterrows():
        with cols[index % 4]:
            display_book_card(row)

    st.divider()

    center = st.columns([2,1,2])[1]

    with center:
        if st.button("📚 Xem toàn bộ tủ sách"):
            st.switch_page("pages/book_list.py")

else:
    st.warning("Chưa có sách trong hệ thống.")