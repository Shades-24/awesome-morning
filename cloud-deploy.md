# Cloud Deployment Guide

This guide covers deploying Awesome Morning to various cloud platforms.

## Prerequisites

- Git repository with your code
- `.env` file with your credentials (DO NOT commit this)
- Cloud platform account

## Option 1: Docker-based Cloud Deployment

### AWS EC2 / Google Cloud Compute / DigitalOcean Droplet

1. **Create a VM instance:**
   - Choose a small instance (1GB RAM minimum)
   - Ubuntu 22.04 LTS recommended

2. **Connect to your VM:**
   ```bash
   ssh user@your-vm-ip
   ```

3. **Install Docker:**
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   ```

4. **Clone your repository:**
   ```bash
   git clone https://github.com/yourusername/awesome-morning.git
   cd awesome-morning
   ```

5. **Set up environment:**
   ```bash
   cp .env.example .env
   nano .env  # Edit with your credentials
   ```

6. **Run with Docker Compose:**
   ```bash
   docker-compose up -d
   ```

7. **Check logs:**
   ```bash
   docker-compose logs -f
   ```

## Option 2: AWS Lambda (Serverless)

For serverless deployment, you can use AWS Lambda with EventBridge:

1. Package your application
2. Create Lambda function with Python 3.11 runtime
3. Set up EventBridge rule for daily 7 AM trigger
4. Configure environment variables in Lambda

Note: Lambda has limits on execution time and package size. Video generation might exceed limits.

## Option 3: Google Cloud Run

Cloud Run can handle longer execution times:

1. Build Docker image
2. Push to Google Container Registry
3. Deploy to Cloud Run
4. Set up Cloud Scheduler for daily triggers

## Option 4: Railway / Render / Fly.io

These platforms offer simple deployment:

### Railway:
1. Connect your GitHub repo
2. Set environment variables
3. Deploy - automatically restarts on crashes

### Render:
1. Create new "Background Worker"
2. Connect repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python scheduler.py`

### Fly.io:
1. Install flyctl
2. Run `fly launch`
3. Deploy with `fly deploy`

## Recommended: DigitalOcean Droplet

For simplicity and cost-effectiveness:

1. **Create $6/month droplet** (Ubuntu 22.04)
2. **Setup:**
   ```bash
   # Install dependencies
   sudo apt update
   sudo apt install -y python3 python3-pip ffmpeg imagemagick

   # Clone repo
   git clone your-repo
   cd awesome-morning

   # Install Python packages
   pip3 install -r requirements.txt

   # Configure
   cp .env.example .env
   nano .env  # Add your credentials

   # Test
   python3 main.py test

   # Run scheduler
   python3 scheduler.py
   ```

3. **Run as systemd service** (keeps running):
   ```bash
   sudo cp awesome-morning.service /etc/systemd/system/
   sudo nano /etc/systemd/system/awesome-morning.service  # Update paths
   sudo systemctl enable awesome-morning
   sudo systemctl start awesome-morning
   sudo systemctl status awesome-morning
   ```

## Email Configuration for Cloud

When deploying to cloud, use Gmail App Passwords:

1. Go to https://myaccount.google.com/apppasswords
2. Create an app password for "Mail"
3. Use this password (not your regular password) in `.env`

## Security Notes

- Never commit `.env` file
- Use environment variables for secrets
- Restrict VM access with firewall rules
- Keep system updated: `sudo apt update && sudo apt upgrade`

## Cost Estimates

- **DigitalOcean Droplet**: $6/month
- **AWS EC2 (t2.micro)**: ~$8-10/month
- **Google Cloud (e2-micro)**: ~$7/month
- **Railway**: $5/month (Hobby plan)
- **Render**: Free tier available (with limitations)

## Monitoring

Check if service is running:
```bash
# Docker
docker-compose ps

# Systemd
sudo systemctl status awesome-morning

# Logs
tail -f output/*.log  # if you add logging
```

## Troubleshooting

**Service not starting:**
- Check logs: `sudo journalctl -u awesome-morning -f`
- Verify `.env` file exists and has correct values
- Check Python dependencies: `pip3 list`

**Video not sending:**
- Test email config: `python3 -c "from email_sender import test_email_config; test_email_config()"`
- Check Gmail App Password is correct
- Verify email is not in spam folder

**Out of disk space:**
- Clear old videos: `rm output/morning_video_*.mp4`
- Set up cron to clean old files

## Updating Code

```bash
cd awesome-morning
git pull
docker-compose down
docker-compose up -d --build
```

Or for systemd:
```bash
cd awesome-morning
git pull
sudo systemctl restart awesome-morning
```
