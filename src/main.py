"""Module to integrate Telegram bot with Todoist API."""

import logging
import os
import sys
from typing import Optional

import telebot
from todoist_api_python.api import TodoistAPI
from telebot.types import Message

class Config:
    """Configuration class to handle environment variables and setup."""
    TELEGRAM_BOT_TOKEN = os.getenv("teletoken")
    TODOIST_API_KEY = os.getenv("todoisttoken")

    @classmethod
    def validate(cls) -> bool:
        """Validate that all required environment variables are set."""
        if not all([cls.TELEGRAM_BOT_TOKEN, cls.TODOIST_API_KEY]):
            logging.error("Missing required environment variables")
            return False
        return True

class TodoistService:
    """Service class to handle Todoist API operations."""
    def __init__(self, api_key: str):
        self.api = TodoistAPI(api_key)

    def create_task(self, content: str) -> Optional[dict]:
        """Create a task in Todoist with the given content."""
        try:
            task = self.api.add_task(content=content, labels=["Links"])
            logging.info("Task created: %s", task.content)
            return task
        except Exception as error:
            logging.error("Error creating task in Todoist: %s", error)
            return None

class TelegramBot:
    """Telegram bot class to handle message processing."""
    def __init__(self, token: str, todoist_service: TodoistService):
        self.bot = telebot.TeleBot(token)
        self.todoist_service = todoist_service
        self._register_handlers()

    def _register_handlers(self) -> None:
        """Register message handlers."""
        self.bot.message_handler(func=lambda message: True)(self.handle_message)

    def handle_message(self, message: Message) -> None:
        """Handle each message received by the bot."""
        task = self.todoist_service.create_task(message.text)
        reply_message = (
            f"Task created: {task.content}" if task
            else "Failed to create task in Todoist."
        )
        
        if not task:
            logging.warning("Failed to create task for message: %s", message.text)
        
        self.bot.reply_to(message, reply_message)

    def start(self) -> None:
        """Start the bot polling."""
        logging.info("Starting bot polling")
        self.bot.polling()
        logging.info("Bot polling ended")

def setup_logging() -> None:
    """Configure logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout
    )

def main() -> None:
    """Main function to run the application."""
    setup_logging()

    if not Config.validate():
        sys.exit(1)

    todoist_service = TodoistService(Config.TODOIST_API_KEY)
    bot = TelegramBot(Config.TELEGRAM_BOT_TOKEN, todoist_service)
    
    try:
        bot.start()
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
    except Exception as error:
        logging.error("Unexpected error: %s", error)
        sys.exit(1)

if __name__ == "__main__":
    main()

