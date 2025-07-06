import streamlit as st

st.set_page_config(page_title="English Listening: Aesop's Fables", layout="centered")

st.title("🎧 English Listening Skills — Aesop's Fables")
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
st.write("""
Practice your English listening and comprehension skills with these timeless short stories.
First, do **Passive Listening** — just listen and enjoy.
Then, repeat for **Active Listening** — listen again and answer the questions!
""")

# =======================================
# 1️⃣ The Fox and the Grapes
# =======================================
st.header("1️⃣ The Fox and the Grapes")

st.subheader("🔊 Passive Listening")
st.write("👉 Just listen to the story. Relax, no questions yet.")
st.video("https://www.youtube.com/watch?v=QXkYawJisCE")

st.subheader("🎯 Active Listening")
st.write("👉 Now listen again and answer the question!")

q1 = st.radio(
    "What did the fox want?",
    ["A bunch of grapes", "A piece of meat", "A rabbit"],
    key="q1"
)
if q1:
    if q1 == "A bunch of grapes":
        st.success("✅ Correct! The fox wanted the grapes.")
    else:
        st.error("❌ Not quite. The fox was after the grapes!")

st.divider()

# =======================================
# 2️⃣ The Wolf and the Lamb
# =======================================
st.header("2️⃣ The Wolf and the Lamb")

st.subheader("🔊 Passive Listening")
st.write("👉 Just listen to the story. No questions for now.")
st.video("https://www.youtube.com/watch?v=nQsaT8fJiKA")  # Replace with relevant link if needed

st.subheader("🎯 Active Listening")
st.write("👉 Listen again and test your understanding!")

q2 = st.radio(
    "Who was drinking water downstream?",
    ["The wolf", "The lamb", "The fox"],
    key="q2"
)
if q2:
    if q2 == "The lamb":
        st.success("✅ Correct! The lamb was drinking downstream.")
    else:
        st.error("❌ Not quite. Listen again!")

st.divider()

# =======================================
# 3️⃣ The Crow and the Pitcher
# =======================================
st.header("3️⃣ The Crow and the Pitcher")

st.subheader("🔊 Passive Listening")
st.write("👉 Just watch the story first.")
st.video("https://www.youtube.com/watch?v=XWThl30YD5s")  # Replace if needed

st.subheader("🎯 Active Listening")
st.write("👉 Watch again and answer!")

q3 = st.radio(
    "How did the crow get the water?",
    ["Tipped the pitcher over", "Called for help", "Dropped stones inside"],
    key="q3"
)
if q3:
    if q3 == "Dropped stones inside":
        st.success("✅ Correct! The clever crow dropped stones to raise the water.")
    else:
        st.error("❌ Try again. Think about the crow’s trick!")

st.divider()

# =======================================
# Final result
# =======================================
correct_answers = sum([
    q1 == "A bunch of grapes",
    q2 == "The lamb",
    q3 == "Dropped stones inside"
])

st.write(f"🎉 **You answered {correct_answers} out of 3 correctly! Great job practicing Active Listening!**")

st.info("📚 Audio by public YouTube videos. For educational use only.")
