import telebot
import os
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN o‘rnatilmagan. Railway Variables bo‘limiga qo‘shing.")

bot = telebot.TeleBot(BOT_TOKEN)

# Start komandasi
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 Yo‘nalishlar")
    btn2 = types.KeyboardButton("ℹ️ Universitet haqida")
    btn3 = types.KeyboardButton("❓ Yordam")
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "Salom! 👋\n"
        "Men Cyber University haqida ma’lumot beruvchi Telegram botman.\n"
        "Kerakli bo‘limni tugma orqali tanlang.",
        reply_markup=markup
    )

# Tugmalarni boshqarish
@bot.message_handler(func=lambda message: True)
def menu_handler(message):
    if message.text == "📚 Yo‘nalishlar":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎓 Bakalavr")
        btn2 = types.KeyboardButton("🎓 Magistratura")
        btn_back = types.KeyboardButton("⬅️ Orqaga")
        markup.add(btn1, btn2, btn_back)

        bot.send_message(message.chat.id, "📚 Yo‘nalishlardan birini tanlang:", reply_markup=markup)

    elif message.text == "🎓 Bakalavr":
        bot.send_message(
            message.chat.id,
            "🎓 Bakalavr yo‘nalishlari:\n- Kiberxavfsizlik\n- Sun’iy intellekt\n- Dasturiy injiniring"
        )

    elif message.text == "🎓 Magistratura":
        bot.send_message(
            message.chat.id,
            "🎓 Magistratura yo‘nalishlari:\n- Axborot xavfsizligi\n- Ma’lumotlar tahlili"
        )

    elif message.text == "ℹ️ Universitet haqida":
        bot.send_message(
            message.chat.id,
            "Cyber University — PQ–14 qarori asosida tashkil etilgan zamonaviy universitet."
        )

    elif message.text == "❓ Yordam":
        bot.send_message(
            message.chat.id,
            "Yordam uchun admin bilan bog‘laning: @username"
        )

    elif message.text == "⬅️ Orqaga":
        send_welcome(message)  # bosh menyuga qaytaradi

    else:
        bot.send_message(message.chat.id, "Iltimos, menyudagi tugmalardan foydalaning.")

# Botni ishga tushirish
bot.infinity_polling()
