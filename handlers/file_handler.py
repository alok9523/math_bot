from telegram import Update
from telegram.ext import CallbackContext
import os

async def handle_document(update: Update, context: CallbackContext):
    document = update.message.document
    if not document:
        await update.message.reply_text("Please send a document.")
        return
    
    file = await context.bot.get_file(document.file_id)
    file_path = f"downloads/{document.file_name}"

    os.makedirs("downloads", exist_ok=True)
    file.download(file_path)

    await update.message.reply_text(f"File {document.file_name} saved successfully!")