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
show_navbar()

# ========================
# LẤY ID SÁCH
# ========================

book_id = st.session_state.get("selected_book_id", None)

if book_id is None:
    st.warning("⚠️ Bạn chưa chọn cuốn sách nào.")
    if st.button("⬅ Quay lại tủ sách"):
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

col_img, col_info = st.columns([1, 2], gap="large")

with col_img:

    if book["img_url"]:
        st.image(book["img_url"], use_container_width=True)
    else:
        st.image(
            "https://via.placeholder.com/300x450?text=No+Image",
            use_container_width=True
        )

with col_info:

    st.markdown(f"## {book['title']}")

    st.markdown(
        f"""
**✍️ Tác giả:** {book['author']}  

**📖 ISBN:** {book['isbn']}
"""
    )

    st.divider()

    st.markdown("### 📝 Mô tả nội dung")

    description = book["description"] if book["description"] else "Chưa có mô tả."

    st.write(description)

    st.divider()

    if st.button("⬅ Quay lại tủ sách"):
        st.switch_page("pages/book_list.py")