from telegram import Update
from telegram.ext import CallbackContext

async def chat(update: Update, context: CallbackContext):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")