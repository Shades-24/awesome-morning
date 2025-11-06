"""Text-to-speech audio generation."""
import os
from datetime import datetime
from gtts import gTTS
import config

def generate_script(motivation, agenda, prayer):
    """Generate the narration script for the video."""
    greeting = get_time_greeting()
    today = datetime.now().strftime("%A, %B %d")

    script_parts = []

    # Opening
    script_parts.append(f"{greeting}. Today is {today}.")
    script_parts.append("")

    # Motivation
    script_parts.append("Here's your motivation for today:")
    script_parts.append(motivation)
    script_parts.append("")

    # Agenda
    if agenda:
        script_parts.append("Your agenda for today:")
        # Clean up agenda for speech
        agenda_lines = agenda.replace("TODAY'S AGENDA:", "").strip()
        script_parts.append(agenda_lines)
        script_parts.append("")

    # Prayer
    script_parts.append("Let's begin with a prayer.")
    script_parts.append(f"{prayer['name']}.")
    script_parts.append(prayer['text'])
    script_parts.append("")

    # Closing
    script_parts.append("Have a blessed and productive day!")

    return "\n".join(script_parts)

def get_time_greeting():
    """Get time-appropriate greeting."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def generate_audio(script, output_path):
    """Generate audio file from script using text-to-speech."""
    try:
        # Use Google Text-to-Speech with English voice
        tts = gTTS(text=script, lang='en', slow=False)
        tts.save(output_path)
        print(f"✓ Audio generated: {output_path}")
        return True
    except Exception as e:
        print(f"Error generating audio: {e}")
        return False

def create_morning_audio(motivation, agenda, prayer):
    """Create the complete morning audio narration."""
    # Generate script
    script = generate_script(motivation, agenda, prayer)

    # Generate audio file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_path = os.path.join(config.OUTPUT_DIR, f"morning_audio_{timestamp}.mp3")

    if generate_audio(script, audio_path):
        return audio_path, script
    else:
        return None, script
