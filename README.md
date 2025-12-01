📧 Email Generator AI

AI-powered tool that generates customized outreach emails for investors and saves them directly to your Gmail drafts.
Built with Streamlit, OpenRouter, and Gmail API.

🚀 Overview

Email Generator AI takes a list of investors and automatically creates personalized, high-quality outreach emails. You can review, edit, and save them to Gmail Drafts with a single click.

This helps founders, sales teams, and professionals reach out to investors or leads faster and more professionally.

🧠 Features
✔️ Upload Investor Dataset

Supports .csv and .xlsx files containing fields such as:
Investor Name
Company / Firm
Domain / Investment Focus
Location (optional)
✔️ AI-Powered Email Generation
Uses OpenRouter LLMs to automatically generate:
Subject lines
Personalized email bodies
Call-to-action statements
Clean, structured formatting
✔️ In-App Editing
Preview email drafts inside the app
Modify content before saving
✔️ Save to Gmail Drafts
Uses Gmail OAuth 2.0 to securely store:
Draft messages (no auto-sending)
OAuth token saved in token.pickle

Email_Generator_AI/
│── app.py                     # Main Streamlit UI 
│── credentials.json           # Gmail OAuth client (added manually)
│── requirements.txt           # Required dependencies
│── token.pickle               # OAuth token (auto-created)
│── README.md                  # This file
│
├── .streamlit/
│    └── secrets.toml          # OpenRouter API key
│
├── utils/
│    ├── __init__.py
│    ├── email_generator.py    # AI generation logic (OpenRouter)
│    ├── gmail_api.py          # Gmail Draft creation
│
└── sample_dataset/
     └── investors_sample.csv  # Example input file

🧠 Tech Stack

Streamlit (Frontend UI)
OpenRouter LLMs (Email generation)
Gmail API (Draft creation)
Python 3.10+
Pandas (Data handling)

⭐ Use Cases
VC & Angel Investor Outreach
Sales Email Automation
Cold Email Personalization
Fundraising Communication
Business Development Workflows
