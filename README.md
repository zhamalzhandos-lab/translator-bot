# 📚 Translator Bot — Telegram бот-словарь

Telegram бот-переводчик с Django админкой для просмотра истории запросов.

## 🚀 Возможности

- Перевод слов с английского языка
- Клавиатура с кнопками
- Django админка с историей всех запросов пользователей
- Сохранение запросов в базу данных

## 🛠 Технологии

- Python 3.12
- pyTelegramBotAPI
- Django 6.0
- SQLite

## 📁 Структура проекта
translator-bot/
├── bot_admin/          # Django приложение
│   ├── models.py       # Модель UserQuery
│   └── admin.py        # Настройка админки
├── translator_project/ # Настройки Django
├── bot.py              # Telegram бот
├── manage.py           # Управление Django
└── slovar.json         # Словарь слов

## 👤 Автор
[zhamalzhandos-lab](https://github.com/zhamalzhandos-lab)
