import logging  
from telegram import Update  
from telegram.ext import Application, CommandHandler, MessageHandler, filters  
import config  

# Import Handlers
from handlers.start import start  
from handlers.admin import ban_user  
from handlers.user_management import check_user  
from handlers.wolfram import wolfram_query  
from handlers.ai_router import ai_router_response  
from handlers.math_solver import solve_math  
from handlers.chat import chat  
from handlers.image_processing import process_image  
from handlers.file_handler import handle_document  

# Configure Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

def main():
    """Main function to start the bot"""
    application = Application.builder().token(config.BOT_TOKEN).build()

    # Register Command Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("register", check_user))
    application.add_handler(CommandHandler("ban", ban_user))
    application.add_handler(CommandHandler("wolfram", wolfram_query))
    application.add_handler(CommandHandler("ai", ai_router_response))
    application.add_handler(CommandHandler("solve", solve_math))

    # Register Message Handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    application.add_handler(MessageHandler(filters.PHOTO, process_image))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Start Bot
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()