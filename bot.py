import logging  
from telegram import Update  
from telegram.ext import Application, CommandHandler, MessageHandler, filters  
import config  

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Command: /start
async def start(update: Update, context):
    user = update.effective_user
    await update.message.reply_text(f"Hello {user.first_name}! Welcome to Advanced Telegram Bot.")

# Message Handler: Echo (Temporary)
async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

def main():
    """Main function to start the bot"""
    application = Application.builder().token(config.BOT_TOKEN).build()

    # Register Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start Bot
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()