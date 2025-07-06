import streamlit as st
from fpdf import FPDF

import random

st.title("✍️  Writing Skills Practice")

st.write("""
**Task:** Write a **formal email** to your professor, based on a *random scenario*.  
Use clear, polite language, proper structure, and a professional tone.
""")

# ----------------------------------
# 📌 Random Scenario
# ----------------------------------
scenarios = [
    "Request a meeting to discuss your midterm exam results.",
    "Ask for a recommendation letter for a scholarship.",
    "Request an extension on an assignment due to illness.",
    "Invite your professor to speak at a student seminar.",
    "Clarify doubts about your final project requirements."
]

selected_scenario = random.choice(scenarios)
st.info(f"📌 **Your Scenario:** {selected_scenario}")

# ----------------------------------
# 📌 Useful Formal Phrases
# ----------------------------------
with st.expander("💡 Useful Formal Phrases"):
    st.write("""
- I hope this email finds you well.
- I am writing to request...
- I would greatly appreciate your assistance...
- I am available on [days/times]...
- Thank you for your time and consideration.
- I look forward to your response.
""")

# ----------------------------------
# 📌 Fun Fact
# ----------------------------------
with st.expander("💡 Fun Fact"):
    st.write("Did you know? 'Best regards' and 'Sincerely' are among the most professional closings in academic emails.")

# ----------------------------------
# 📌 Email Form
# ----------------------------------
subject = st.text_input("📌 Email Subject:", placeholder="E.g., Request for Meeting")

email_body = st.text_area("✉️ Write your email body here:", height=200)

# ----------------------------------
# ✅ Submit + Feedback
# ----------------------------------
if st.button("✅ Submit Email"):
    feedback = []
    score = 0

    if any(word in subject.lower() for word in ["request", "meeting", "recommendation", "extension", "invite", "clarify"]):
        score += 1
    else:
        feedback.append("🔹 Subject: Try to include a clear action word like 'request', 'invite', or 'clarify'.")

    if any(greet in email_body.lower() for greet in ["dear professor", "dear dr", "dear sir", "dear madam"]):
        score += 1
    else:
        feedback.append("🔹 Greeting: Add a polite greeting like 'Dear Professor...'.")

    if "meeting" in email_body.lower() or "letter" in email_body.lower() or "extension" in email_body.lower() or "invite" in email_body.lower() or "clarify" in email_body.lower():
        score += 1
    else:
        feedback.append("🔹 Purpose: Clearly mention the reason for your email.")

    if "regards" in email_body.lower() or "sincerely" in email_body.lower():
        score += 1
    else:
        feedback.append("🔹 Closing: End with 'Regards', 'Sincerely', or a similar sign-off.")

    st.success(f"✅ You covered {score}/4 key elements.")

    if feedback:
        st.info("\n".join(feedback))

# ----------------------------------
# 📌 Model Answer
# ----------------------------------
with st.expander("💡 Show Example Email"):
    st.markdown(f"""
**Subject:** Request to Discuss Midterm Exam Results

**Body:**  
Dear Professor [Last Name],

I hope this email finds you well.  
I am writing to request a meeting to discuss my performance on the recent midterm exam.  
I would greatly appreciate your feedback and guidance on how I can improve.

Could we please schedule a time to meet next week? I am available on Tuesday or Thursday afternoon, but I am happy to adjust to your availability.

Thank you very much for your time and support.

Best regards,  
[Your Name]
""")

# ----------------------------------
# 📄 PDF Download
# ----------------------------------
if st.button("📥 Download My Email as PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Formal Email Writing Practice", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Scenario: {selected_scenario}", ln=True)
    pdf.cell(200, 10, txt=f"Subject: {subject}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Body:\n{email_body}")

    pdf_file = "my_formal_email.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as f:
        st.download_button(
            label="📄 Click to Download PDF",
            data=f,
            file_name=pdf_file,
            mime="application/pdf"
        )
