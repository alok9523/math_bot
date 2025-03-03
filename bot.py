import logging
import requests
from telegram import Update
from telegram.ext import CallbackContext
import config

logger = logging.getLogger(__name__)

async def ai_router_response(update: Update, context: CallbackContext):
    """Handles AI-based responses using OpenRouter API."""
    user_message = " ".join(context.args) if context.args else ""

    if not user_message:
        await update.message.reply_text("Please provide a query. Example: /ai Explain quantum mechanics")
        return

    logger.info(f"Received AI request from {update.message.chat.username}: {user_message}")

    # API Request to OpenRouter
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",  # Ensure correct model name
        "messages": [{"role": "user", "content": user_message}],
        "stream": False  # Make it True if handling streamed responses
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        logger.info(f"OpenRouter Response: {response.status_code} - {response.text}")

        if response.status_code == 200:
            ai_text = response.json()["choices"][0]["message"]["content"]
            await update.message.reply_text(ai_text)
        else:
            await update.message.reply_text(f"Error from OpenRouter: {response.text}")
    except Exception as e:
        logger.error(f"AI response error: {str(e)}")
        await update.message.reply_text("AI service is currently unavailable.")