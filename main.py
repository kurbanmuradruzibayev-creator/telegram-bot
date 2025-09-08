import telebot
import os
from dotenv import load_dotenv

# .env fayldan tokenni yuklash
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

# Boshlanish komandasi
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Salom! 👋\n"
        "Men Cyber University haqida ma’lumot beruvchi Telegram botman.\n"
        "/programs buyrug‘i orqali yo‘nalishlarni ko‘rishingiz mumkin."
    )

# Dasturlar haqida ma’lumot
@bot.message_handler(commands=['programs'])
def programs_info(message):
    text = (
        "📚 Cyber University yo‘nalishlari:\n\n"
        "🎓 Bakalavr:\n"
        "- Kiberxavfsizlik\n"
        "- Sun’iy intellekt\n"
        "- Dasturiy injiniring\n\n"
        "🎓 Magistratura:\n"
        "- Axborot xavfsizligi\n"
        "- Ma’lumotlar tahlili\n"
    )
    bot.send_message(message.chat.id, text)

# Oddiy echo (test uchun)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

# Botni ishga tushirish
bot.infinity_polling()
