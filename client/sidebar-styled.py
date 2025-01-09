import streamlit as st
from datetime import datetime


def sidebar():
    st.sidebar.title("Navigation")
    router = st.sidebar.radio("Go to", ["Home", "ETL"])

    # Set page config
    

    # Custom CSS for styling
    st.html("""
        <style>
        /* Sidebar styling */
        .stSidebar {
            background-color: #2E303E;
        }

        /* Navigation link styling */
        .nav-link {
            padding: 0.5rem 0;
            color: #FFFFFF;
            text-decoration: none;
            display: block;
            transition: background-color 0.2s;
        }
        .nav-link:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        /* Title styling */
        .sidebar-title {
            color: #FFFFFF;
            opacity: 0.7;
            padding: 1rem 0;
            margin-bottom: 1rem;
        }
        
        /* Feedback buttons styling */
        .feedback-button {
            background: transparent;
            border: none;
            color: #FFFFFF;
            cursor: pointer;
            font-size: 1.2rem;
            padding: 0.5rem;
        }
        </style>
    """)

    # Sidebar title
    st.sidebar.html("<h2 class='sidebar-title'>State of LLM Apps 2023</h2>")

    # Navigation items
    nav_items = [
        ("💡", "Key takeaways"),
        ("📝", "App and developer growth"),
        ("📊", "LLMs adoption at-a-glance"),
        ("📊", "Top models"),
        ("📊", "Top orchestration tools"),
        ("📊", "Top vector retrieval tools"),
        ("💬", "Are chatbots the future?"),
        ("✨", "Gallery of LLM apps"),
        ("😕", "Concerns building with LLMs"),
        ("🏗️", "LLM app architecture"),
        ("❓", "About Streamlit"),
        ("🛠️", "Methodology")
    ]

    # Create navigation links
    for emoji, title in nav_items:
        st.sidebar.markdown(
            f"<a href='#' class='nav-link'>{emoji} {title}</a>",
            unsafe_allow_html=True
        )

    # Add separator before feedback section
    st.sidebar.markdown("<hr style='margin: 2rem 0; opacity: 0.2;'>", unsafe_allow_html=True)

    # Feedback section
    st.sidebar.markdown("<p style='color: #FFA500;'>How do you like this app?</p>", unsafe_allow_html=True)
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.markdown("<button class='feedback-button'>👍</button>", unsafe_allow_html=True)
    with col2:
        st.markdown("<button class='feedback-button'>👎</button>", unsafe_allow_html=True)

    # Last updated date
    st.sidebar.markdown("<hr style='margin: 2rem 0; opacity: 0.2;'>", unsafe_allow_html=True)
    st.sidebar.markdown(
        f"<p style='color: #808080; font-size: 0.8rem;'>Last updated January 01, 2024</p>",
        unsafe_allow_html=True
    )

    # Main content area placeholder
    st.markdown("## Select a section from the sidebar")

    return router