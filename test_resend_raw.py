#!/usr/bin/env python3
"""Debug Resend API with raw HTTP request."""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('RESEND_API_KEY')
print(f"API Key: {api_key}")
print()

# Make raw API request
url = "https://api.resend.com/emails"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "from": "onboarding@resend.dev",
    "to": ["cmraad1@gmail.com"],
    "subject": "Test from Awesome Morning",
    "html": "<h1>Test Email</h1><p>This is a test.</p>"
}

print("Sending request to Resend API...")
print(f"URL: {url}")
print(f"Headers: {headers}")
print(f"Data: {json.dumps(data, indent=2)}")
print()

try:
    response = requests.post(url, headers=headers, json=data)

    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Response Content-Type: {response.headers.get('content-type')}")
    print()
    print(f"Raw Response Text:")
    print(response.text)
    print()

    if response.status_code == 200:
        print("✅ SUCCESS!")
        try:
            print(f"JSON Response: {response.json()}")
        except:
            print("Could not parse JSON")
    else:
        print(f"❌ ERROR: Status {response.status_code}")

except Exception as e:
    print(f"❌ Exception: {e}")
    import traceback
    traceback.print_exc()
