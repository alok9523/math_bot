from telegram import Update
from telegram.ext import CallbackContext
import logging  

logger = logging.getLogger(__name__)
ADMIN_ID = 123456789  # Replace with your Telegram ID  

async def ban_user(update: Update, context: CallbackContext):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /ban <user_id>")
        return

    user_id = context.args[0]
    await update.message.reply_text(f"User {user_id} has been banned (simulated).")
    logger.info(f"Admin {update.message.from_user.id} banned user {user_id}.")