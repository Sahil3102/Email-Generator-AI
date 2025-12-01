import requests
import streamlit as st

# --- Get API key from secrets
OPENROUTER_API_KEY = st.secrets["openrouter"]["api_key"]

# --- Generate email subject + body

def generate_email(vc_name, firm, focus, vendor_name, offer_desc):
    prompt = f"""
You are an assistant helping a startup founder write personalized outreach emails to venture capitalists.
Generate a professional and persuasive email **subject** and **body** based on the following:

VC Name: {vc_name}
VC Firm: {firm}
Investment Focus: {focus}

Startup Name: {vendor_name}
Startup Offering: {offer_desc}

The email should:
- Have a clear and relevant subject line
- Be friendly, short, and professional
- Mention what the startup does and why the VC might be interested

Return the output as:
Subject: <subject here>
Body:
<body here>
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://yourapp.streamlit.app",
        "X-Title": "AI Email Crafter"
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )

    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        lines = content.split("\n")
        subject = next((l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("subject:")), "")
        body_lines = content.split("Body:", 1)[-1].strip()
        return subject, body_lines
    else:
        return "[Error Generating Subject]", f"[Error] {response.text}"
