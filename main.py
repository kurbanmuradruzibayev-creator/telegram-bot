import telebot
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get TOKEN from environment variables
TOKEN = os.getenv("TOKEN")
if not TOKEN or ":" not in TOKEN:
    logging.error("Bot token is invalid or not found")
    raise ValueError("Bot token noto‘g‘ri yoki topilmadi")

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Multilingual data with sub-items for sections
data = {
    "uz": {
        "welcome": "⚜️ Cyber University davlat universiteti botiga xush kelibsiz!",
        "menu": ["👑 Universitet haqida", "💳 Aloqa", "💸 Magistratura", "💰 Bakalavr"],
        "about": "⚙️ Cyber University — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
                 "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qaroriga asosan Cyber University tashkil etildi.\n\n"
                 "Qarorni o‘qing! 🫵 https://lex.uz/uz/docs/-7332592",
        "contact": "📞 Aloqa:\n\n"
                   "Telegram: Cyber University rasmiy sahifasi\n"
                   "🌐 Veb-sayt: csu.uz\n"
                   "📸 Instagram: instagram.com/csu.uz\n"
                   "📘 Facebook: www.facebook.com/profile.php?id=61577521082631\n"
                   "💼 LinkedIn: www.linkedin.com/company/csu_uz/\n"
                   "☎️ Murojaatlar uchun: 558885555",
        "bachelor": {
            "title": "🎓 Bakalavriat yo‘nalishlari:",
            "items": [
                {"name": "Kiberxavfsizlik injiniringi: tarmoq va tizim xavfsizligi", "desc": "Tarmoq va tizim xavfsizligi bo‘yicha mutaxassislar tayyorlash."},
                {"name": "Kompyuter injiniringi: sun’iy intellekt", "desc": "Sun’iy intellekt va mashinaviy o‘qitish bo‘yicha chuqur bilimlar."},
                {"name": "Kiberxavfsizlik injiniringi: internet ashyolari xavfsizligi", "desc": "IoT qurilmalarini xavfsizligini ta’minlash."},
                {"name": "Dasturiy injiniring: amaliy matematika va algoritmlashtirish", "desc": "Algoritmlar va dasturiy ta’minot ishlab chiqish."},
                {"name": "Yurisprudensiya: kiber huquq", "desc": "Raqamli muhitda huquqiy masalalar bo‘yicha ta’lim."},
                {"name": "Yurisprudensiya: raqamli kriminalistika", "desc": "Kiberjinoyatlarni tergov qilish bo‘yicha mutaxassislik."},
                {"name": "Menejment: kiberxavfsizlik menejmenti", "desc": "Kiberxavfsizlikni boshqarish va tashkil qilish."},
                {"name": "Iqtisodiyot: raqamli iqtisodiyot", "desc": "Raqamli iqtisodiyot va blokcheyn texnologiyalari."}
            ]
        },
        "master": {
            "title": "🎓 Magistratura yo‘nalishlari:",
            "items": [
                {"name": "Axborot xavfsizligi", "desc": "Axborot tizimlarini himoya qilish bo‘yicha chuqur bilimlar."},
                {"name": "Kiber huquq", "desc": "Raqamli huquq va kiberxavfsizlik qonunchiligi bo‘yicha ta’lim."}
            ]
        },
        "home": "🏠 Bosh sahifa",
        "back": "⬅️ Orqaga"
    },
    "ru": {
        "welcome": "⚜️ Добро пожаловать в бот Государственного университета Cyber University!",
        "menu": ["👑 Об университете", "💳 Контакты", "💸 Магистратура", "💰 Бакалавриат"],
        "about": "⚙️ Cyber University — современное высшее учебное заведение, открывающее путь в цифровое будущее Узбекистана.\n\n"
                 "На основании Постановления Президента Республики Узбекистан от 20 января 2025 года №PQ–14 был создан Cyber University.\n\n"
                 "Читайте постановление! 🫵 https://lex.uz/ru/docs/-7332592",
        "contact": "📞 Контакты:\n\n"
                   "Telegram: официальный канал Cyber University\n"
                   "🌐 Сайт: csu.uz\n"
                   "📸 Instagram: instagram.com/csu.uz\n"
                   "📘 Facebook: www.facebook.com/profile.php?id=61577521082631\n"
                   "💼 LinkedIn: www.linkedin.com/company/csu_uz/\n"
                   "☎️ Телефон: 558885555",
        "bachelor": {
            "title": "🎓 Направления бакалавриата:",
            "items": [
                {"name": "Кибербезопасность: защита сетей и систем", "desc": "Подготовка специалистов по защите сетей и систем."},
                {"name": "Компьютерная инженерия: искусственный интеллект", "desc": "Глубокие знания в области искусственного интеллекта и машинного обучения."},
                {"name": "Кибербезопасность: безопасность интернета вещей", "desc": "Обеспечение безопасности устройств IoT."},
                {"name": "Программная инженерия: прикладная математика и алгоритмы", "desc": "Алгоритмы и разработка программного обеспечения."},
                {"name": "Юриспруденция: киберправо", "desc": "Обучение правовым аспектам цифровой среды."},
                {"name": "Юриспруденция: цифровая криминалистика", "desc": "Специализация по расследованию киберпреступлений."},
                {"name": "Менеджмент: управление кибербезопасностью", "desc": "Управление и организация кибербезопасности."},
                {"name": "Экономика: цифровая экономика", "desc": "Цифровая экономика и технологии блокчейн."}
            ]
        },
        "master": {
            "title": "🎓 Магистратура:",
            "items": [
                {"name": "Информационная безопасность", "desc": "Глубокие знания по защите информационных систем."},
                {"name": "Киберправо", "desc": "Обучение законодательству в области кибербезопасности."}
            ]
        },
        "home": "🏠 На главную",
        "back": "⬅️ Назад"
    },
    "en": {
        "welcome": "⚜️ Welcome to Cyber University State University bot!",
        "menu": ["👑 About University", "💳 Contact", "💸 Master Programs", "💰 Bachelor Programs"],
        "about": "⚙️ Cyber University — a modern higher education institution opening the way to Uzbekistan's digital future.\n\n"
                 "Cyber University was established based on the Presidential Decree of the Republic of Uzbekistan No. PQ–14, dated January 20, 2025.\n\n"
                 "Read the decree! 🫵 https://lex.uz/en/docs/-7332592",
        "contact": "📞 Contact:\n\n"
                   "Telegram: official Cyber University channel\n"
                   "🌐 Website: csu.uz\n"
                   "📸 Instagram: instagram.com/csu.uz\n"
                   "📘 Facebook: www.facebook.com/profile.php?id=61577521082631\n"
                   "💼 LinkedIn: www.linkedin.com/company/csu_uz/\n"
                   "☎️ Phone: 558885555",
        "bachelor": {
            "title": "🎓 Bachelor Programs:",
            "items": [
                {"name": "Cybersecurity Engineering: network and system security", "desc": "Training specialists in network and system security."},
                {"name": "Computer Engineering: artificial intelligence", "desc": "In-depth knowledge in artificial intelligence and machine learning."},
                {"name": "Cybersecurity Engineering: IoT security", "desc": "Ensuring the security of IoT devices."},
                {"name": "Software Engineering: applied mathematics and algorithms", "desc": "Algorithms and software development."},
                {"name": "Law: cyber law", "desc": "Education on legal aspects of the digital environment."},
                {"name": "Law: digital forensics", "desc": "Specialization in investigating cybercrimes."},
                {"name": "Management: cybersecurity management", "desc": "Managing and organizing cybersecurity."},
                {"name": "Economics: digital economy", "desc": "Digital economy and blockchain technologies."}
            ]
        },
        "master": {
            "title": "🎓 Master Programs:",
            "items": [
                {"name": "Information Security", "desc": "In-depth knowledge in protecting information systems."},
                {"name": "Cyber Law", "desc": "Education on cybersecurity legislation."}
            ]
        },
        "home": "🏠 Home",
        "back": "⬅️ Back"
    }
}

# Store user language and current menu state
user_state = {}

def main_menu(chat_id, lang):
    """Display the main menu in the specified language."""
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(data[lang]["menu"][0], data[lang]["menu"][1])  # 👑 Universitet haqida, 💳 Aloqa
    keyboard.row(data[lang]["menu"][2], data[lang]["menu"][3])  # 💸 Magistratura, 💰 Bakalavr
    bot.send_message(chat_id, data[lang]["welcome"], reply_markup=keyboard)
    user_state[chat_id] = {"lang": lang, "menu": "main"}
    logging.info(f"Main menu displayed for chat_id: {chat_id}, lang: {lang}")

def sub_menu(chat_id, lang, section):
    """Display a sub-menu for sections with multiple items (e.g., bachelor, master)."""
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for item in data[lang][section]["items"]:
        keyboard.add(item["name"])
    keyboard.add(data[lang]["back"])
    bot.send_message(chat_id, data[lang][section]["title"], reply_markup=keyboard)
    user_state[chat_id]["menu"] = section
    logging.info(f"Sub-menu '{section}' displayed for chat_id: {chat_id}")

@bot.message_handler(commands=['start'])
def start(message):
    """Handle the /start command to prompt language selection."""
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("O‘zbekcha 🇺🇿", "Русский 🇷🇺", "English 🇬🇧")
    bot.send_message(message.chat.id,
                     "Tilni tanlang / Выберите язык / Choose language:",
                     reply_markup=keyboard)
    logging.info(f"Start command received for chat_id: {message.chat.id}")

@bot.message_handler(func=lambda m: m.text in ["O‘zbekcha 🇺🇿", "Русский 🇷🇺", "English 🇬🇧"])
def set_language(message):
    """Set the user's language preference and show the main menu."""
    lang_map = {
        "O‘zbekcha 🇺🇿": "uz",
        "Русский 🇷🇺": "ru",
        "English 🇬🇧": "en"
    }
    chat_id = message.chat.id
    user_state[chat_id] = {"lang": lang_map[message.text], "menu": "main"}
    main_menu(chat_id, user_state[chat_id]["lang"])
    logging.info(f"Language set to {user_state[chat_id]['lang']} for chat_id: {chat_id}")

@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    """Handle menu and sub-menu selections."""
    chat_id = message.chat.id
    if chat_id not in user_state:
        start(message)
        return

    lang = user_state[chat_id]["lang"]
    current_menu = user_state[chat_id]["menu"]

    # Handle main menu selections
    if current_menu == "main":
        if message.text in data[lang]["menu"]:
            if message.text == data[lang]["menu"][0]:  # About
                bot.send_message(chat_id, data[lang]["about"], reply_markup=create_back_keyboard(lang))
                user_state[chat_id]["menu"] = "about"
            elif message.text == data[lang]["menu"][1]:  # Contact
                bot.send_message(chat_id, data[lang]["contact"], reply_markup=create_back_keyboard(lang))
                user_state[chat_id]["menu"] = "contact"
            elif message.text == data[lang]["menu"][2]:  # Master
                sub_menu(chat_id, lang, "master")
            elif message.text == data[lang]["menu"][3]:  # Bachelor
                sub_menu(chat_id, lang, "bachelor")
            logging.info(f"Main menu item '{message.text}' selected for chat_id: {chat_id}")
        else:
            send_invalid_input_message(chat_id, lang)
    # Handle sub-menu selections
    elif current_menu in ["bachelor", "master"]:
        for item in data[lang][current_menu]["items"]:
            if message.text == item["name"]:
                bot.send_message(chat_id, f"{item['name']}:\n{item['desc']}", reply_markup=create_back_keyboard(lang))
                logging.info(f"Sub-menu item '{message.text}' selected for chat_id: {chat_id}")
                return
        if message.text == data[lang]["back"]:
            main_menu(chat_id, lang)
        else:
            send_invalid_input_message(chat_id, lang)
    # Handle back navigation
    elif message.text == data[lang]["back"]:
        main_menu(chat_id, lang)
    else:
        send_invalid_input_message(chat_id, lang)

def create_back_keyboard(lang):
    """Create a keyboard with a single Back button."""
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(data[lang]["back"])
    return keyboard

def send_invalid_input_message(chat_id, lang):
    """Send a message for invalid input."""
    messages = {
        "uz": "Iltimos, menyudan biror variantni tanlang.",
        "ru": "Пожалуйста, выберите вариант из меню.",
        "en": "Please select an option from the menu."
    }
    bot.send_message(chat_id, messages[lang])
    logging.warning(f"Invalid input received: {messages[lang]} from chat_id: {chat_id}")

if __name__ == "__main__":
    try:
        logging.info("Starting bot polling...")
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Bot polling failed: {str(e)}")
        raise
