import streamlit as st
import os

def load_css(file_name):
    """
    Load a local CSS file and inject it into the Streamlit app.
    file_name should be relative to the application root, e.g., 'assets/css/global.css'
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Cannot find CSS file at: {file_path}")
    except Exception as e:
        st.error(f"Error loading CSS: {e}")
