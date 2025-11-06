#!/usr/bin/env python3
"""
Generate morning video and save locally (no email).
Use this while troubleshooting Resend account.
"""

from datetime import datetime
import config
from ai_generator import generate_motivation
from prayer_manager import get_daily_prayer
from agenda_manager import load_agenda, format_agenda_for_video

print("=" * 60)
print("AWESOME MORNING - Local Video Generation")
print("=" * 60)
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

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
    print(f"   ℹ No agenda set")
print()

# Step 3: Get prayer
print("3. Selecting Catholic prayer...")
prayer = get_daily_prayer()
print(f"   ✓ Prayer: {prayer['name']}")
print()

# Step 4: Create script (no audio for now to avoid gTTS issues)
print("4. Creating narration script...")
from audio_generator import generate_script
script = generate_script(motivation, agenda_text, prayer)
print(f"   ✓ Script created ({len(script)} characters)")
print()
print("   Script Preview:")
print("   " + "-" * 55)
for line in script.split('\n')[:10]:
    print(f"   {line}")
print("   " + "-" * 55)
print()

# Step 5: Save script to file
script_filename = f"morning_script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
script_path = f"{config.OUTPUT_DIR}/{script_filename}"
with open(script_path, 'w') as f:
    f.write(script)
print(f"5. Script saved to: {script_path}")
print()

print("=" * 60)
print("✓ SUCCESS! Content generated!")
print("=" * 60)
print()
print("Your morning motivation content is ready:")
print(f"  - Motivation: {len(motivation)} characters")
print(f"  - Prayer: {prayer['name']}")
print(f"  - Agenda: {'Set' if agenda_raw else 'Not set'}")
print(f"  - Script: {script_path}")
print()
print("Once Resend is working, this will be:")
print("  - Converted to speech")
print("  - Made into a video")
print("  - Emailed to cmraad1@gmail.com")
