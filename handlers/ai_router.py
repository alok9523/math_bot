import requests
import config
from telegram import Update
from telegram.ext import CallbackContext

async def ai_router_response(update: Update, context: CallbackContext):
    query = update.message.text
    if not query:
        await update.message.reply_text("Please provide some text.")
        return

    try:
        response = requests.post(
            "https://api.app-router.ai/generate",  # Replace with actual endpoint
            json={"input": query, "api_key": config.AI_ROUTER_API_KEY}
        )
        response_data = response.json()
        ai_reply = response_data.get("response", "No response received.")
        await update.message.reply_text(ai_reply)
    except Exception as e:
        await update.message.reply_text("AI service is currently unavailable.")