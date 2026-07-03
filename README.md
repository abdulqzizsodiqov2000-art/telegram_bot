# 🎮 Telegram Games Bot - Render Deployment Guide

## ⚡ Setup Instructions

### 1. Get Telegram Bot Token
- Message [@BotFather](https://t.me/BotFather) on Telegram
- Send `/start` → `/newbot` → follow instructions
- Copy the token (example: `123456789:ABCdefGHIjklmnOPQRstuvWXYZ`)

### 2. Add Environment Variables on Render
**CRITICAL STEP** - Bot won't run without this!

1. Go to your Render service
2. Click **Settings** → **Environment**
3. Add this variable:
   - **Key:** `TELEGRAM_TOKEN`
   - **Value:** `your_actual_token_from_BotFather`
4. Click **Save** (it will auto-deploy)

### 3. Deploy
1. Push code to GitHub/GitLab
2. On Render, create **New** → **Background Worker**
3. Select your repo
4. Name: `telegram-bot` (or any name)
5. Runtime: `Python 3`
6. Build Command: `pip install -r requirements.txt`
7. Start Command: `bash start.sh`
8. Plan: **Free** (or Paid)
9. **Important:** Add environment variable before deploying!
10. Click **Create Background Worker**

## 🔧 Local Testing
```bash
# Create .env file
cp .env.example .env

# Fill your token
# TELEGRAM_TOKEN=your_token_here

# Install and run
pip install -r requirements.txt
python main.py
```

## ❌ Troubleshooting

**Error: "TELEGRAM_TOKEN environment variable not set!"**
- ✅ Go to Render Dashboard → Settings → Environment
- ✅ Add `TELEGRAM_TOKEN` with your actual token
- ✅ Save and wait for auto-deploy (1-2 min)

**Bot doesn't respond**
- Check Render logs for errors
- Verify token is correct from @BotFather
- Restart the service in Render Dashboard
