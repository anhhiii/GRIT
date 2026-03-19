import streamlit as st

def display_book_card(book_row):
    with st.container(border=True):
        # Ảnh sách
        img = book_row["img_url"] if book_row["img_url"] else "https://via.placeholder.com/200x320"
        
        # Fixed height for image
        st.markdown(f"""
        <div class="bc-img-wrapper">
            <img src="{img}">
        </div>
        """, unsafe_allow_html=True)

        # Tên sách (fixed height for 2 lines)
        title = book_row["title"]
        st.markdown(f'''
        <div class="bc-title" title="{title}">
            {title}
        </div>
        ''', unsafe_allow_html=True)

        # Tác giả (fixed height for 1 line)
        author = book_row['author']
        st.markdown(f'''
        <div class="bc-author">
            ✍️ {author}
        </div>
        ''', unsafe_allow_html=True)

        # Click card button
        if st.button("📖 Xem chi tiết", key=f"detail_{book_row['id']}", use_container_width=True):
            st.session_state.selected_book_id = int(book_row["id"])
            st.switch_page("pages/book_detail.py")