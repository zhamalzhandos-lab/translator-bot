import os
import django
import sys

sys.path.insert(0, '/content/translator_project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'translator_project.settings')
django.setup()

import telebot
import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from bot_admin.models import UserQuery

TOKEN = "8466601850:AAFAD2xl8vBtU4lWCmFKcfkTiadjvyQZgjk"
bot = telebot.TeleBot(TOKEN)
users_mode = {}

with open("/content/slovar.json", "r", encoding="utf-8") as f:
    slovar = json.load(f)

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("📖 Переводчик"), KeyboardButton("❓ Помощь"))
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-словарь 📚", reply_markup=main_keyboard())

@bot.message_handler(func=lambda m: m.text == "❓ Помощь")
def help_btn(message):
    bot.send_message(message.chat.id, "/start - запуск\n📖 Переводчик - начать перевод")

@bot.message_handler(func=lambda m: m.text == "📖 Переводчик")
def translation_btn(message):
    users_mode[message.chat.id] = True
    bot.send_message(message.chat.id, "Напиши слово на английском 🇬🇧")

@bot.message_handler(func=lambda m: True)
def translate(message):
    chat_id = message.chat.id
    if not users_mode.get(chat_id):
        return

    word = message.text.lower()
    translation = slovar.get(word, "")
    found = word in slovar

    UserQuery.objects.create(
        telegram_id=chat_id,
        username=message.from_user.username,
        word=word,
        translation=translation if found else "",
        found=found
    )

    if found:
        bot.send_message(chat_id, f"Перевод: {translation}")
    else:
        bot.send_message(chat_id, "Нет такого слова ❌")

print("Бот запущен...")
bot.polling()
