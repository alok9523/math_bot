import wolframalpha
import config
from telegram import Update
from telegram.ext import CallbackContext

# Initialize Wolfram Client
client = wolframalpha.Client(config.WOLFRAM_API_KEY)

async def wolfram_query(update: Update, context: CallbackContext):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Please provide a query after /wolfram.")
        return
    
    try:
        res = client.query(query)
        answer = next(res.results).text
        await update.message.reply_text(f"Answer: {answer}")
    except Exception as e:
        await update.message.reply_text("Sorry, I couldn't process that query.")