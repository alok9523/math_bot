from telegram import Update
from telegram.ext import CallbackContext
import sqlite3
import logging  

logger = logging.getLogger(__name__)

def add_user(user_id, username):
    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()

async def check_user(update: Update, context: CallbackContext):
    user = update.effective_user
    add_user(user.id, user.username)
    await update.message.reply_text(f"User {user.first_name} registered successfully.")
    logger.info(f"User {user.id} ({user.username}) registered.")