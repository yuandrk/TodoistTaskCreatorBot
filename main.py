import os
import telebot
import requests

# Отримання токенів з змінних середовища
TELEGRAM_BOT_TOKEN = os.getenv('TELE_TOKEN')
TODOIST_API_KEY = os.getenv('TODOIST_TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Створюємо функцію для створення задачі у Todoist  
def create_todoist_task(content):
    url = 'https://api.todoist.com/rest/v2/tasks'
    headers = {
        'Authorization': f'Bearer {TODOIST_API_KEY}',
        'Content-Type': 'application/json',
        'priority': '4',
        'description': f'content'

    }
    data = {
        'content': content
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return None




##Обробляє кожне повідомлення, що отримане ботом
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    task = create_todoist_task(message.text)
    if task is not None:
        bot.reply_to(message, f"Задачу створено: {task['content']}")
    else:
        bot.reply_to(message, "Не вдалося створити задачу у Todoist.")

bot.polling()
