"""Module to integrate Telegram bot with Todoist API."""

import os
import telebot
from todoist_api_python.api import TodoistAPI
import logging
import sys

# Configure logging to output to the console
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    stream=sys.stdout)

# Get tokens from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("teletoken")
TODOIST_API_KEY = os.getenv("todoisttoken")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
todoist_api = TodoistAPI(TODOIST_API_KEY)

def create_todoist_task(content):
    """Create a task in Todoist with the given content."""
    try:
        task = todoist_api.add_task(content=content, due_string="Monday", labels=["Links"])
        logging.info(f"Task created: {task.content}")
        return task
    except Exception as error:
        logging.error(f"Error creating task in Todoist: {error}")
        return None

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Handle each message received by the bot."""
    task = create_todoist_task(message.text)
    if task:
        reply_message = f"Task created: {task.content}"
    else:
        reply_message = "Failed to create task in Todoist."
        logging.warning(f"Failed to create task for message: {message.text}")
    bot.reply_to(message, reply_message)

if __name__ == "__main__":
    logging.info("Starting bot polling")
    bot.polling()
    logging.info("Bot polling ended")