#!/usr/bin/env bash
set -e

echo "🚀 Starting Telegram Bot..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install --no-cache-dir -r requirements.txt

# Load environment variables from .env if present (local testing)
if [ -f .env ]; then
  echo "📝 Loading .env file..."
  export $(grep -v '^#' .env | xargs)
fi

# Check if TELEGRAM_TOKEN is set
if [ -z "$TELEGRAM_TOKEN" ]; then
  echo "❌ ERROR: TELEGRAM_TOKEN not set!"
  echo ""
  echo "For Render Dashboard:"
  echo "  1. Go to https://dashboard.render.com/"
  echo "  2. Select your service"
  echo "  3. Click Settings → Environment"
  echo "  4. Add: TELEGRAM_TOKEN = <your bot token from @BotFather>"
  echo "  5. Click Save"
  echo ""
  exit 1
fi

echo "✅ TELEGRAM_TOKEN found!"
echo "🎮 Starting bot now..."
echo ""

# Run the bot
python main.py
