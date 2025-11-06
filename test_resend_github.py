#!/usr/bin/env python3
"""Test using exact GitHub README example."""

import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.environ["RESEND_API_KEY"]

print(f"API Key: {resend.api_key[:15]}...")
print()

# Exact example from GitHub README
params: resend.Emails.SendParams = {
    "from": "onboarding@resend.dev",
    "to": ["cmraad1@gmail.com"],
    "subject": "hi",
    "html": "<strong>hello, world!</strong>",
}

print("Sending email using exact GitHub README pattern...")
try:
    email: resend.Emails.SendResponse = resend.Emails.send(params)
    print(email)
    print()
    print("=" * 60)
    print("✅ SUCCESS! Email sent to cmraad1@gmail.com")
    print("=" * 60)
    print("Check your inbox!")
except Exception as e:
    print(f"❌ Error: {e}")
    print()
    print("Since your API key has full permissions, this is likely:")
    print("1. IP blocking - Resend blocking requests from this server's IP")
    print("2. Regional restriction - Server region not allowed")
    print("3. Rate limiting - Too many failed attempts")
    print()
    print("Solution: Contact Resend support at support@resend.com")
    print("Tell them: 'Paid account getting 403 on all API calls'")
