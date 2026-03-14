from components.header import show_header
from components.navbar import show_navbar

st.set_page_config(page_title="Hiên Chữ", layout="wide", initial_sidebar_state="collapsed")

# 2. Gọi thành phần chung
show_header()
show_navbar()