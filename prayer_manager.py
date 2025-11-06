"""Catholic prayer management."""
import json
import random
import os
import config

def load_prayers():
    """Load Catholic prayers from JSON file."""
    try:
        with open(config.PRAYERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Prayer file not found: {config.PRAYERS_FILE}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing prayer file: {e}")
        return []

def get_daily_prayer():
    """Get a random Catholic prayer for the day."""
    prayers = load_prayers()
    if not prayers:
        # Fallback prayer if file is missing
        return {
            "name": "Morning Prayer",
            "text": "Heavenly Father, thank You for this new day. Guide my steps, guard my heart, and grant me the grace to serve You faithfully. Amen."
        }

    return random.choice(prayers)

def get_prayer_by_name(name):
    """Get a specific prayer by name."""
    prayers = load_prayers()
    for prayer in prayers:
        if prayer['name'].lower() == name.lower():
            return prayer
    return None
