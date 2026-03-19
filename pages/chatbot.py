import streamlit as st
from services.chat_service import chat_with_recommendation
from components.header import show_header
from components.navbar import show_navbar

st.set_page_config(page_title="Hiên Chữ - Trợ lý AI", page_icon="✨", layout="wide", initial_sidebar_state="collapsed")

show_header()
show_navbar(active_page="chatbot")

from utils.css import load_css

# CSS Customization for Chatbot Page
load_css("assets/css/chatbot.css")

# Chat Hero Section
st.markdown("""
<div class="chat-hero">
    <h1 class="chat-title">Trợ lý AI <span>Hiên Chữ</span></h1>
    <p class="chat-subtitle">Hỏi bất cứ điều gì về thế giới sách. Trợ lý AI sẽ giúp bạn tìm kiếm, tóm tắt và đưa ra những gợi ý phù hợp nhất với sở thích của bạn.</p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Empty State Helpers
if len(st.session_state.messages) == 0:
    st.markdown("<div style='text-align:center; font-family:\"Inter\", sans-serif; color:#8c8279; margin-bottom:1.5rem;'>Bắt đầu trò chuyện với một trong các gợi ý dưới đây:</div>", unsafe_allow_html=True)
    cols = st.columns([1,1,1], gap="medium")
    with cols[0]:
        st.markdown("""
        <div class="suggestion-card">
            <div class="suggestion-title">💡 Gợi ý cảm hứng</div>
            <div class="suggestion-text">Mình muốn tìm một cuốn tiểu thuyết lãng mạn nhẹ nhàng cho cuối tuần.</div>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="suggestion-card">
            <div class="suggestion-title">💡 Hiểu sâu tác phẩm</div>
            <div class="suggestion-text">Bạn có thể tóm tắt ngắn gọn nội dung triết lý trong cuốn 'Đắc Nhân Tâm' không?</div>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="suggestion-card">
            <div class="suggestion-title">💡 Khám phá thể loại mới</div>
            <div class="suggestion-text">Nêu 3 cuốn sách khoa học viễn tưởng đáng đọc nhất cho người mới bắt đầu.</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

# Hiển thị lịch sử chat
for msg in st.session_state.messages:
    # customize avatar based on role
    avatar = "👤" if msg["role"] == "user" else "✨"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# Input
if prompt := st.chat_input("Bạn đang tìm cuốn sách nào?"):
    # User
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Loading 
    with st.chat_message("assistant", avatar="✨"):
        message_placeholder = st.empty()
        with st.spinner("AI đang tìm kiếm thư viện và suy nghĩ... 📚"):
            response = chat_with_recommendation(prompt)
        message_placeholder.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("<br><br><br>", unsafe_allow_html=True)
