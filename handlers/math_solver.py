import requests
import config
from telegram import Update
from telegram.ext import CallbackContext

async def solve_math(update: Update, context: CallbackContext):
    equation = " ".join(context.args)
    if not equation:
        await update.message.reply_text("Please provide a mathematical expression.")
        return

    try:
        response = requests.get(f"https://api.wolframalpha.com/v1/result?i={equation}&appid={config.WOLFRAM_API_KEY}")
        solution = response.text
        await update.message.reply_text(f"Solution: {solution}")
    except Exception as e:
        await update.message.reply_text("Error solving the equation.")