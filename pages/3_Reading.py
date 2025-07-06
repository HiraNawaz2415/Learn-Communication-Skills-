import streamlit as st
from fpdf import FPDF


st.title("📖 Reading Skills Practice")
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
st.header("SQ3R Reading Practice")

st.write("""
**SQ3R** helps you read actively and understand deeply.  
Complete each step and download your answers as a PDF!
""")

# ------------------------------
# 📚 Passages
# ------------------------------
passages = {
    "Intercultural Communication": """
In an increasingly interconnected world, the ability to communicate effectively 
across cultures has become an essential skill. Beyond linguistic proficiency, 
intercultural communication requires an understanding of social norms, 
values, and non-verbal behaviors that differ from one culture to another. 
By developing cultural awareness and empathy, individuals can navigate 
complex interactions, avoid misunderstandings, and build stronger 
relationships both personally and professionally.
""",
    "Renewable Energy": """
Renewable energy sources like solar, wind, and hydro power are vital 
for a sustainable future. Unlike fossil fuels, renewables do not emit 
harmful greenhouse gases and can help combat climate change. 
Investing in renewable energy also creates jobs, reduces dependence 
on imported fuels, and promotes economic growth in local communities.
""",
    "Artificial Intelligence": """
Artificial Intelligence (AI) is transforming industries by automating tasks 
and analyzing large amounts of data faster than humans can. While AI brings 
efficiency and innovation, it also raises concerns about job displacement, 
privacy, and ethical decision-making. Balancing AI’s benefits with 
responsible use is a major challenge for societies worldwide.
""",
    "Climate Change Adaptation": """
Climate change adaptation involves adjusting human and natural systems 
in response to the effects of climate change. Unlike mitigation, which 
focuses on reducing greenhouse gas emissions, adaptation aims to minimize 
the damage caused by rising temperatures, extreme weather, and sea-level rise. 
Effective adaptation strategies include building resilient infrastructure, 
protecting ecosystems, and supporting vulnerable communities.
""",
    "Healthy Lifestyles": """
Maintaining a healthy lifestyle involves more than just eating nutritious food. 
It also requires regular physical activity, sufficient sleep, and effective 
stress management. By adopting healthy habits, individuals can improve 
their physical and mental well-being, reduce the risk of chronic diseases, 
and enhance their overall quality of life.
"""
}

selected_passage = st.selectbox(
    "📚 **Choose a Passage to Practice:**",
    list(passages.keys())
)

st.markdown("### 📄 Passage")
st.write(passages[selected_passage])

# ------------------------------
# SQ3R Steps
# ------------------------------
survey = st.text_area("🔍 **1. Survey:** Quickly skim and note your first impressions.", height=80)
question = st.text_area("❓ **2. Question:** Write questions you want answered.", height=80)
read = st.text_area("📖 **3. Read:** Take notes while reading.", height=80)
recite = st.text_area("🗣️ **4. Recite:** Close the passage and write in your own words.", height=80)
review = st.text_area("🔄 **5. Review:** Final key ideas to remember.", height=80)

# ------------------------------
# ✅ Submit + Feedback
# ------------------------------
if st.button("✅ Submit and Check"):
    score = 0
    feedback = []

    if any(word in survey.lower() for word in ["culture", "renewable", "ai", "climate", "health"]):
        score += 1
    else:
        feedback.append("🔹 Survey: Try to mention the main topic!")

    if "how" in question.lower() or "why" in question.lower():
        score += 1
    else:
        feedback.append("🔹 Question: Use 'how' or 'why' to make deeper questions.")

    if len(read.strip()) > 10:
        score += 1
    else:
        feedback.append("🔹 Read: Add more notes while reading!")

    if len(recite.strip()) > 10:
        score += 1
    else:
        feedback.append("🔹 Recite: Try to explain it fully in your own words!")

    if len(review.strip()) > 10:
        score += 1
    else:
        feedback.append("🔹 Review: Add a clear final summary!")

    st.success(f"✅ You completed SQ3R with {score}/5 steps strong!")

    if feedback:
        st.info("\n".join(feedback))

# ------------------------------
# 📄 Model Answers (for each)
# ------------------------------
st.markdown("## 💡 Model Answers")

if selected_passage == "Intercultural Communication":
    st.markdown("**1️⃣ Survey:** Communication across cultures.")
    st.markdown("**2️⃣ Question:** How does cultural awareness help communication?")
    st.markdown("**3️⃣ Read:** Social norms, values, non-verbal cues, empathy.")
    st.markdown("**4️⃣ Recite:** It means understanding differences to communicate well.")
    st.markdown("**5️⃣ Review:** Awareness, empathy, building better relationships.")

elif selected_passage == "Renewable Energy":
    st.markdown("**1️⃣ Survey:** Clean energy sources.")
    st.markdown("**2️⃣ Question:** Why are renewables better than fossil fuels?")
    st.markdown("**3️⃣ Read:** No greenhouse gases, local jobs, sustainability.")
    st.markdown("**4️⃣ Recite:** Renewable energy helps fight climate change.")
    st.markdown("**5️⃣ Review:** Sustainability, less pollution, more jobs.")

elif selected_passage == "Artificial Intelligence":
    st.markdown("**1️⃣ Survey:** Technology that automates tasks.")
    st.markdown("**2️⃣ Question:** What are the benefits and risks of AI?")
    st.markdown("**3️⃣ Read:** Efficiency, innovation, ethical concerns.")
    st.markdown("**4️⃣ Recite:** AI can help but also creates challenges.")
    st.markdown("**5️⃣ Review:** Benefits must be balanced with responsibility.")

elif selected_passage == "Climate Change Adaptation":
    st.markdown("**1️⃣ Survey:** Dealing with climate impacts.")
    st.markdown("**2️⃣ Question:** How does adaptation differ from mitigation?")
    st.markdown("**3️⃣ Read:** Resilient infrastructure, protecting ecosystems.")
    st.markdown("**4️⃣ Recite:** Adaptation reduces harm from climate impacts.")
    st.markdown("**5️⃣ Review:** Strategies help communities cope with change.")

elif selected_passage == "Healthy Lifestyles":
    st.markdown("**1️⃣ Survey:** Living well and staying healthy.")
    st.markdown("**2️⃣ Question:** What habits improve overall well-being?")
    st.markdown("**3️⃣ Read:** Nutrition, exercise, sleep, stress management.")
    st.markdown("**4️⃣ Recite:** Good habits mean better physical and mental health.")
    st.markdown("**5️⃣ Review:** Healthy choices prevent diseases and improve life.")

# ------------------------------
# 📄 Download as PDF
# ------------------------------
if st.button("📥 Download My SQ3R PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="SQ3R Reading Practice", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Passage: {selected_passage}", ln=True)

    pdf.multi_cell(0, 10, txt=f"1. Survey:\n{survey}\n")
    pdf.multi_cell(0, 10, txt=f"2. Question:\n{question}\n")
    pdf.multi_cell(0, 10, txt=f"3. Read:\n{read}\n")
    pdf.multi_cell(0, 10, txt=f"4. Recite:\n{recite}\n")
    pdf.multi_cell(0, 10, txt=f"5. Review:\n{review}\n")

    pdf_file = "sq3r_answers.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as f:
        st.download_button(
            label="📄 Click to Download PDF",
            data=f,
            file_name=pdf_file,
            mime="application/pdf"
        )
