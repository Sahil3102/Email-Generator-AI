from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle
import base64
from email.mime.text import MIMEText

SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def save_to_gmail_draft(subject, body):
    service = get_gmail_service()

    message = MIMEText(body)
    message['to'] = ''
    message['from'] = 'me'
    message['subject'] = subject

    create_message = {
        'message': {
            'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
        }
    }
    draft = service.users().drafts().create(userId='me', body=create_message).execute()

    return f"Draft saved (ID: {draft['id']}) ✅"
