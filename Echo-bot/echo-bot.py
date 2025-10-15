import telebot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise RuntimeError("TOKEN not found")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def echo_text(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    # Відправляємо те саме фото
    bot.send_photo(message.chat.id, message.photo[-1].file_id, caption=message.caption)

@bot.message_handler(content_types=['video'])
def echo_video(message):
    # Відправляємо те саме відео
    bot.send_video(message.chat.id, message.video.file_id, caption=message.caption)

@bot.message_handler(content_types=['document'])
def echo_document(message):
    # Відправляємо той самий документ
    bot.send_document(message.chat.id, message.document.file_id, caption=message.caption)

@bot.message_handler(content_types=['audio'])
def echo_audio(message):
    # Відправляємо той самий аудіофайл
    bot.send_audio(message.chat.id, message.audio.file_id, caption=message.caption)

@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    # Відправляємо ту саму голосову повідомлення
    bot.send_voice(message.chat.id, message.voice.file_id)

@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    # Відправляємо той самий стікер
    bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(content_types=['location'])
def echo_location(message):
    # Відправляємо ту саму локацію
    bot.send_location(message.chat.id, message.location.latitude, message.location.longitude)

if __name__ == '__main__':
    print("Бот запущений...")
    bot.polling()