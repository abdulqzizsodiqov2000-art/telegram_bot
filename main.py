from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

# Bot tokeningizni shu yerga yozing
TOKEN = "8736854784:AAF1N4sNNYO0vKBITVSBuaVCvd0BZwllyNc"

# 20 ta yaxshi omad
good_luck = [
    "🎉 Bugun juda omadli kuningiz!",
    "💰 Katta pul topishingiz mumkin.",
    "❤️ Sevgan insoningiz sizni xursand qiladi.",
    "🏆 Ishlaringiz muvaffaqiyatli bo'ladi.",
    "🌟 Omad siz tomonda.",
    "🎁 Kutilmagan sovg'a olasiz.",
    "😊 Kayfiyatingiz a'lo bo'ladi.",
    "📚 O'qishda muvaffaqiyat kutmoqda.",
    "🚗 Yaxshi safar kutmoqda.",
    "💼 Ishingizda o'sish bo'ladi.",
    "🤝 Yangi do'st orttirasiz.",
    "🍀 Bugun eng omadli kunlardan biri.",
    "🎯 Maqsadingizga erishasiz.",
    "🏡 Oilangiz bilan baxtli vaqt o'tkazasiz.",
    "💎 Foydali imkoniyat chiqadi.",
    "🥇 G'alaba sizniki bo'ladi.",
    "📱 Yaxshi xabar olasiz.",
    "🎊 Orzuingiz amalga oshadi.",
    "🌈 Quvonchli voqealar bo'ladi.",
    "⭐ Omad sizga kulib boqmoqda."
]

# 20 ta yomon omad
bad_luck = [
    "😕 Bugun ehtiyot bo'ling.",
    "💸 Keraksiz xarajat qilishingiz mumkin.",
    "⚠️ Shoshilmang, xato qilishingiz mumkin.",
    "🌧 Kayfiyatingiz biroz tushishi mumkin.",
    "📵 Keraksiz tortishuvlardan uzoq bo'ling.",
    "🚫 Bugun tavakkal qilmang.",
    "😴 Charchoq sezishingiz mumkin.",
    "📉 Rejalaringiz kechikishi mumkin.",
    "🤕 Mayda muammolar chiqishi mumkin.",
    "⏳ Sabr qilish kerak bo'ladi.",
    "❌ Hamma gapga ishonmang.",
    "🚷 Ehtiyotkor bo'ling.",
    "😔 Omad bugun siz tomonda emas.",
    "📄 Hujjatlarni tekshirib chiqing.",
    "🚦 Yo'lda ehtiyot bo'ling.",
    "😶 Sirlaringizni hammaga aytmang.",
    "📦 Kutilgan narsa kechikishi mumkin.",
    "💔 Xafa qiladigan gap eshitishingiz mumkin.",
    "🌪 Kutilmagan vaziyat yuz berishi mumkin.",
    "☁️ Bugun dam olganingiz ma'qul."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎰 Omad o'yiniga xush kelibsiz!\n\n"
        "/omad buyrug'ini yuboring va 5 ta omad natijasini oling!"
    )

async def omad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    natijalar = []

    # Bir xil natija qayta chiqmasligi uchun
    yaxshi = random.sample(good_luck, 5)
    yomon = random.sample(bad_luck, 5)

    for i in range(5):
        if random.choice([True, False]):
            natijalar.append(f"🍀 {i+1}. {yaxshi.pop()}")
        else:
            natijalar.append(f"💀 {i+1}. {yomon.pop()}")

    await update.message.reply_text(
        "🎰 Sizning bugungi 5 ta omadingiz:\n\n"
        + "\n".join(natijalar)
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("omad", omad))

    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()