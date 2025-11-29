from aiogram import Router, F, Bot
from aiogram.types import Message, ContentType
from aiogram.filters import CommandStart
import io

# Імпортуємо функцію "ШІ"
from genius_api.genius_api import analyze_image_and_find_movie

router = Router()

# --- 1. Обробник команди /start ---
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привіт! Я КіноШукач. Надішли мені кадр з фільму, і я спробую його знайти.")

# --- 2. Обробник ФОТО (Головний функціонал) ---
@router.message(F.content_type == ContentType.PHOTO)
async def handle_photo(message: Message, bot: Bot):
    await message.answer("Прийняв кадр. Аналізую через ШІ Google Vision... ")

    try:
        # Завантажуємо файл у пам'ять
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        image_buffer = io.BytesIO()
        await bot.download_file(file_info.file_path, image_buffer)
        image_bytes = image_buffer.getvalue()

        # Викликаємо ШІ
        movie_guess = await analyze_image_and_find_movie(image_bytes)

        # Відправляємо результат
        await message.answer(movie_guess)

    except Exception as e:
        print(f"Помилка: {e}")
        await message.answer("Щось пішло не так під час обробки фото.")

# --- 3. Обробник ВСЬОГО ІНШОГО (Текст, файли, стікери) ---
# Цей код спрацює, якщо це не /start і не фото
@router.message()
async def handle_any_other_content(message: Message):
    if message.content_type == ContentType.TEXT:
        await message.answer("Я бачу твій текст, але я розумію ТІЛЬКИ ФОТО кадрів з фільмів. Надішли картинку!")
    else:
        await message.answer(f"Ти надіслав {message.content_type}. Будь ласка, надішли звичайне зображення.")