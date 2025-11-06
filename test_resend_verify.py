#!/usr/bin/env python3
"""Verify Resend account status."""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('RESEND_API_KEY')

print("Testing Resend Account...")
print(f"API Key: {api_key[:15]}...")
print()

# Try to get API key info
print("1. Checking API key validity...")
url = "https://api.resend.com/api-keys"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(f"   Status: {response.status_code}")
print(f"   Response: {response.text[:200]}")
print()

# Try to get domains
print("2. Checking domains...")
url = "https://api.resend.com/domains"
response = requests.get(url, headers=headers)
print(f"   Status: {response.status_code}")
print(f"   Response: {response.text[:200]}")
print()

# Check emails sent
print("3. Checking recent emails...")
url = "https://api.resend.com/emails"
response = requests.get(url, headers=headers)
print(f"   Status: {response.status_code}")
print(f"   Response: {response.text[:200]}")
print()

print("=" * 60)
if response.status_code == 403:
    print("⚠️  ACCOUNT ACCESS ISSUE")
    print()
    print("Your Resend account has access restrictions.")
    print()
    print("Please check your Resend dashboard:")
    print("1. Go to https://resend.com/")
    print("2. Check for any warnings or alerts")
    print("3. Verify your email is confirmed")
    print("4. Check if your account is in trial/restricted mode")
    print("5. Look for any verification steps needed")
