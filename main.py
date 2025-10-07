import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# .env faylidan tokenni o'qiymiz
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Start komandasi
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Men Cyber University botiman.\n"
        "Quyidagi komandalardan foydalanishingiz mumkin:\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam\n"
        "/info - Cyber University haqida ma'lumot"
    )

# Yordam komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Mavjud komandalar:\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam ko'rsatish\n"
        "/info - Universitet haqida ma'lumot\n"
        "/courses - Ta'lim yo'nalishlari"
    )

# Universitet haqida ma'lumot
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = """
🏫 **Cyber University** - O'zbekistonning raqamli kelajagi

🎯 **Asosiy maqsad:** 
Kiberxavfsizlik sohasida xalqaro darajada raqobatbardosh mutaxassislar tayyorlash

📚 **Ta'lim yo'nalishlari:**
• Kiberxavfsizlik injiniringi
• Kompyuter injiniringi
• Dasturiy injiniring
• Yurisprudensiya
• Menejment
• Iqtisodiyot

📍 **Manzil:** Toshkent viloyati, Nurafshon shahri
    """
    await update.message.reply_text(info_text)

# Kurslar haqida ma'lumot
async def courses_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    courses_text = """
🎓 **Ta'lim yo'nalishlari:**

🔐 **Kiberxavfsizlik injiniringi**
- Tarmoq xavfsizligi
- Ma'lumotlar himoyasi
- Kiberhujumlarni aniqlash

💻 **Kompyuter injiniringi**
- Kompyuter tizimlari
- Qurilma drayverlari
- Mobil qurilmalar

🖥️ **Dasturiy injiniring**
- Web dasturlash
- Mobil ilovalar
- Sun'iy intellekt

⚖️ **Yurisprudensiya**
- Axborot huquqi
- Kiberhuquq
- Intellektual mulk

📊 **Menejment**
- IT loyihalar boshqaruvi
- Biznes tahlili
- Raqamli marketing

💼 **Iqtisodiyot**
- Raqamli iqtisod
- Kripto iqtisod
- Fintech
    """
    await update.message.reply_text(courses_text)

# Xabarlarni qayta ishlash
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if 'salom' in text or 'hello' in text:
        await update.message.reply_text("Salom! Cyber University botiga xush kelibsiz!")
    elif 'grant' in text:
        await update.message.reply_text("2025/2026 o'quv yili uchun 100 ta davlat granti mavjud!")
    elif 'stipendiya' in text:
        await update.message.reply_text("Stipendiyalar sanoat hamkorlari va Innovatsion rivojlanish kengashi tomonidan taqdim etiladi")
    elif 'qabul' in text:
        await update.message.reply_text("Qabul haqida ma'lumot @cyberuni_uz kanalida e'lon qilinadi")
    else:
        await update.message.reply_text("Tushunmadim, /help buyrug'i bilan yordam oling")

# Xatoliklarni qayta ishlash
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Xato: {context.error}")

# Asosiy funksiya
def main():
    # Bot ilovasini yaratish
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Komanda handlerlarini qo'shish
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("courses", courses_command))
    
    # Xabar handlerlarini qo'shish
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Xato handlerini qo'shish
    application.add_error_handler(error_handler)
    
    # Botni ishga tushirish
    print("Bot ishga tushdi...")
    application.run_polling()

if __name__ == "__main__":
    main()
