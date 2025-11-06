#!/usr/bin/env python3
"""Check Resend domains using official docs pattern."""

import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv('RESEND_API_KEY')

print("Checking Resend Setup...")
print(f"API Key: {resend.api_key[:15]}...")
print()

# List domains
print("Listing domains...")
try:
    domains = resend.Domains.list()
    print(f"✅ Success!")
    print(f"Response: {domains}")

    if isinstance(domains, dict) and 'data' in domains:
        domain_list = domains['data']
        print(f"\nFound {len(domain_list)} domain(s):")
        for domain in domain_list:
            print(f"  - {domain.get('name')}")
            print(f"    ID: {domain.get('id')}")
            print(f"    Status: {domain.get('status')}")
            print(f"    Region: {domain.get('region')}")
            print()
except Exception as e:
    print(f"❌ Failed: {e}")
    print()
    print("This suggests the API key doesn't have permission to access Resend.")
    print()
    print("Since you have a paid account, please check:")
    print("1. Is this API key created in the correct Resend account/workspace?")
    print("2. Does the API key have 'Full Access' or 'Sending Access' permissions?")
    print("3. Are there any IP restrictions on the API key?")
    print("4. Try deleting and recreating the API key with full permissions")
