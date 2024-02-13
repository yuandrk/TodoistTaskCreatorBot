"""Module to integrate Telegram bot with Todoist API."""

import os
import telebot
import requests

# Get tokens from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELE_TOKEN')
TODOIST_API_KEY = os.getenv('TODOIST_TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def create_todoist_task(content):
    """Create a task in Todoist with the given content.

    Args:
        content (str): Content of the task to be created.

    Returns:
        The response from Todoist API if successful, None otherwise.
    """
    url = 'https://api.todoist.com/rest/v2/tasks'
    headers = {
        'Authorization': f'Bearer {TODOIST_API_KEY}',
        'Content-Type': 'application/json',
        'priority': '4',
        'description': 'content'
    }
    data = {'content': content}
    response = requests.post(url, headers=headers, json=data, timeout=10)
    if response.status_code == 200:
        return response.json()
    print(f'Error: {response.status_code}, {response.text}')
    return None

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Handle each message received by the bot."""
    task = create_todoist_task(message.text)
    reply_message = f"Задачу створено: {task['content']}" if task else "Не вдалося створити задачу у Todoist."
    bot.reply_to(message, reply_message)

if __name__ == "__main__":
    bot.polling()
