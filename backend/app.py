from flask import Flask, request, jsonify, redirect, session
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauthlib.oauth2 import WebApplicationClient
import os
import re
import pickle
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.secret_key = os.urandom(24)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

CREDENTIALS_PATH = 'credentials.json'

@app.route('/login')
def login():
    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_PATH, SCOPES
    )
    
    credentials = flow.run_local_server(port=5001)
    
    # Save credentials for later use
    with open('token.pickle', 'wb') as token:
        pickle.dump(credentials, token)

    return redirect('/emails')

@app.route('/oauth2callback')  # This route is required for handling the callback
def oauth2callback():
    

    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_PATH, SCOPES
    )
    credentials = flow.fetch_token(authorization_response=request.url)

    # Save credentials for later use
    with open('token.pickle', 'wb') as token:
        pickle.dump(credentials, token)

    return redirect('/emails')

@app.route('/emails')
def get_emails():
    try:
        # Load saved credentials
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

        # Create Gmail API client
        service = build('gmail', 'v1', credentials=credentials)
        
        # List messages
        results = service.users().messages().list(userId='me').execute()
        messages = results.get('messages', [])

        
        email_count_dict = {}
        for msg in messages:
            msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
            
            headers = msg_detail['payload']['headers']
            sender = next(header['value'] for header in headers if header['name'] == 'From')
            email_address = re.search(r'<(.+)>', sender).group(1)
            
                
            
            if email_address in email_count_dict:
                email_count_dict[email_address] += 1
            else:
                email_count_dict[email_address] = 1

        email_count_data = []
        for email_address in email_count_dict:
            email = {
                "address": email_address,
                "count": email_count_dict[email_address]
            }
            email_count_data.append(email)
            
        return jsonify(email_count_data)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)})


    
@app.route('/top-emails', methods=['GET'])
def get_top_emails():
    sample_data = {
        "top_emails": [
            {"email": "newsletter@xyz.com", "count": 45},
            {"email": "alerts@bank.com", "count": 30},
            {"email": "promo@store.com", "count": 20}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000, ssl_context=('cert.crt', 'cert.key'))
