import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import random
import logging
from dotenv import load_dotenv

# Load .env file if exists (for local testing)
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN", "").strip()
if not TOKEN:
    logger.error("❌ TELEGRAM_TOKEN environment variable not set!")
    logger.error("📝 On Render Dashboard:")
    logger.error("   1. Click: Settings")
    logger.error("   2. Click: Environment")
    logger.error("   3. Add Variable: TELEGRAM_TOKEN = <your_token_from_BotFather>")
    logger.error("   4. Click Save (auto-deploy will start)")
    logger.error("")
    logger.error("💻 Get token: Message @BotFather on Telegram → /newbot")
    import sys
    sys.exit(1)

numbers = {}

keyboard = [
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
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id
    text = update.message.text

    # Son topish
    if text == "🎲 Son topish":
        numbers[user] = random.randint(1, 10)
        await update.message.reply_text("Men 1 dan 10 gacha son o'yladim. Toping!")

    elif user in numbers:
        try:
            guess = int(text)
            if guess == numbers[user]:
                await update.message.reply_text("🎉 To'g'ri topdingiz!")
                del numbers[user]
            elif guess > numbers[user]:
                await update.message.reply_text("📉 Kichikroq son kiriting.")
            else:
                await update.message.reply_text("📈 Kattaroq son kiriting.")
        except ValueError:
            pass

    # Zar
    elif text == "🎲 Zar tashlash":
        await update.message.reply_text(f"🎲 Natija: {random.randint(1,6)}")

    # Tanga
    elif text == "🪙 Tanga tashlash":
        await update.message.reply_text(random.choice(["🟡 Gerb", "⚪ Raqam"]))

    # Tosh-Qaychi-Qog'oz
    elif text == "✊ Tosh-Qaychi-Qog'oz":
        bot = random.choice(["✊ Tosh", "✌️ Qaychi", "🖐 Qog'oz"])
        await update.message.reply_text(f"Bot tanladi: {bot}")

    # Matematika
    elif text == "➕ Matematika":
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        context.user_data["math"] = a + b
        await update.message.reply_text(f"{a} + {b} = ?")

    elif "math" in context.user_data:
        try:
            if int(text) == context.user_data["math"]:
                await update.message.reply_text("✅ To'g'ri!")
            else:
                await update.message.reply_text(
                    f"❌ Xato. Javob: {context.user_data['math']}"
                )
            del context.user_data["math"]
        except ValueError:
            await update.message.reply_text("Faqat son kiriting!")

    # Quiz
    elif text == "🎯 Quiz":
        await update.message.reply_text(
            "Savol:\nO'zbekiston poytaxti qaysi shahar?\n\nA) Samarqand\nB) Toshkent\nC) Buxoro\n\nJavobni yozing."
        )

    elif text.lower() == "toshkent":
        await update.message.reply_text("✅ To'g'ri!")

    # So'z topish
    elif text == "🔠 So'z topish":
        word = random.choice(["PYTHON", "TELEGRAM", "BOT", "GAME"])
        await update.message.reply_text(f"Yashirin so'z: {word}")

    # Juft yoki Toq
    elif text == "🔢 Juft yoki Toq":
        son = random.randint(1, 100)
        natija = "Juft" if son % 2 == 0 else "Toq"
        await update.message.reply_text(f"{son} — {natija}")

    # Slot
    elif text == "🎰 Slot":
        icons = ["🍒", "🍋", "🍉", "⭐", "7️⃣","15"]
        await update.message.reply_text(
            f"{random.choice(icons)} | {random.choice(icons)} | {random.choice(icons)}"
        )

    # Love Test
    elif text == "❤️ Love Test":
        await update.message.reply_text(
            f"❤️ Moslik darajasi: {random.randint(1,100)}%"
        )

    else:
        await update.message.reply_text("Menyudan o'yin tanlang.")

async def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
    
    logger.info("✅ Bot ishga tushdi...")
    
    async with app:
        await app.start()
        await app.updater.start_polling()
        await app.updater.idle()
        await app.stop()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())