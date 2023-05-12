import os
import pickle
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up API key and service account credentials
API_KEY = 'Your API key'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'path_to_credentials_file.json'
SPREADSHEET_ID = 'Your Sheets File'

# Load saved credentials
if os.path.exists(SERVICE_ACCOUNT_FILE):
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
else:
    raise Exception("Service account credentials file not found at: {}".format(SERVICE_ACCOUNT_FILE))

# Authorize client
authorized = False
while not authorized:
    try:
        creds.flow_static_credentials(API_KEY, SCOPES)
        authorized = True
    except Exception as e:
        print("Error authorizing client: {}".format(e))
        input("Press Enter to retry...")

# Connect to Google Sheets API
service = build('sheets', 'v4', credentials=creds)

def save_memory(title, content):
    # Save memory to Google Sheet
    range_name = f"A{len(service.spreadsheets().values().get(spreadsheetId=SPRID).get('values'))}"
    body = {'values': [{'userEnteredValue': {'stringValue': title}, 'range': range_name}}]
    service.spreadsheets().values().update(spreadsheetId=SPRID, range=f"{range_name}!A1", valueInputOption='RAW', body=body).execute()

def load_memories():
    # Load memories from Google Sheet
    response = service.spreadsheets().values().get(spreadsheetId=SPRID, range="A:A").execute()
    values = response['values']
    memories = []
    for row in values:
        if row['userEnteredValue'] is not None:
            memories.append({'title': row['userEnteredValue']['stringValue'], 'content': row['userEnteredValue']['stringValue']})
    return memories

def clear_memories():
    # Clear all memories from Google Sheet
    range_name = "A:A"
    service.spreadsheets().values().batch_update(spreadsheetId=SPRID, body={'valueInputOption': 'RAW', 'requests': [{
            'insertDimension': {
                'position': 0,
                'size': {
                    'width': 1,
                    'height': 1,
                },
                'location': {
                    'rowIndex': 0,
                    'columnIndex': 0,
                }
            },
            'valueInputOption': 'RAW',
            'values': [''] * len(service.spreadsheets().values().get(spreadsheetId=SPRID).get('values'))
        }])
