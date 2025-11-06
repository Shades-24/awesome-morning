#!/usr/bin/env python3
"""Minimal Resend API test."""

import resend
import os
from dotenv import load_dotenv

load_dotenv()

# Get API key
api_key = os.getenv('RESEND_API_KEY')
print(f"API Key loaded: {api_key[:10]}..." if api_key else "API Key: NOT FOUND")

# Set API key
resend.api_key = api_key

# Try a simple email (no attachment)
print("\nTrying to send simple email...")

try:
    params = {
        "from": "onboarding@resend.dev",
        "to": ["cmraad1@gmail.com"],
        "subject": "Test from Awesome Morning",
        "html": "<h1>Test Email</h1><p>This is a test from your morning motivation system.</p>"
    }

    print(f"Sending to: {params['to']}")
    print(f"From: {params['from']}")

    email = resend.Emails.send(params)
    print(f"\n✅ SUCCESS! Email ID: {email.get('id')}")

except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
