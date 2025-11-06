"""Agenda management for daily tasks."""
import os
from datetime import datetime
import config

def load_agenda():
    """Load agenda from text file. Returns agenda items or None if not set."""
    if not os.path.exists(config.AGENDA_FILE):
        return None

    try:
        with open(config.AGENDA_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                return content
    except Exception as e:
        print(f"Error reading agenda: {e}")

    return None

def set_agenda(agenda_text):
    """Set agenda for tomorrow morning. User calls this the night before."""
    try:
        with open(config.AGENDA_FILE, 'w', encoding='utf-8') as f:
            f.write(agenda_text)
        print(f"✓ Agenda set for tomorrow morning:\n{agenda_text}")
        return True
    except Exception as e:
        print(f"Error setting agenda: {e}")
        return False

def clear_agenda():
    """Clear the agenda file after it's been used."""
    if os.path.exists(config.AGENDA_FILE):
        try:
            os.remove(config.AGENDA_FILE)
            return True
        except Exception as e:
            print(f"Error clearing agenda: {e}")
            return False
    return True

def format_agenda_for_video(agenda_text):
    """Format agenda text for display in video."""
    if not agenda_text:
        return "No agenda set for today. Take time to plan your priorities!"

    # Add header
    formatted = "TODAY'S AGENDA:\n\n"

    # Split into lines and format
    lines = agenda_text.strip().split('\n')
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if line:
            # Add bullet if not already present
            if not line.startswith(('•', '-', '*', str(i))):
                formatted += f"• {line}\n"
            else:
                formatted += f"{line}\n"

    return formatted.strip()
