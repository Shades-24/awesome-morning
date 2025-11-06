# Resend Email Setup Guide

**Resend is the RECOMMENDED email provider** for Awesome Morning because it's:
- ✅ Free for 3,000 emails/month (plenty for daily use)
- ✅ Better deliverability (won't go to spam)
- ✅ No complex SMTP setup
- ✅ Simple API key authentication
- ✅ Professional email sending

---

## Quick Setup (5 minutes)

### Step 1: Sign up for Resend

1. Go to https://resend.com/signup
2. Create a free account (no credit card required)
3. Verify your email

### Step 2: Get your API key

1. Log in to Resend dashboard
2. Go to **API Keys** in the sidebar
3. Click **Create API Key**
4. Name it: "Awesome Morning"
5. Copy the API key (starts with `re_...`)

### Step 3: (Optional) Add your domain

**For free tier**, you can use the default `onboarding@resend.dev` sender.

**To use your own email** (like `morning@yourdomain.com`):
1. Go to **Domains** in Resend dashboard
2. Click **Add Domain**
3. Enter your domain
4. Add the DNS records they provide
5. Wait for verification (~10 minutes)

### Step 4: Configure your .env file

```bash
# Copy the example
cp .env.example .env

# Edit .env
nano .env
```

Add these lines:

```bash
# Resend Configuration (RECOMMENDED)
RESEND_API_KEY=re_your_api_key_here
EMAIL_TO=cmraad1@gmail.com

# Optional: Use custom from address (requires domain setup)
# EMAIL_FROM=morning@yourdomain.com

# Anthropic API (for AI motivation)
ANTHROPIC_API_KEY=sk-ant-api03-...
```

### Step 5: Test it!

```bash
python main.py test
```

You should see:
```
✓ Resend API key configured (RECOMMENDED)
  Provider: Resend
  From: onboarding@resend.dev
  To: cmraad1@gmail.com
```

---

## Resend vs Gmail Comparison

| Feature | Resend (Recommended) | Gmail SMTP |
|---------|---------------------|------------|
| **Setup Difficulty** | ⭐ Easy (just API key) | ⭐⭐⭐ Complex (App Password) |
| **Deliverability** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐ Good (may go to spam) |
| **Free Tier** | 3,000 emails/month | 500 emails/day |
| **From Address** | Custom domain or default | Must be your Gmail |
| **Reliability** | ⭐⭐⭐⭐⭐ Very high | ⭐⭐⭐ Medium |
| **Professional Look** | ✅ Yes | ❌ Shows Gmail |
| **Rate Limits** | Generous | Strict |

---

## Using Gmail Instead (Not Recommended)

If you really want to use Gmail:

### Step 1: Enable 2-Factor Authentication
1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification

### Step 2: Create App Password
1. Go to https://myaccount.google.com/apppasswords
2. Create password for "Mail"
3. Copy the 16-character password

### Step 3: Configure .env
```bash
EMAIL_FROM=your-gmail@gmail.com
EMAIL_PASSWORD=your-16-char-app-password
EMAIL_TO=cmraad1@gmail.com
```

**Issues with Gmail:**
- More likely to end up in spam
- Requires separate sending Gmail account
- More complex setup
- Strict rate limits

---

## Troubleshooting

### "No email provider configured"
**Solution:** Check your `.env` file has `RESEND_API_KEY=re_...`

### "Error sending email via Resend: 403"
**Solution:** Your API key is invalid. Generate a new one in Resend dashboard.

### "Domain not verified"
**Solution:**
- Use the default sender: Remove `EMAIL_FROM` from `.env`
- Or complete domain verification in Resend dashboard

### Email not arriving
**Solution:**
1. Check spam folder
2. Verify `EMAIL_TO` is correct in `.env`
3. Check Resend dashboard for delivery logs

---

## Free Tier Limits

**Resend Free Tier:**
- 3,000 emails/month
- 100 emails/day
- Up to 3 domains
- Full API access

For daily morning emails, you'll use **~30 emails/month** — well within the free tier!

---

## Cost Comparison

If you ever exceed the free tier:

- **Resend:** $20/month for 50,000 emails
- **SendGrid:** $15/month for 50,000 emails (more complex)
- **Mailgun:** $35/month for 50,000 emails
- **Gmail:** Free but unreliable for automation

**Verdict:** Resend offers the best balance of ease, reliability, and cost.

---

## Why Not Other Providers?

**SendGrid:** More complex API, worse free tier
**Mailgun:** More expensive, complex setup
**AWS SES:** Requires AWS account, complex verification
**Postmark:** No free tier
**Gmail SMTP:** Unreliable for automation

**Resend is specifically designed for developers and automation!**

---

## Next Steps

1. ✅ Sign up for Resend (5 minutes)
2. ✅ Get API key
3. ✅ Add to `.env` file
4. ✅ Test with `python main.py test`
5. ✅ Deploy to cloud
6. ✅ Wake up to motivation every morning!

---

**Questions?** Check the main README.md or the Resend documentation at https://resend.com/docs
