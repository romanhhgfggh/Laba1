import sys
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher

# --- МАГІЧНИЙ БЛОК (ВИПРАВЛЯЄ ПОМИЛКУ ІМПОРТУ) ---
# Це змушує Python шукати папки (genius_api, handlers) саме там, де лежить Main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# ------------------------------------------------

# Тепер імпорти точно спрацюють
from config.config import BOT_TOKEN
from handlers.handlers import router as main_router

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запускається... (Імпорти успішні!)")

    # Створюємо бота та диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Підключаємо роутер
    dp.include_router(main_router)

    # Видаляємо старі оновлення і запускаємо
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот зупинений.")
    except Exception as e:
        print(f"Критична помилка при запуску: {e}")
        input("Натисни Enter, щоб вийти...")