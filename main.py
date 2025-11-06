#!/usr/bin/env python3
"""
Awesome Morning - Daily motivation video generator and sender.

This script generates a personalized morning motivation video with:
- AI-generated motivational message
- Your daily agenda
- Catholic prayer
- Text-to-speech narration

The video is emailed to you every morning at 7 AM.
"""

import os
import sys
from datetime import datetime

# Import our modules
import config
from ai_generator import generate_motivation
from prayer_manager import get_daily_prayer
from agenda_manager import load_agenda, format_agenda_for_video, clear_agenda
from audio_generator import create_morning_audio
from video_generator import create_video
from email_sender import send_email_with_video

def generate_and_send_morning_video():
    """Main function to generate and send the morning video."""
    print("=" * 60)
    print("AWESOME MORNING - Generating your daily motivation video")
    print("=" * 60)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    try:
        # Step 1: Generate motivation
        print("1. Generating motivational message...")
        motivation = generate_motivation()
        print(f"   ✓ Motivation: {motivation[:60]}...")
        print()

        # Step 2: Load agenda
        print("2. Loading your agenda...")
        agenda_raw = load_agenda()
        agenda_text = format_agenda_for_video(agenda_raw)
        if agenda_raw:
            print(f"   ✓ Agenda loaded")
        else:
            print(f"   ℹ No agenda set (you can set it with: python set_agenda.py)")
        print()

        # Step 3: Get prayer
        print("3. Selecting Catholic prayer...")
        prayer = get_daily_prayer()
        print(f"   ✓ Prayer: {prayer['name']}")
        print()

        # Step 4: Generate audio
        print("4. Creating audio narration...")
        audio_path, script = create_morning_audio(motivation, agenda_text, prayer)
        if audio_path:
            print(f"   ✓ Audio generated")
        else:
            print(f"   ❌ Audio generation failed")
            return False
        print()

        # Step 5: Generate video
        print("5. Creating video (this may take 1-2 minutes)...")
        video_path = create_video(motivation, agenda_text, prayer, audio_path)
        if video_path:
            print(f"   ✓ Video created: {video_path}")
        else:
            print(f"   ❌ Video generation failed")
            return False
        print()

        # Step 6: Send email
        print("6. Sending email...")
        if send_email_with_video(video_path):
            print(f"   ✓ Email sent to {config.EMAIL_TO}")
        else:
            print(f"   ❌ Email sending failed")
            print(f"   Video saved locally at: {video_path}")
            return False
        print()

        # Step 7: Clear agenda for next day
        print("7. Cleaning up...")
        clear_agenda()
        print(f"   ✓ Agenda cleared (set new one for tomorrow)")
        print()

        print("=" * 60)
        print("✓ SUCCESS! Your morning video has been sent!")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_system():
    """Test the system without scheduling."""
    print("Testing Awesome Morning system...\n")

    # Check configuration
    print("Checking configuration...")
    if hasattr(config, 'RESEND_API_KEY') and config.RESEND_API_KEY:
        print(f"✓ Email configured: Resend → {config.EMAIL_TO}")
    elif config.EMAIL_FROM and config.EMAIL_PASSWORD:
        print(f"✓ Email configured: {config.EMAIL_FROM} → {config.EMAIL_TO}")
    else:
        print("⚠ Email not configured. Video will be generated but not sent.")

    if not config.AI_PROVIDER:
        print("⚠ No AI API key found. Will use fallback quotes.")
    else:
        print(f"✓ AI provider: {config.AI_PROVIDER}")

    print()

    # Run the generation
    return generate_and_send_morning_video()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        # Test mode - run once
        test_system()
    else:
        # Normal mode - run once (scheduler is in scheduler.py)
        generate_and_send_morning_video()
