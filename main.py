import telebot
import os

# Railway Variables dan TOKEN olish
TOKEN = os.getenv("TOKEN")

if not TOKEN or ":" not in TOKEN:
    raise ValueError("Bot token noto'g'ri yoki topilmadi")

bot = telebot.TeleBot(TOKEN)

# Uch tilli matn bazasi (expanded with extra menu items and placeholders)
data = {
    "uz": {
        "welcome": "⚜️ Cyber University davlat universiteti botiga xush kelibsiz!",
        "menu": ["👑 Universitet haqida", "💰 Bakalavr", "💸 Magistratura", "💳 Qabul", "🔁 Kontaklar", "📊 Hisobotlar", "📷 QR skaner", "⚙️ Sozlamalar"],
        "about": "⚙️ Cyber University — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
                 "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qaroriga asosan Cyber University tashkil etildi.\n\n"
                 "Qarorni o‘qing! 🫵 https://lex.uz/uz/docs/-7332592",
        "bachelor": "🎓 Bakalavriat yo‘nalishlari:\n"
                    "• Kiberxavfsizlik injiniringi: tarmoq va tizim xavfsizligi\n"
                    "• Kompyuter injiniringi: sun’iy intellekt\n"
                    "• Kiberxavfsizlik injiniringi: internet ashyolari xavfsizligi\n"
                    "• Dasturiy injiniring: amaliy matematika va algoritmlashtirish\n"
                    "• Yurisprudensiya: kiber huquq\n"
                    "• Yurisprudensiya: raqamli kriminalistika\n"
                    "• Menejment: kiberxavfsizlik menejmenti\n"
                    "• Iqtisodiyot: raqamli iqtisodiyot",
        "master": "🎓 Magistratura yo‘nalishlari:\n"
                  "• Axborot xavfsizligi\n"
                  "• Kiber huquq",
        "admission": "📌 Qabul tartibi:\n\n"
                     "Cyber University davlat universiteti ⚜️\n\n"
                     "Eslatma: Prezidentning PF-81-son Farmoniga muvofiq —\n"
                     "bakalavriatga qabul jarayoni ikki bosqichda amalga oshiriladi:\n"
                     "1) Avval test\n"
                     "2) So‘ng tanlov\n\n"
                     "Manba: https://lex.uz/uz/docs/-6937332",
        "contacts": "📞 Kontaktlar:\n\n"
                    "Telegram: Cyber University rasmiy sahifasi\n"
                    "🌐 Veb-sayt: csu.uz\n"
                    "📸 Instagram: instagram.com/csu.uz\n"
                    "📘 Facebook: www.facebook.com/profile.php?id=61577521082631\n"
                    "💼 LinkedIn: www.linkedin.com/company/csu_uz/\n"
                    "☎️ Murojaatlar uchun: 558885555",
        "reports": "📊 Hisobotlar: Bu yerda universitet hisobotlari bo'ladi. (Keling, keyinroq qo'shamiz!)",  # Placeholder
        "qr": "📷 QR skaner: QR kodlarni skanerlash funksiyasi. (Hozircha mavjud emas.)",  # Placeholder
        "settings": "⚙️ Sozlamalar: Bot sozlamalari. (Keyingi versiyada.)",  # Placeholder
        "home": "🏠 Bosh sahifa"
    },
    "ru": {
        "welcome": "⚜️ Добро пожаловать в бот Государственного университета Cyber University!",
        "menu": ["👑 Об университете", "💰 Бакалавриат", "💸 Магистратура", "💳 Прием", "🔁 Контакты", "📊 Отчеты", "📷 QR-сканер", "⚙️ Настройки"],
        "about": "⚙️ Cyber University — современное высшее учебное заведение, открывающее путь в цифровое будущее Узбекистана.\n\n"
                 "На основании Постановления Президента Республики Узбекистан от 20 января 2025 года №PQ–14 был создан Cyber University.\n\n"
                 "Читайте постановление! 🫵 https://lex.uz/ru/docs/-7332592",
        "bachelor": "🎓 Направления бакалавриата:\n"
                    "• Кибербезопасность: защита сетей и систем\n"
                    "• Компьютерная инженерия: искусственный интеллект\n"
                    "• Кибербезопасность: безопасность интернета вещей\n"
                    "• Программная инженерия: прикладная математика и алгоритмы\n"
                    "• Юриспруденция: киберправо\n"
                    "• Юриспруденция: цифровая криминалистика\n"
                    "• Менеджмент: управление кибербезопасностью\n"
                    "• Экономика: цифровая экономика",
        "master": "🎓 Магистратура:\n"
                  "• Информационная безопасность\n"
                  "• Киберправо",
        "admission": "📌 Прием:\n\n"
                     "Cyber University ⚜️\n\n"
                     "Согласно Указу Президента №PF-81 прием в бакалавриат осуществляется в два этапа:\n"
                     "1) Сначала тест\n"
                     "2) Затем конкурс\n\n"
                     "Источник: https://lex.uz/ru/docs/-6937332",
        "contacts": "📞 Контакты:\n\n"
                    "Telegram: официальный канал Cyber University\n"
                    "🌐 Сайт: csu.uz\n"
                    "📸 Instagram: instagram.com/csu.uz\n"
                    "📘 Facebook: www.facebook.com/profile.php?id=61577521082631\n"
                    "💼 LinkedIn: www.linkedin.com/company/csu_uz/\n"
                    "☎️ Телефон: 558885555",
        "reports": "📊 Отчеты: Здесь будут отчеты университета. (Добавим позже!)",  # Placeholder
        "qr": "📷 QR-сканер: Функция сканирования QR-кодов. (Пока недоступна.)",  # Placeholder
        "settings": "⚙️ Настройки: Настройки бота. (В следующей версии.)",  # Placeholder
        "home": "🏠 На главную"
    },
    "en": {
        "welcome": "⚜️ Welcome to Cyber University State University bot!",
        "menu": ["👑 About University", "💰 Bachelor Programs", "💸 Master Programs", "💳 Admission", "🔁 Contacts", "📊 Reports", "📷 QR Scanner", "⚙️ Settings"],
        "about": "⚙️ Cyber University — a modern higher education institution opening the way to Uzbekistan's digital future.\n\n"
                 "Cyber University was established based on the Presidential Decree of the Republic of Uzbekistan No. PQ–14, dated January 20, 2025.\n\n"
                 "Read the decree! 🫵 https://lex.uz/en/docs/-7332592",
        "bachelor": "🎓 Bachelor Programs:\n"
                    "• Cybersecurity Engineering: network and system security\n"
                    "• Computer Engineering: artificial intelligence\n"
                    "• Cybersecurity Engineering: IoT security\n"
                    "• Software Engineering: applied mathematics and algorithms\n"
                    "• Law: cyber law\n"
                    "• Law: digital forensics\n"
                    "• Management: cybersecurity management\n"
                    "• Economics: digital economy",
        "master": "🎓 Master Programs:\n"
                  "• Information Security\n"
                  "• Cyber Law",
        "admission": "📌 Admission:\n\n"
                     "Cyber University ⚜️\n\n"
                     "According to Presidential Decree PF-81, admission to bachelor’s programs is carried out in two stages:\n"
                     "1) First test\n"
                     "2) Then selection\n\n"
                     "Source: https://lex.uz/en/docs/-6937332",
        "contacts": "📞 Contacts:\n\n"
                    "Telegram: official Cyber University channel\n"
                    "🌐 Website: csu.uz\n"
                    "📸 Instagram: instagram.com/csu.uz\n"
                    "📘 Facebook: www.facebook.com/profile.php?id=61577521082631\n"
                    "💼 LinkedIn: www.linkedin.com/company/csu_uz/\n"
                    "☎️ Phone: 558885555",
        "reports": "📊 Reports: University reports will be here. (We'll add later!)",  # Placeholder
        "qr": "📷 QR Scanner: QR code scanning feature. (Not available yet.)",  # Placeholder
        "settings": "⚙️ Settings: Bot settings. (In the next version.)",  # Placeholder
        "home": "🏠 Home"
    }
}

# Foydalanuvchi tili saqlanadi
user_lang = {}

def main_menu(chat_id, lang):
    # Create expanded 2-column keyboard to match the original function's layout
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_items = data[lang]["menu"]
    for i in range(0, len(menu_items), 2):
        if i + 1 < len(menu_items):
            keyboard.row(menu_items[i], menu_items[i + 1])
        else:
            keyboard.row(menu_items[i])  # For odd number of items
    bot.send_message(chat_id, data[lang]["welcome"], reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("O‘zbekcha 🇺🇿", "Русский 🇷🇺", "English 🇬🇧")
    bot.send_message(message.chat.id,
                     "Tilni tanlang / Выберите язык / Choose language:",
                     reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text in ["O‘zbekcha 🇺🇿", "Русский 🇷🇺", "English 🇬🇧"])
def set_language(message):
    lang_map = {
        "O‘zbekcha 🇺🇿": "uz",
        "Русский 🇷🇺": "ru",
        "English 🇬🇧": "en"
    }
    user_lang[message.chat.id] = lang_map[message.text]
    lang = user_lang[message.chat.id]
    main_menu(message.chat.id, lang)

@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    lang = user_lang.get(message.chat.id, "uz")
    menu_items = data[lang]["menu"]
    
    if message.text in menu_items:
        text = ""
        if "Universitet haqida" in message.text or "Об университете" in message.text or "About University" in message.text:
            text = data[lang]["about"]
        elif "Bakalavr" in message.text or "Бакалавриат" in message.text or "Bachelor Programs" in message.text:
            text = data[lang]["bachelor"]
        elif "Magistratura" in message.text or "Магистратура" in message.text or "Master Programs" in message.text:
            text = data[lang]["master"]
        elif "Qabul" in message.text or "Прием" in message.text or "Admission" in message.text:
            text = data[lang]["admission"]
        elif "Kontaklar" in message.text or "Контакты" in message.text or "Contacts" in message.text:
            text = data[lang]["contacts"]
        elif "Hisobotlar" in message.text or "Отчеты" in message.text or "Reports" in message.text:
            text = data[lang]["reports"]
        elif "QR skaner" in message.text or "QR-сканер" in message.text or "QR Scanner" in message.text:
            text = data[lang]["qr"]
        elif "Sozlamalar" in message.text or "Настройки" in message.text or "Settings" in message.text:
            text = data[lang]["settings"]

        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(data[lang]["home"])
        bot.send_message(message.chat.id, text, reply_markup=keyboard)

    elif message.text == data[lang]["home"]:
        main_menu(message.chat.id, lang)

if __name__ == "__main__":
    print("Bot ishga tushmoqda...")  # Debug print
    bot.polling(none_stop=True)
