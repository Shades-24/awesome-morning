# Awesome Morning ☀️

**Your personalized morning motivation video, delivered daily via email.**

Wake up to an AI-generated motivational message, your daily agenda, and a Catholic prayer—all narrated in a beautiful ~30-second video sent directly to your inbox every morning at 7 AM.

---

## Features

✨ **AI-Powered Motivation** - Fresh, inspiring messages generated daily using Claude or GPT
📅 **Daily Agenda** - Set your tasks the night before, see them in the morning
🙏 **Catholic Prayers** - Start each day with a prayer from a curated collection
🎥 **Video Generation** - Professional-looking videos with text overlays and narration
🔊 **Text-to-Speech** - Natural-sounding voice narration
📧 **Email Delivery** - Automatically sent to your email every morning
☁️ **Cloud-Ready** - Easy deployment to any cloud platform

---

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/awesome-morning.git
cd awesome-morning

# Install dependencies
pip install -r requirements.txt

# Or use a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your credentials
nano .env
```

**Required settings in `.env`:**

```bash
# Email Configuration - OPTION 1: Resend (RECOMMENDED)
# Sign up at https://resend.com (free, 3000 emails/month)
RESEND_API_KEY=re_your_api_key_here
EMAIL_TO=cmraad1@gmail.com

# Email Configuration - OPTION 2: Gmail SMTP (not recommended)
# EMAIL_FROM=your-email@gmail.com
# EMAIL_PASSWORD=your-gmail-app-password
# EMAIL_TO=cmraad1@gmail.com

# AI API Key (optional but recommended)
ANTHROPIC_API_KEY=your-anthropic-key-here

# Schedule (optional, defaults shown)
DELIVERY_TIME=07:00
TIMEZONE=America/New_York
```

**Resend Setup (RECOMMENDED - 5 minutes):**
1. Go to https://resend.com/signup
2. Create free account (no credit card needed)
3. Get API key from dashboard
4. Add `RESEND_API_KEY=re_...` to `.env`
5. Done! Much easier than Gmail.

**See [RESEND_SETUP.md](RESEND_SETUP.md) for detailed email setup guide.**

### 3. Test the System

```bash
# Test generation without scheduling
python main.py test
```

This will:
- Generate a motivation message
- Load your agenda (if set)
- Select a prayer
- Create the video
- Send it to your email

### 4. Set Your Agenda

The night before, set what you want to accomplish:

```bash
# Interactive mode
python set_agenda.py

# Or provide directly
python set_agenda.py "Morning workout, Team meeting at 10am, Finish report"

# View current agenda
python set_agenda.py show
```

### 5. Start the Scheduler

```bash
# Run the scheduler (keeps running)
python scheduler.py
```

The scheduler will:
- Run every day at 7:00 AM (or your configured time)
- Generate and send your morning video
- Clear the agenda for the next day

**Keep the scheduler running** - Use cloud deployment (see below) for 24/7 operation.

---

## Usage Examples

### Setting Your Agenda

```bash
# Example agenda entry
python set_agenda.py
```

Then type:
```
- Morning prayer and meditation
- Gym at 6:30am
- Client meeting at 10am
- Lunch with Sarah at 12pm
- Work on project proposal
- Evening family time
```

Press Ctrl+D (Mac/Linux) or Ctrl+Z (Windows) when done.

### Running a Test

```bash
python main.py test
```

Output:
```
============================================================
AWESOME MORNING - Generating your daily motivation video
============================================================
Time: 2024-01-15 07:00:00

1. Generating motivational message...
   ✓ Motivation: Today is a gift. Embrace it with courage...

2. Loading your agenda...
   ✓ Agenda loaded

3. Selecting Catholic prayer...
   ✓ Prayer: Morning Offering

4. Creating audio narration...
   ✓ Audio generated

5. Creating video (this may take 1-2 minutes)...
   ✓ Video created: output/morning_video_20240115_070000.mp4

6. Sending email...
   ✓ Email sent to cmraad1@gmail.com

7. Cleaning up...
   ✓ Agenda cleared (set new one for tomorrow)

============================================================
✓ SUCCESS! Your morning video has been sent!
============================================================
```

---

## Cloud Deployment

For 24/7 operation, deploy to a cloud server. See [cloud-deploy.md](cloud-deploy.md) for detailed guides.

### Quick Deploy with Docker

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Recommended: DigitalOcean ($6/month)

1. Create a Droplet (Ubuntu 22.04, Basic $6/month)
2. SSH into your server
3. Clone this repo
4. Install dependencies
5. Set up as systemd service

```bash
# On your cloud server
git clone https://github.com/yourusername/awesome-morning.git
cd awesome-morning
pip3 install -r requirements.txt
cp .env.example .env
nano .env  # Add your credentials

# Test it
python3 main.py test

# Run as service
sudo cp awesome-morning.service /etc/systemd/system/
sudo nano /etc/systemd/system/awesome-morning.service  # Update paths
sudo systemctl enable awesome-morning
sudo systemctl start awesome-morning
```

---

## Project Structure

```
awesome-morning/
├── main.py                    # Main application orchestrator
├── scheduler.py               # Daily scheduling system
├── set_agenda.py             # Utility to set daily agenda
├── config.py                 # Configuration management
├── ai_generator.py           # AI-powered motivation
├── prayer_manager.py         # Catholic prayer database
├── agenda_manager.py         # Agenda file handling
├── audio_generator.py        # Text-to-speech narration
├── video_generator.py        # Video creation with overlays
├── email_sender.py           # Email delivery system
├── data/
│   └── catholic_prayers.json # Collection of Catholic prayers
├── output/                   # Generated videos and audio
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── Dockerfile               # Docker container config
├── docker-compose.yml       # Docker Compose setup
├── awesome-morning.service  # systemd service file
├── cloud-deploy.md         # Cloud deployment guide
└── README.md               # This file
```

---

## Customization

### Change Prayer Collection

Edit `data/catholic_prayers.json` to add more prayers:

```json
[
  {
    "name": "Your Prayer Name",
    "text": "Prayer text here..."
  }
]
```

### Modify Video Style

Edit `video_generator.py`:
- Change background colors (line 15-25)
- Adjust font sizes
- Modify layout and timing

### Use Different AI Provider

In `.env`, set either:
```bash
ANTHROPIC_API_KEY=sk-ant-...  # For Claude
```
or
```bash
OPENAI_API_KEY=sk-...  # For GPT
```

### Change Delivery Time

In `.env`:
```bash
DELIVERY_TIME=06:00  # 6 AM
TIMEZONE=America/Los_Angeles
```

---

## Troubleshooting

### Email Not Sending

**Problem:** Email not being sent

**Solution:**
1. **Use Resend (recommended)** - Much more reliable than Gmail
   - Sign up at https://resend.com
   - Get API key and add to `.env`
   - See [RESEND_SETUP.md](RESEND_SETUP.md) for details

2. **If using Gmail:**
   - Make sure you're using a Gmail App Password, not your regular password
   - Enable 2-factor authentication on your Google account
   - Generate app password at https://myaccount.google.com/apppasswords

### Video Generation Failed

**Problem:** `MoviePy error` or missing fonts

**Solution:**
```bash
# Install system dependencies
# Ubuntu/Debian:
sudo apt install ffmpeg imagemagick fonts-dejavu-core

# macOS:
brew install ffmpeg imagemagick

# Windows: Download and install FFmpeg from ffmpeg.org
```

### AI Generation Not Working

**Problem:** Using fallback quotes instead of AI

**Solution:**
1. Check your API key is correct in `.env`
2. Verify you have credits/access to the API
3. Test with: `python -c "from ai_generator import generate_motivation; print(generate_motivation())"`

### Scheduler Not Running

**Problem:** Script stops after SSH disconnect

**Solution:** Use one of these approaches:
1. Cloud deployment with systemd service
2. Run in Docker container
3. Use `nohup python scheduler.py &`
4. Use `screen` or `tmux`

---

## Requirements

### Python Dependencies
- Python 3.8+
- moviepy (video generation)
- Pillow (image processing)
- gTTS (text-to-speech)
- anthropic or openai (AI generation)
- APScheduler (scheduling)
- python-dotenv (configuration)

### System Dependencies
- FFmpeg (video encoding)
- ImageMagick (image processing)
- System fonts

---

## FAQ

**Q: Does this work on Windows?**
A: Yes! Install Python 3.8+, FFmpeg, and ImageMagick. Then follow the setup guide.

**Q: Can I use a different email provider?**
A: Yes, modify `email_sender.py` to use your SMTP server settings.

**Q: How much does it cost to run?**
A: Cloud hosting: ~$6/month. AI API: ~$0.01-0.05/day. Email: Free with Gmail.

**Q: Can I customize the prayers?**
A: Yes! Edit `data/catholic_prayers.json` to add/remove prayers.

**Q: What if I don't set an agenda?**
A: The video will still be generated with motivation and prayer, just without agenda items.

**Q: Can I run this locally instead of cloud?**
A: Yes, but your computer must be on at 7 AM. Cloud deployment is recommended for reliability.

---

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

MIT License - feel free to use and modify for personal use.

---

## Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review [cloud-deploy.md](cloud-deploy.md) for deployment help
3. Open an issue on GitHub

---

## Acknowledgments

- Built with Python, MoviePy, and love
- Text-to-speech by Google TTS
- AI generation by Anthropic Claude / OpenAI GPT
- Catholic prayers from traditional sources

---

**Made with ☕ and 🙏 to start each day with purpose and faith.**
