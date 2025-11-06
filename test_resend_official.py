#!/usr/bin/env python3
"""Test Resend using official SDK patterns."""

import resend
import os
from dotenv import load_dotenv

load_dotenv()

# Set API key exactly as docs show
resend.api_key = os.getenv('RESEND_API_KEY')

print(f"API Key: {resend.api_key[:15]}...")
print()

# Test 1: List API keys (to verify auth works)
print("Test 1: Listing API keys...")
try:
    keys = resend.ApiKeys.list()
    print(f"✅ Success! Found {len(keys.get('data', []))} API keys")
    print(f"   Response: {keys}")
except Exception as e:
    print(f"❌ Failed: {e}")
print()

# Test 2: Send email from onboarding domain
print("Test 2: Sending from onboarding@resend.dev...")
try:
    params = {
        "from": "onboarding@resend.dev",
        "to": ["cmraad1@gmail.com"],
        "subject": "Test from Awesome Morning",
        "html": "<h1>Hello!</h1><p>This is a test from your morning motivation system.</p>",
    }

    email = resend.Emails.send(params)
    print(f"✅ Success! Email ID: {email.get('id')}")
    print(f"   Full response: {email}")
except Exception as e:
    print(f"❌ Failed: {e}")
    import traceback
    traceback.print_exc()
print()

# Test 3: Send from your verified domain
print("Test 3: Sending from orders.planflowers.com.au...")
try:
    params = {
        "from": "morning@orders.planflowers.com.au",
        "to": ["cmraad1@gmail.com"],
        "subject": "Morning Motivation Test",
        "html": "<h1>Good Morning!</h1><p>Testing from your verified domain.</p>",
    }

    email = resend.Emails.send(params)
    print(f"✅ Success! Email ID: {email.get('id')}")
    print(f"   Full response: {email}")
except Exception as e:
    print(f"❌ Failed: {e}")
    import traceback
    traceback.print_exc()
print()

# Test 4: List domains
print("Test 4: Listing domains...")
try:
    domains = resend.Domains.list()
    print(f"✅ Success!")
    print(f"   Domains: {domains}")
except Exception as e:
    print(f"❌ Failed: {e}")
