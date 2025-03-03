import logging
import requests
import json
from telegram import Update
from telegram.ext import CallbackContext
import config

# Configure logging
logger = logging.getLogger(__name__)

async def ai_router_response(update: Update, context: CallbackContext):
    """Handles AI-based responses using OpenRouter API."""
    user_message = " ".join(context.args) if context.args else ""

    if not user_message:
        await update.message.reply_text("Please provide a query. Example: /ai What is quantum mechanics?")
        return

    logger.info(f"Received AI request from {update.message.chat.username}: {user_message}")

    # OpenRouter API request
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {config.AI_ROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourwebsite.com",  # Replace with your actual site URL if needed
        "X-Title": "YourBotName"  # Replace with your bot name if needed
    }
    data = {
        "model": "openai/gpt-4o",  # Change the model if needed
        "messages": [{"role": "user", "content": user_message}],
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        logger.info(f"OpenRouter Response: {response.status_code} - {response.text}")

        if response.status_code == 200:
            ai_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
            await update.message.reply_text(ai_text)
        else:
            await update.message.reply_text(f"Error from OpenRouter: {response.text}")
    except Exception as e:
        logger.error(f"AI response error: {str(e)}")
        await update.message.reply_text("AI service is currently unavailable.")