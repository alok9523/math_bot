import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from handlers.start import start_command
from handlers.chat import chat_handler
from handlers.wolfram import wolfram_handler
from handlers.ai_router import ai_router_handler
from handlers.math_solver import math_solver_handler
from config import TELEGRAM_BOT_TOKEN

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Function to handle errors
async def error_handler(update: object, context: CallbackContext) -> None:
    logger.error(f"Exception while handling update: {context.error}")

# Main function to run the bot
def main():
    # Initialize bot application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command Handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("wolfram", wolfram_handler))
    application.add_handler(CommandHandler("ai", ai_router_handler))
    application.add_handler(CommandHandler("math", math_solver_handler))

    # Chat Handler (Handles AI chat responses)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_handler))

    # Error Handler
    application.add_error_handler(error_handler)

    # Start polling
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()