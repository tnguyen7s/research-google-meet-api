from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

event = {
    'summary': 'Meeting made from Python code using a Google Calendar API',
    'start': {
        'dateTime': '2023-07-17T15:00:00Z'
    },
    'end': {
        'dateTime': '2023-07-17T16:00:00Z'
    },
    'attendees': [
        {
            'email': 'lamhuynh2207@gmail.com'
        },
        {
            'email': 'dinhhoanganh2001@gmail.com'
        }, 
        {
            'email': 'kietdng2@gmail.com'
        },
        {
            'email': 'truongtrinhkhaidng@gmail.com'
        },
        {
            'email': 'auroranguyen259@gmail.com'
        }, 
        {
            'email': 'pntphamnnguyenthao@gmail.com'
        }
    ]
}

# Get your Google Calendar API credentials.
creds = None
SCOPES = ['https://www.googleapis.com/auth/calendar.events.owned']

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

try:
    # Create the event.
    service = build('calendar', 'v3', credentials=creds)
    service.events().insert(calendarId='primary', body=event, sendNotifications=True).execute()

except HttpError as err:
    print(err)
