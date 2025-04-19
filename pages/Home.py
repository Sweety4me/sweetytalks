# pages/Home.py
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", page_title="SweetyTalks")

# Load custom CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <div class="logo">❤️ SweetyTalks</div>
    <div class="menu">
        <input type="text" placeholder="Search...">
    </div>
</div>
""", unsafe_allow_html=True)

# Tabs Navigation
selected_tab = option_menu(
    menu_title=None,
    options=["🌍 World", "🎬 Entertainment", "⚽ Sports", "💻 Tech", "💼 Business", "🍲 Food"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#111"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {"color": "white", "font-size": "16px", "text-align": "center", "margin": "0 10px"},
        "nav-link-selected": {"background-color": "#ff3399"},
    }
)

# Trending Section
st.markdown("### 🔥 Trending Now")
cols = st.columns(3)
with cols[0]:
    st.image("https://source.unsplash.com/400x250/?breaking-news", use_column_width=True)
    st.markdown("**Global Heatwave Update!**")
with cols[1]:
    st.image("https://source.unsplash.com/400x250/?bollywood", use_column_width=True)
    st.markdown("**Top 5 Movies That Broke Records**")
with cols[2]:
    st.image("https://source.unsplash.com/400x250/?technology", use_column_width=True)
    st.markdown("**New AI Shocking Breakthrough!**")

st.markdown("---")
st.info("Click tabs above to explore categories, more coming soon!")

