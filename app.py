import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Aashna | Portfolio",
    layout="wide"
)

html_file = Path(__file__).parent / "portfolio.html"

if html_file.exists():
    html_code = html_file.read_text(encoding="utf-8")
    components.html(
        html_code,
        height=2000,
        scrolling=True
    )
else:
    st.error("Portfolio HTML file not found!")
