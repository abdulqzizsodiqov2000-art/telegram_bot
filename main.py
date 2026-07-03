#!/usr/bin/env python3
"""Telegram Games Bot"""

import os
import logging
import random
from dotenv import load_dotenv

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Setup
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Token
TOKEN = os.getenv("TELEGRAM_TOKEN", "").strip()
if not TOKEN:
    logger.error("❌ TELEGRAM_TOKEN not set!")
    logger.error("Go to: https://dashboard.render.com/ → Settings → Environment")
    logger.error("Add: TELEGRAM_TOKEN = <BotFather'dan olgan tokeningiz>")
    raise ValueError("Token required!")

# Game state
games = {}

# Menu
menu = [
    ["🎲 Son topish"],
    ["🎲 Zar tashlash"],
    ["🪙 Tanga tashlash"],
    ["✊ Tosh-Qaychi-Qog'oz"],
    ["➕ Matematika"],
    ["🎯 Quiz"],
    ["🔠 So'z topish"],
    ["🔢 Juft yoki Toq"],
    ["🎰 Slot"],
    ["❤️ Love Test"],
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 O'yinlar botiga xush kelibsiz!\nKerakli o'yinni tanlang.",
        reply_markup=ReplyKeyboardMarkup(menu, resize_keyboard=True)
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id
    text = update.message.text

    if text == "🎲 Son topish":
        games[user] = {"type": "number", "value": random.randint(1, 10)}
        await update.message.reply_text("Men 1 dan 10 gacha son o'yladim. Toping!")

    elif user in games and games[user]["type"] == "number":
        try:
            guess = int(text)
            if guess == games[user]["value"]:
                await update.message.reply_text("🎉 To'g'ri topdingiz!")
                del games[user]
            elif guess > games[user]["value"]:
                await update.message.reply_text("📉 Kichikroq son kiriting.")
            else:
                await update.message.reply_text("📈 Kattaroq son kiriting.")
        except ValueError:
            pass

    elif text == "🎲 Zar tashlash":
        await update.message.reply_text(f"🎲 Natija: {random.randint(1,6)}")

    elif text == "🪙 Tanga tashlash":
        await update.message.reply_text(random.choice(["🟡 Gerb", "⚪ Raqam"]))

    elif text == "✊ Tosh-Qaychi-Qog'oz":
        bot = random.choice(["✊ Tosh", "✌️ Qaychi", "🖐 Qog'oz"])
        await update.message.reply_text(f"Bot tanladi: {bot}")

    elif text == "➕ Matematika":
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        games[user] = {"type": "math", "value": a + b}
        await update.message.reply_text(f"{a} + {b} = ?")

    elif user in games and games[user]["type"] == "math":
        try:
            if int(text) == games[user]["value"]:
                await update.message.reply_text("✅ To'g'ri!")
            else:
                await update.message.reply_text(f"❌ Xato. Javob: {games[user]['value']}")
            del games[user]
        except ValueError:
            await update.message.reply_text("Faqat son kiriting!")

    elif text == "🎯 Quiz":
        games[user] = {"type": "quiz"}
        await update.message.reply_text("O'zbekiston poytaxti qaysi shahar?\nA) Samarqand\nB) Toshkent\nC) Buxoro")

    elif user in games and games[user]["type"] == "quiz":
        if text.lower() in ["toshkent", "b)", "b"]:
            await update.message.reply_text("✅ To'g'ri!")
            del games[user]
        else:
            await update.message.reply_text("❌ Xato. To'g'ri: Toshkent")
            del games[user]

    elif text == "🔠 So'z topish":
        word = random.choice(["PYTHON", "TELEGRAM", "BOT", "GAME"])
        await update.message.reply_text(f"Yashirin so'z: {word}")

    elif text == "🔢 Juft yoki Toq":
        son = random.randint(1, 100)
        natija = "Juft" if son % 2 == 0 else "Toq"
        await update.message.reply_text(f"{son} — {natija}")

    elif text == "🎰 Slot":
        icons = ["🍒", "🍋", "🍉", "⭐", "7️⃣"]
        await update.message.reply_text(f"{random.choice(icons)} | {random.choice(icons)} | {random.choice(icons)}")

    elif text == "❤️ Love Test":
        await update.message.reply_text(f"❤️ Moslik darajasi: {random.randint(1,100)}%")

    else:
        await update.message.reply_text("Menyudan o'yin tanlang.")

def main():
    """Start the bot."""
    logger.info("🚀 Bot starting...")
    app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    logger.info("✅ Bot initialized!")
    logger.info("🎮 Waiting for messages...")
    
    # Start polling
    app.run_polling()


if __name__ == "__main__":
    main()