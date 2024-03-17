"""Module to integrate Telegram bot with Todoist API."""

import os
from todoist_api_python.api import TodoistAPI
import telebot

# Get tokens from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELE_TOKEN")
TODOIST_API_KEY = os.getenv("todoisttoken") 

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
todoist_api = TodoistAPI(TODOIST_API_KEY)


def create_todoist_task(content):
    """Create a task in Todoist with the given content.

    Args:
        content (str): Content of the task to be created.

    Returns:
        The response from Todoist API if successful, None otherwise.
    """
    try:
        task = todoist_api.add_task(content=content)
        return task  # The add_task method returns a Task object if successful
    except Exception as error:
        print(f"Error creating task in Todoist: {error}")
        return None


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Handle each message received by the bot."""
    task = create_todoist_task(message.text)
    if task:
        reply_message = f"Task is created: {task.content}"
    else:
        reply_message = "Problem with creat task"
    bot.reply_to(message, reply_message)


if __name__ == "__main__":
    bot.polling()
