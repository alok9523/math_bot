import putter
from telegram import Update
from telegram.ext import CallbackContext
from config import AI_ROUTER_API_KEY

# Initialize Putter AI
puter = putter.Client(api_key=AI_ROUTER_API_KEY)

def ai_response(update: Update, context: CallbackContext):
    """Handles AI-based responses using Putter AI"""
    user_message = update.message.text

    try:
        # Sending request to Putter AI
        response = puter.ai.chat(user_message, testMode=False)

        # Sending response back to user
        update.message.reply_text(response)

    except Exception as e:
        update.message.reply_text(f"Error: {e}")