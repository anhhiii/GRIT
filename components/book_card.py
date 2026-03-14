import streamlit as st

def display_book_card(book_row):

    with st.container(border=True):

        # Ảnh sách
        img = book_row["img_url"] if book_row["img_url"] else "https://via.placeholder.com/200x300"

        st.image(img, use_container_width=True)

        # Tên sách
        title = book_row["title"]
        if len(title) > 40:
            title = title[:40] + "..."

        st.markdown(f"**{title}**")

        # Tác giả
        st.caption(f"✍️ {book_row['author']}")

        # Click card
        if st.button("Xem chi tiết", key=f"detail_{book_row['id']}", use_container_width=True):
            st.session_state.selected_book_id = int(book_row["id"])
            st.switch_page("pages/book_detail.py")