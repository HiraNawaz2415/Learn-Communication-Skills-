import streamlit as st
from fpdf import FPDF
import requests
from transformers import pipeline
import os

st.set_page_config(page_title="🎤 Presentation Practice Hub", layout="wide")

st.title("🎤 Presentation Skills Practice — Multi-Mode")
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
Select your practice **mode** and complete each section below.
Write your reflections, check your preparation, and download your notes as a PDF!
""")

# --------------------------
# Select Mode
# --------------------------
mode = st.selectbox(
    "🗂️ **Choose Practice Mode:**",
    ["Public Speaking", "Online Presentation", "Academic Talk", "Interview Pitch"]
)

# --------------------------
# Video + Prompts
# --------------------------
if mode == "Public Speaking":
    st.subheader("📢 Public Speaking Practice")
    st.video("https://www.youtube.com/watch?v=ZXsQAXx_ao0")  # Example: TED Talk tips
    st.markdown("""
**Tips:** Focus on stage presence, voice projection, eye contact, gestures.
""")
    points = st.text_area("💡 **What 3 key points did you learn?**", height=150)
    checklist = [
        "Make strong eye contact",
        "Use open body language",
        "Speak clearly and project your voice",
        "Engage the audience with questions"
    ]

elif mode == "Online Presentation":
    st.subheader("💻 Online Presentation Practice")
    st.video("https://www.youtube.com/embed/18uDutylDa4")

    st.markdown("""
**Tips:** Focus on screen presence, clear slides, managing tech, speaking naturally online.
""")
    points = st.text_area("💡 **What 3 key points did you learn?**", height=150)
    checklist = [
        "Check audio and camera quality",
        "Share screen effectively",
        "Look at the camera",
        "Speak at a steady pace"
    ]

elif mode == "Academic Talk":
    st.subheader("🎓 Academic Presentation Practice")
    st.video("https://www.youtube.com/embed/HAnw168huqA")  # Example: How to give an academic presentation
    st.markdown("""
**Tips:** Focus on structure, research clarity, slides design, answering questions.
""")
    points = st.text_area("💡 **What 3 key points did you learn?**", height=150)
    checklist = [
        "Start with clear research question",
        "Use clear, simple slides",
        "Explain key results confidently",
        "Prepare for audience questions"
    ]

elif mode == "Interview Pitch":
    st.subheader("💼 Interview Pitch Practice")
    st.video("https://www.youtube.com/watch?v=sfbobc0oAu8")
    st.markdown("""
**Tips:** Focus on clear self-introduction, relevant examples, confident delivery.
""")
    points = st.text_area("💡 **What 3 key points did you learn?**", height=150)
    checklist = [
        "Introduce yourself confidently",
        "Highlight key skills and examples",
        "Speak naturally and clearly",
        "End with a positive closing"
    ]

# --------------------------
# Checklist
# --------------------------
st.markdown("### ✅ Self-Checklist")
checks = []
for item in checklist:
    checked = st.checkbox(item)
    checks.append(f"[{'x' if checked else ' '}] {item}")

# --------------------------
# PDF Export
# --------------------------
if st.button("📥 Download My Practice Notes as PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Presentation Practice Notes", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Mode: {mode}", ln=True)

    pdf.multi_cell(0, 10, txt=f"Key Points Learned:\n{points}\n")
    pdf.cell(200, 10, txt="Self-Checklist:", ln=True)
    for line in checks:
        pdf.cell(200, 10, txt=line, ln=True)

    pdf_file = "presentation_practice.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as f:
        st.download_button(
            label="📄 Click to Download PDF",
            data=f,
            file_name=pdf_file,
            mime="application/pdf"
        )

st.success("✅ Keep practicing — confident presenters inspire audiences!")


