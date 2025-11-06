#!/usr/bin/env python3
"""Quick test to verify Resend email is working."""

import config
from email_sender import send_via_resend
from PIL import Image
import os

# Create a simple test image (since video is failing)
print("Creating test image...")
img = Image.new('RGB', (640, 480), color=(73, 109, 137))
test_path = os.path.join(config.OUTPUT_DIR, 'test_image.jpg')
img.save(test_path)
print(f"✓ Test image created: {test_path}")

# Test sending email
print(f"\nTesting email delivery to {config.EMAIL_TO}...")
result = send_via_resend(test_path, config.EMAIL_TO)

if result:
    print("\n" + "=" * 60)
    print("✅ SUCCESS! Email sent via Resend")
    print("=" * 60)
    print(f"\nCheck your inbox at {config.EMAIL_TO}")
    print("If you don't see it, check your spam folder.")
else:
    print("\n" + "=" * 60)
    print("❌ FAILED to send email")
    print("=" * 60)
