import streamlit as st
import pandas as pd
from utils.email_generator import generate_email
from utils.gmail_api import save_to_gmail_draft

st.set_page_config(page_title="Email Generator AI", layout="wide")
st.markdown("<h1 style='font-size:2.2em'>🧾 Email Generator AI</h1><p style='margin-bottom:2rem;'>Effortlessly draft personalized VC outreach emails using AI ✨</p>", unsafe_allow_html=True)

# --- State
if "email_results" not in st.session_state:
    st.session_state.email_results = []

# --- Sidebar
with st.sidebar:
    st.markdown("### 📤 Upload VC List")
    uploaded_file = st.file_uploader("Upload .csv or .xlsx", type=["csv", "xlsx"])
    vendor_name = st.text_input("🏢 Your Company Name", value="Satu Energy")
    vendor_offer = st.text_area("🧠 What are you offering?", value="We're building AI-powered renewable energy systems.")
    generate_button = st.button("✨ Generate Emails")

# --- Load VC data
vc_df = pd.DataFrame()
if uploaded_file:
    vc_df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

# --- Show VC List
if not vc_df.empty:
    st.markdown("### 👥 Uploaded VC List")
    st.dataframe(vc_df, use_container_width=True)

    if generate_button:
        results = []
        for _, row in vc_df.iterrows():
            name = row.get("Name", "")
            firm = row.get("Firm", "")
            focus = row.get("Focus", "")
            subject, body = generate_email(name, firm, focus, vendor_name, vendor_offer)
            results.append({
                "VC Name": name,
                "Firm": firm,
                "Subject": subject,
                "Body": body
            })
        st.session_state.email_results = results

# --- Results
email_df = pd.DataFrame(st.session_state.email_results)
if not email_df.empty:
    st.markdown("## ✉️ Generated Emails")
    st.dataframe(email_df[["VC Name", "Firm", "Subject"]], use_container_width=True)

    st.markdown("### 🔍 Email Preview")
    preview = email_df.iloc[0]
    with st.container():
        st.markdown(f"""
        <div style="padding: 1rem; background-color: #f9f9f9; border-radius: 8px; margin-bottom: 2rem;">
        <p><strong>To:</strong> {preview['VC Name']} ({preview['Firm']})</p>
        <p><strong>Subject:</strong> {preview['Subject']}</p>
        <hr>
        <p style="white-space: pre-wrap;">{preview['Body']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 💾 Save to Gmail Drafts")
    for i, row in email_df.iterrows():
        with st.expander(f"📨 {row['VC Name']} — {row['Firm']}"):
            subject = st.text_input("✉️ Subject", value=row["Subject"], key=f"subject_{i}")
            body = st.text_area("📝 Body", value=row["Body"], key=f"body_{i}", height=150)
            if st.button("Save to Gmail Draft", key=f"save_{i}"):
                response = save_to_gmail_draft(subject, body)
                st.success(response)
else:
    st.info("⬅️ Upload your VC list and generate emails to get started.")
