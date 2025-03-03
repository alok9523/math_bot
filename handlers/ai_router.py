import requests
import json
import logging
from telegram import Update
from telegram.ext import CallbackContext
import config

logger = logging.getLogger(__name__)

async def ai_router_response(update: Update, context: CallbackContext):
    """Handles AI-based responses using OpenRouter API with advanced JSON structure."""
    user_message = " ".join(context.args) if context.args else ""

    if not user_message:
        await update.message.reply_text("Please provide a query. Example: /ai Explain quantum mechanics")
        return

    logger.info(f"Received AI request from {update.message.chat.username}: {user_message}")

    # OpenRouter API Endpoint
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {config.AI_ROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Advanced JSON Schema for Response Formatting
    data = json.dumps({
        "model": "openai/gpt-4o",
        "messages": [{"role": "user", "content": user_message}],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "ai_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "response_text": {
                            "type": "string",
                            "description": "AI-generated response"
                        },
                        "source": {
                            "type": "string",
                            "description": "Source of the information (if applicable)"
                        },
                        "confidence_score": {
                            "type": "number",
                            "description": "Confidence level of AI response"
                        }
                    },
                    "required": ["response_text"],
                    "additionalProperties": False
                }
            }
        }
    })

    try:
        response = requests.post(url, headers=headers, data=data)
        logger.info(f"OpenRouter Response: {response.status_code} - {response.text}")

        if response.status_code == 200:
            response_data = response.json()
            ai_content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")

            # Send formatted AI response
            await update.message.reply_text(f"🤖 AI Says:\n\n{ai_content}")

        else:
            await update.message.reply_text(f"⚠️ Error from OpenRouter: {response.text}")

    except Exception as e:
        logger.error(f"AI response error: {str(e)}")
        await update.message.reply_text("⚠️ AI service is currently unavailable. Please try again later.")