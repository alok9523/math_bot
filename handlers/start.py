from telegram import Update
from telegram.ext import CallbackContext
import logging  

logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_message = f"Hello {user.first_name}! Welcome to Advanced Telegram Bot.\n\n"
    welcome_message += "Use the following commands:\n"
    welcome_message += "/wolfram <query> - Query Wolfram Alpha\n"
    welcome_message += "/ai <query> - Get AI-powered responses\n"
    welcome_message += "/solve <equation> - Solve math equations\n"
    await update.message.reply_text(welcome_message)
    logger.info(f"User {user.id} started the bot.")