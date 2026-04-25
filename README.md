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
## ⚙️ Установка и запуск

### 1. Установи зависимости
pip install django pyTelegramBotAPI

### 2. Применить миграции
python manage.py migrate

### 3. Создать суперпользователя
python manage.py createsuperuser

### 4. Запустить сервер
python manage.py runserver

### 5. Запустить бота
python bot.py

## 👤 Автор
[zhamalzhandos-lab](https://github.com/zhamalzhandos-lab)
