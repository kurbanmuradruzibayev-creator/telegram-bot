import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Konstanta sifatida joylashuv
LOCATION = "📍 Joylashuv: Universitet Toshkent viloyati, Nurafshon shahri."

# Asosiy keyboard
def main_keyboard():
    keyboard = [
        [KeyboardButton("🎓 Ta'lim yo'nalishlari"), KeyboardButton("ℹ️ Universitet haqida")],
        [KeyboardButton("📞 Aloqa", request_contact=True), KeyboardButton("📍 Manzil", request_location=True)],
        [KeyboardButton("💰 Grantlar"), KeyboardButton("🌐 Xalqaro hamkorlik")],
        [KeyboardButton("🚗 Qanday borish mumkin?")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, input_field_placeholder="Quyidagilardan birini tanlang...")

# Start komandasi
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(
        f"Salom {user.first_name}! 👋\n"
        f"Cyber University rasmiy botiga xush kelibsiz!\n\n"
        f"Quyidagi menyudan kerakli bo'limni tanlang:",
        reply_markup=main_keyboard()
    )

# Joylashuv haqida ma'lumot
async def show_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location_text = f"""
{LOCATION}

**Tafsilotlar:**
🏛️ **Binolar:** Zamonaviy o'quv binolari
💻 **Labaratoriyalar:** Ilg'or kompyuter labaratoriyalari
📚 **Kutubxona:** Raqamli kutubxona
🏋️ **Sport majmuasi:** Sport zallari
🍽️ **Oshxona:** To'liq oziq-ovqat xizmati

**Atrof-muhit:**
- Shahar markaziga yaqin
- Transport aloqasi qulay
- Yashil va osoyishta hudud
- Zamonaviy infratuzilma
"""
    await update.message.reply_text(location_text, reply_markup=main_keyboard())

# Qanday borish mumkin
async def how_to_get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    directions_text = f"""
{LOCATION}

**🚗 Avtomobil orqali:**
- Toshkent shahridan - 30-40 daqiqa
- Halq yo'nalishi bo'yicha
- Nurafshon shahri markaziga yaqin

**🚌 Jamoat transporti:**
- Toshkent markazidan avtobuslar
- Shahar ichidagi marshrut taksilar
- Taksi xizmatlari (Yandex, MyTaxi)

**📍 Navigatsiya:**
- Google Maps: "Cyber University Nurafshon"
- Yandex Maps: "Cyber University"
- 2GIS: "Cyber University"

**📞 Aloqa:**
- Telefon: +998 XX XXX XX XX
- Telegram: @cyberuni_uz
- Email: info@cyberuni.uz
"""
    await update.message.reply_text(directions_text, reply_markup=main_keyboard())

# Foydalanuvchi lokatsiyasini qabul qilish
async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location = update.message.location
    user = update.message.from_user
    
    # Foydalanuvchi lokatsiyasiga asoslangan masofa va yo'nalish
    response_text = f"""
📍 **Sizning joylashuvingiz qabul qilindi!**

{LOCATION}

**Sizga qulay yo'nalishlar:**
- 🚗 Taksi bilan: 15-25 daqiqa
- 🚌 Jamoat transporti: 30-40 daqiqa
- 🚶 Piyoda: 1-1.5 soat

**Masofani aniq bilish uchun:**
Google Maps yoki Yandex Maps dan foydalaning:

🗺️ **Google Maps:** 
https://maps.google.com/?q=Nurafshon+Cyber+University

🗺️ **Yandex Maps:**
https://yandex.com/maps/?text=Cyber+University+Nurafshon

📱 **Navigatsiya ilovalari:**
- Google Maps
- Yandex Navigator
- 2GIS
"""
    await update.message.reply_text(response_text, reply_markup=main_keyboard())
    
    # Universitetning taxminiy lokatsiyasini yuborish (opsional)
    # await update.message.reply_location(
    #     latitude=41.0,  # Nurafshon taxminiy kordinatalari
    #     longitude=69.0,
    #     reply_markup=main_keyboard()
    # )

# Universitet haqida ma'lumot (joylashuvni ham qo'shamiz)
async def about_university(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = f"""
🏫 **Cyber University** - O'zbekistonning raqamli kelajagi

{LOCATION}

🎯 **Asosiy maqsad:** 
Kiberxavfsizlik sohasida xalqaro darajada raqobatbardosh mutaxassislar tayyorlash

📚 **Ta'lim tili:** Ingliz tili
⏳ **Muddat:** 1 yil Foundation + 3 yil asosiy ta'lim
🎓 **Kredit-modul tizimi**

**Infratuzilma:**
- Zamonaviy o'quv binolari
- Ilg'or kompyuter labaratoriyalari
- Raqamli kutubxona
- Sport majmuasi
- Talabalar turar joyi
"""
    await update.message.reply_text(text, reply_markup=main_keyboard())

# Kontakt qabul qilish
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    await update.message.reply_text(
        f"Rahmat! Sizning kontaktlaringiz qabul qilindi.\n"
        f"Telefon: {contact.phone_number}\n\n"
        f"{LOCATION}\n"
        f"Qo'shimcha ma'lumot uchun: @cyberuni_uz",
        reply_markup=main_keyboard()
    )

# Xabarlarni qayta ishlash
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "ℹ️ Universitet haqida":
        await about_university(update, context)
    elif text == "🎓 Ta'lim yo'nalishlari":
        await show_courses(update, context)
    elif text == "💰 Grantlar":
        await show_grants(update, context)
    elif text == "🌐 Xalqaro hamkorlik":
        await show_international(update, context)
    elif text == "📍 Manzil" or text == "🚗 Qanday borish mumkin?":
        await how_to_get(update, context)
    elif text == "🔙 Asosiy menyu":
        await back_to_main(update, context)
    else:
        await update.message.reply_text(
            "Tushunmadim, quyidagi tugmalardan foydalaning:",
            reply_markup=main_keyboard()
        )

# Pastdagi funksiyalarni oldingi koddan qo'shing
async def show_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ta'lim yo'nalishlari keyboard
    def courses_keyboard():
        keyboard = [
            [KeyboardButton("🔐 Kiberxavfsizlik"), KeyboardButton("💻 Kompyuter injiniringi")],
            [KeyboardButton("🖥️ Dasturiy injiniring"), KeyboardButton("⚖️ Yurisprudensiya")],
            [KeyboardButton("📊 Menejment"), KeyboardButton("💼 Iqtisodiyot")],
            [KeyboardButton("🔙 Asosiy menyu")]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Quyidagi ta'lim yo'nalishlaridan birini tanlang:",
        reply_markup=courses_keyboard()
    )

async def show_grants(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
💰 **Grant va stipendiyalar:**

🎯 **100 ta davlat granti** - 2025/2026 o'quv yili uchun

🏆 **Sanoat hamkorlari stipendiyalari:**
- IT kompaniyalar tomonidan
- Amaliyot vaqtida maosh
- Ish bilan ta'minlash

📚 **Innovatsion rivojlanish kengashi** stipendiyalari
"""
    await update.message.reply_text(text, reply_markup=main_keyboard())

async def show_international(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🌐 **Xalqaro hamkorlik:**

🤝 **Hamkor universitetlar:**
- AQSH (Stanford, MIT)
- Xitoy (Tsinghua, Peking)
- Yaponiya (Tokyo, Kyoto)
- Janubiy Koreya (KAIST)

🎓 **Imkoniyatlar:**
- Almashinuv dasturlari
- Qo'shma loyihalar
- Xorijiy professorlar
- Xalqaro sertifikatlar
"""
    await update.message.reply_text(text, reply_markup=main_keyboard())

async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Asosiy menyu:",
        reply_markup=main_keyboard()
    )

def main():
    if not BOT_TOKEN:
        print("Bot tokeni topilmadi!")
        return

    application = Application.builder().token(BOT_TOKEN).build()
    
    # Handlerlar
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.CONTACT, contact_handler))
    application.add_handler(MessageHandler(filters.LOCATION, location_handler))
    
    print("Bot ishga tushdi...")
    application.run_polling()

if __name__ == "__main__":
    main()
