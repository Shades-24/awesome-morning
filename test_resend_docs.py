#!/usr/bin/env python3
"""Test Resend using EXACT official documentation pattern."""

import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.environ["RESEND_API_KEY"]

print(f"API Key loaded: {resend.api_key[:15]}...")
print()

# Use EXACT pattern from official docs
print("Sending email using official docs pattern...")

params: resend.Emails.SendParams = {
    "from": "Acme <onboarding@resend.dev>",
    "to": ["cmraad1@gmail.com"],
    "subject": "Morning Motivation Test",
    "html": "<strong>Hello from Awesome Morning!</strong><p>This is a test email.</p>",
}

try:
    email = resend.Emails.send(params)
    print(email)
    print()
    print("=" * 60)
    print("✅ SUCCESS! Email sent!")
    print("=" * 60)
    print(f"Check your inbox at cmraad1@gmail.com")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
