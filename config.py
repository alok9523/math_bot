import os  

# Bot Token (Replace with your actual bot token)
BOT_TOKEN = os.getenv("BOT_TOKEN", "your-telegram-bot-token")

# API Keys (Replace with actual keys)
WOLFRAM_API_KEY = os.getenv("WOLFRAM_API_KEY", "3GJAG3-3RA3EGRUQ7")
AI_ROUTER_API_KEY = os.getenv("AI_ROUTER_API_KEY", "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"")

# Database File Paths
USER_DB_PATH = "database/users.db"
LOG_DB_PATH = "database/logs.db"

# Logging Configuration
LOG_FILE = "logs/bot.log"
LOG_LEVEL = "INFO"

# Other Settings
ADMINS = [6195379665]  # Replace with Telegram user IDs of admins