import streamlit as st

st.set_page_config(
    page_title="Communication Skills Course",
    page_icon="🗣️",
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    /* Main title styling */
    .big-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: linear-gradient(135deg, #4b4b4b 0%, #bdbdbd 100%);
    }

    /* Subtitle styling */
    .subtitle {
        font-size: 1.2rem;
        color: #555;
    }

    /* Footer styling */
    .footer {
        font-size: 0.8rem;
        color: #888;
        text-align: center;
        margin-top: 50px;
    }

    /* Sidebar gradient background */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #4b4b4b 0%, #bdbdbd 100%);
        color: white
    }

    /* Optional: make sidebar text white */
    [data-testid="stSidebar"] * {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header with Logo and Title ---
col1, col2 = st.columns([1, 5])

with col1:
    st.image("assets/logo.png", width=100)

with col2:
    st.markdown('<div class="big-title">🗣️ Communication Skills Course</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Master listening, speaking, reading, writing, and presentation skills in one place.</div>', unsafe_allow_html=True)

st.write("---")

# --- Main Content ---
st.header("🚀 Start Learning")

st.write("""
Welcome to your professional **Communication Skills App**!  
Use the sidebar to navigate through each module:
- **🎧 Listening Skills**
- **🗣️ Speaking Skills**
- **📚 Reading Skills**
- **✍️ Writing Skills**
- **🎤 Presentation Skills**

Track your progress and become a confident communicator!
""")

st.success("💡 Tip: Complete all modules to earn your Communication Skills Certificate.")

# --- Optional: Replace with a communication-themed banner ---
st.image("https://images.unsplash.com/photo-1588702547923-7093a6c3ba33?fit=crop&w=1200", use_column_width=True)

# --- Footer ---
st.markdown('<div class="footer">© 2025 Your Name or Organization — Communication Skills App</div>', unsafe_allow_html=True)
