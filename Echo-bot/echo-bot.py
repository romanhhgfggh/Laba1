import os
import telebot
from dotenv import load_dotenv

# Завантажуємо змінні оточення (токен)
load_dotenv()
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise RuntimeError("Токен не знайдено! Переконайся, що файл .env існує.")

# Створюємо об'єкт бота
bot = telebot.TeleBot(TOKEN)

# --- Єдина "Точка входу" для повідомлень ---

# Список усіх типів контенту, які ми хочемо "віддзеркалювати"
ALL_CONTENT_TYPES = [
    'text', 'audio', 'document', 'photo', 'sticker', 'video',
    'voice', 'location', 'contact', 'new_chat_members',
    'left_chat_member', 'new_chat_title', 'new_chat_photo',
    'delete_chat_photo', 'group_chat_created',
    'supergroup_chat_created', 'channel_chat_created',
    'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'
]

@bot.message_handler(content_types=ALL_CONTENT_TYPES)
def echo_all_messages(message):
    """
    Цей ОДИН обробник перехоплює ВСІ типи повідомлень
    і просто копіює їх назад користувачу.
    """
    try:
        # Найпростіший спосіб "віддзеркалити" повідомлення - це скопіювати його
        bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
    except Exception as e:
        print(f"Не вдалося скопіювати повідомлення: {e}")

# --- Головна "Точка входу" для скрипта ---

def main():
    """Головна функція для запуску бота."""
    print("Бот запущений...")
    # bot.polling() - це старий метод. 
    # bot.infinity_polling() - більш надійний, він 
    # автоматично перезапускається у разі збоїв.
    bot.infinity_polling()

if __name__ == '__main__':
    main()
