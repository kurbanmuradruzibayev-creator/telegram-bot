import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Keyboard konstantalari
MAIN_MENU, COURSES, CONTACT, ABOUT = range(4)

# Asosiy keyboard
def main_keyboard():
    keyboard = [
        [KeyboardButton("🎓 Ta'lim yo'nalishlari"), KeyboardButton("ℹ️ Universitet haqida")],
        [KeyboardButton("📞 Aloqa", request_contact=True), KeyboardButton("📍 Manzil", request_location=True)],
        [KeyboardButton("💰 Grantlar"), KeyboardButton("🌐 Xalqaro hamkorlik")]
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

# Universitet haqida
async def about_university(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🏫 **Cyber University** - O'zbekistonning raqamli kelajagi

🎯 **Asosiy maqsad:** 
Kiberxavfsizlik sohasida xalqaro darajada raqobatbardosh mutaxassislar tayyorlash

📚 **Ta'lim tili:** Ingliz tili
⏳ **Muddat:** 1 yil Foundation + 3 yil asosiy ta'lim
🎓 **Kredit-modul tizimi**

📍 **Manzil:** Toshkent viloyati, Nurafshon shahri
    """
    await update.message.reply_text(text, reply_markup=main_keyboard())

# Ta'lim yo'nalishlari keyboard
def courses_keyboard():
    keyboard = [
        [KeyboardButton("🔐 Kiberxavfsizlik"), KeyboardButton("💻 Kompyuter injiniringi")],
        [KeyboardButton("🖥️ Dasturiy injiniring"), KeyboardButton("⚖️ Yurisprudensiya")],
        [KeyboardButton("📊 Menejment"), KeyboardButton("💼 Iqtisodiyot")],
        [KeyboardButton("🔙 Asosiy menyu")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Ta'lim yo'nalishlari
async def show_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Quyidagi ta'lim yo'nalishlaridan birini tanlang:",
        reply_markup=courses_keyboard()
    )

# Har bir kurs haqida ma'lumot
async def course_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    course = update.message.text
    info = ""
    
    if course == "🔐 Kiberxavfsizlik":
        info = """
🔐 **Kiberxavfsizlik injiniringi**

📖 **Asosiy fanlar:**
- Tarmoq xavfsizligi
- Ma'lumotlar bazasi himoyasi
- Kriptografiya
- Kiberhujumlarni aniqlash va oldini olish

💼 **Ish joylari:**
- Bank va moliya institutlari
- Davlat idoralari
- IT kompaniyalar
- Telekommunikasyon kompaniyalari
        """
    elif course == "💻 Kompyuter injiniringi":
        info = """
💻 **Kompyuter injiniringi**

📖 **Asosiy fanlar:**
- Kompyuter arxitekturasi
- Operatsion tizimlar
- Mikroprotsessorlar
- Mobil qurilmalar

💼 **Ish joylari:**
- Elektronika korxonalari
- Telekommunikasyon
- IT kompaniyalar
- Ishlab chiqarish korxonalari
        """
    elif course == "🖥️ Dasturiy injiniring":
        info = """
🖥️ **Dasturiy injiniring**

📖 **Asosiy fanlar:**
- Web dasturlash
- Mobil ilovalar
- Sun'iy intellekt
- Ma'lumotlar tahlili

💼 **Ish joylari:**
- Dasturiy ta'minot kompaniyalari
- Startuplar
- Bank va moliya
- Turli soha korxonalari
        """
    elif course == "⚖️ Yurisprudensiya":
        info = """
⚖️ **Yurisprudensiya**

📖 **Asosiy fanlar:**
- Axborot huquqi
- Kiberhuquq
- Intellektual mulk
- Raqamli iqtisod huquqi

💼 **Ish joylari:**
- Sud tizimi
- Advokatlik
- Korporativ huquq
- Davlat idoralari
        """
    elif course == "📊 Menejment":
        info = """
📊 **Menejment**

📖 **Asosiy fanlar:**
- IT loyihalar boshqaruvi
- Biznes tahlili
- Raqamli marketing
- Strategik menejment

💼 **Ish joylari:**
- Menejment konsalting
- IT kompaniyalar
- Bank va moliya
- Ishlab chiqarish korxonalari
        """
    elif course == "💼 Iqtisodiyot":
        info = """
💼 **Iqtisodiyot**

📖 **Asosiy fanlar:**
- Raqamli iqtisod
- Kripto iqtisod
- Fintech
- Makroiqtisod

💼 **Ish joylari:**
- Bank va moliya
- Investitsiya kompaniyalari
- Davlat idoralari
- Xalqaro tashkilotlar
        """
    
    if info:
        await update.message.reply_text(info, reply_markup=courses_keyboard())

# Grantlar haqida
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

# Xalqaro hamkorlik
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

# Kontakt qabul qilish
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    await update.message.reply_text(
        f"Rahmat! Sizning kontaktlaringiz qabul qilindi.\n"
        f"Telefon: {contact.phone_number}",
        reply_markup=main_keyboard()
    )

# Lokatsiya qabul qilish
async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.location
    await update.message.reply_text(
        "Manzilingiz qabul qilindi! Universitet Toshkent viloyati, Nurafshon shahrida joylashgan.",
        reply_markup=main_keyboard()
    )

# Asosiy menyuga qaytish
async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Asosiy menyu:",
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
    elif text == "🔙 Asosiy menyu":
        await back_to_main(update, context)
    elif text in ["🔐 Kiberxavfsizlik", "💻 Kompyuter injiniringi", "🖥️ Dasturiy injiniring", 
                  "⚖️ Yurisprudensiya", "📊 Menejment", "💼 Iqtisodiyot"]:
        await course_info(update, context)
    else:
        await update.message.reply_text(
            "Tushunmadim, quyidagi tugmalardan foydalaning:",
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
