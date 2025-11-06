"""Configuration management for Awesome Morning."""
import os
from dotenv import load_dotenv

load_dotenv()

# Email Configuration
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_TO = os.getenv('EMAIL_TO', 'cmraad1@gmail.com')

# AI Configuration
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Use Anthropic by default if available, otherwise OpenAI
AI_PROVIDER = 'anthropic' if ANTHROPIC_API_KEY else 'openai' if OPENAI_API_KEY else None

# Schedule Configuration
DELIVERY_TIME = os.getenv('DELIVERY_TIME', '07:00')
TIMEZONE = os.getenv('TIMEZONE', 'America/New_York')

# Video Configuration
VIDEO_DURATION = int(os.getenv('VIDEO_DURATION', '30'))
VIDEO_WIDTH = int(os.getenv('VIDEO_WIDTH', '1920'))
VIDEO_HEIGHT = int(os.getenv('VIDEO_HEIGHT', '1080'))
VIDEO_FPS = 24

# Paths
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
AGENDA_FILE = os.path.join(os.path.dirname(__file__), 'agenda.txt')
PRAYERS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'catholic_prayers.json')

# Create directories if they don't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(PRAYERS_FILE), exist_ok=True)
