# 🎮 Telegram Games Bot

O'zbekcha o'yinlar botiga xush kelibsiz!

## 🚀 Tez Deployment (Render)

### 1️⃣ Token Olish
@BotFather'ga Telegram'da yozing:
- `/start`
- `/newbot`
- Bot nomini kiriting
- **TOKEN'ni copy qiling** (example: `123456789:ABCdefGHIjklmnOPQRstuvWXYZ`)

### 2️⃣ GitHub'da Deploy Qiling
```bash
# GitHub'da repository yarating
git clone https://github.com/YOUR_USERNAME/telegram_bot
cd telegram_bot
git add .
git commit -m "Initial commit"
git push origin main
```

### 3️⃣ Render'da Token Qo'shing (MUQIM!)

**Bu qadam KERAK, bo'lmasa bot ishlamaydi!**

1. https://dashboard.render.com/ ga kiring
2. **New** → **Background Worker** tanlang
3. GitHub repo'ni tanlang va Connect qiling
4. **Name:** `telegram-bot`
5. **Runtime:** `Python 3`
6. **Build Command:** `pip install -r requirements.txt` ✅
7. **Start Command:** `bash start.sh` ✅
8. **Plan:** `Free` ✅
9. **Environment Variables** qismi:
   - Klik: **Add Environment Variable**
   - **Key:** `TELEGRAM_TOKEN`
   - **Value:** `<BotFather'dan olgan tokeningiz>` (o'zingiz olgan haqiqiy token)
   - **Save** tugmasini bosing

10. **Create Background Worker** tugmasini bosing
11. ✅ Bot 2 daqiqada ishga tushar!

## 💻 Local Testing

```bash
# .env file'i tekshiring
cat .env

# Dependencies o'rnatish
pip install -r requirements.txt

# Bot'ni ishga tushirish
python main.py
```

Bot ishlasa, Telegram'da `/start` bo'sh message yuboring

## ✅ Status Tekshirish

Render Dashboard'da:
- **Logs** → Bot xatoliklarini ko'ring
- **Redeploy** → Qayta deploy qilish

## 🎮 O'yinlar

Bot quyidagi o'yinlarni taklif qiladi:
- 🎲 Son topish
- 🎲 Zar tashlash
- 🪙 Tanga tashlash
- ✊ Tosh-Qaychi-Qog'oz
- ➕ Matematika
- 🎯 Quiz
- 🔠 So'z topish
- 🔢 Juft yoki Toq
- 🎰 Slot
- ❤️ Love Test

## ❌ Agar Bot Ishlamasa

**Error: "TELEGRAM_TOKEN not found"**
- ✅ Render Dashboard → Settings → Environment
- ✅ `TELEGRAM_TOKEN` qo'shilganini tekshiring
- ✅ **Save** tugmasini bosing
- ✅ 2 daqiqa kuting va qayta tekshiring

**Logs'da boshqa xato ko'rsa:**
- Render Dashboard → Logs → Xabarni o'qing
- GitHub'da push qiling va qayta deploy qiling

## 📝 Fayllar

- `main.py` - Bot kodi
- `requirements.txt` - Dependencies
- `render.yaml` - Render konfiguratsiyasi
- `start.sh` - Launch script
- `.env.example` - Environment variables example
- `.gitignore` - Git ignore rules

## ⚠️ Muhim

- `.env` fayl **GitHub'da saqlanmaydi** (.gitignore)
- Token **Render Dashboard'da** qo'shilishi KERAK
- Token **HECH QANDAY JOYDA** publish qilmang!
