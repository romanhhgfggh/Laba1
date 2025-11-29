import os
from dotenv import load_dotenv

# Завантажуємо змінні з файлу .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Новий код: Встановлюємо змінну середовища для автентифікації Google
# Google Vision API автоматично шукатиме цей файл.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not BOT_TOKEN:
    exit("Помилка: BOT_TOKEN не знайдено у файлі .env")
