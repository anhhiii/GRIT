import streamlit as st
import json
import pandas as pd
from openai import OpenAI

# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="Goodbook",
    page_icon="📚",
    layout="wide"
)

# ==========================
# STYLE UI
# ==========================

st.markdown("""
<style>

.stApp {
background-color:#f8f6f3;
}

.title{
font-size:40px;
font-weight:bold;
color:#2c3e50;
}

.card{
padding:20px;
border-radius:15px;
background:white;
box-shadow:0 3px 10px rgba(0,0,0,0.1);
margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# LOAD DATABASE
# ==========================

@st.cache_data
def load_books():
    with open("books.json", encoding="utf-8") as f:
        return json.load(f)

books = load_books()

# ==========================
# SIDEBAR MENU
# ==========================

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Trang chủ",
        "Danh mục sách",
        "Chi tiết sách",
        "AI gợi ý sách"
    ]
)

# ==========================
# TRANG CHỦ
# ==========================

if menu == "Trang chủ":

    st.markdown('<p class="title">📚 Goodbook</p>', unsafe_allow_html=True)

    st.subheader("Mỗi cuốn sách – Một cánh cửa mới")

    st.write("""
    Goodbook giúp bạn tìm cuốn sách phù hợp chỉ trong vài phút.
    """)
    
    st.divider()

    st.header("🔥 Sách nổi bật")

    cols = st.columns(3)

    for i, book in enumerate(books[:3]):
        with cols[i]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader(book["title"])
            st.write("✍️", book["author"])
            st.write(book["description"])
            st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# DANH MỤC SÁCH
# ==========================

elif menu == "Danh mục sách":

    st.title("📚 Danh mục sách")

    categories = list(set(book["category"] for book in books))

    category = st.selectbox(
        "Chọn thể loại",
        ["Tất cả"] + categories
    )

    for book in books:

        if category == "Tất cả" or book["category"] == category:

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader(book["title"])
            st.write("Tác giả:", book["author"])
            st.write("Thể loại:", book["category"])
            st.write(book["description"])

            st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# CHI TIẾT SÁCH
# ==========================

elif menu == "Chi tiết sách":

    st.title("📖 Chi tiết sách")

    titles = [b["title"] for b in books]

    selected = st.selectbox(
        "Chọn sách",
        titles
    )

    for book in books:

        if book["title"] == selected:

            st.header(book["title"])

            col1, col2 = st.columns([1,2])

            with col1:
                st.image(
                    "https://cdn-icons-png.flaticon.com/512/2232/2232688.png",
                    width=150
                )

            with col2:

                st.write("✍️ Tác giả:", book["author"])
                st.write("📅 Năm:", book["year"])

                st.subheader("Tóm tắt")
                st.write(book["description"])

                st.subheader("Ai nên đọc?")
                st.write(book["who_should_read"])

                st.subheader("Thời điểm đọc")
                st.write(book["when_to_read"])

                st.subheader("Điểm nổi bật")
                st.write(book["highlight"])

                if "quote" in book:
                    st.success("Trích dẫn: " + book["quote"])

# ==========================
# RAG SEARCH
# ==========================

def search_books(query):

    results = []

    for book in books:

        text = (
            book["title"] +
            book["description"] +
            book["category"] +
            book["who_should_read"]
        ).lower()

        if any(word in text for word in query.lower().split()):
            results.append(book)

    return results[:3]

# ==========================
# AI CHATBOT
# ==========================

# elif menu == "AI gợi ý sách":

#     st.title("🤖 AI gợi ý sách")

#     user_input = st.text_input(
#         "Bạn muốn đọc sách gì?"
#     )

#     if st.button("Gợi ý sách"):

#         results = search_books(user_input)

#         if results:

#             st.subheader("📚 Sách phù hợp với bạn")

#             for book in results:

#                 st.markdown('<div class="card">', unsafe_allow_html=True)

#                 st.subheader(book["title"])
#                 st.write("✍️", book["author"])
#                 st.write(book["description"])

#                 st.markdown('</div>', unsafe_allow_html=True)

#         else:
#             st.warning("Chưa tìm thấy sách phù hợp.")