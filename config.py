import os  

# Bot Token (Replace with your actual bot token)
BOT_TOKEN = os.getenv("BOT_TOKEN", "7889602638:AAFtqbV5K_4uCEJcCL4DmdnkdJ0QCzVjrtg")

# API Keys (Replace with actual keys)
WOLFRAM_API_KEY = os.getenv("WOLFRAM_API_KEY", "3GJAG3-3RA3EGRUQ7")

AI_ROUTER_API_KEY = os.getenv("AI_ROUTER_API_KEY", "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")

# Database File Paths
USER_DB_PATH = "database/users.db"
LOG_DB_PATH = "database/logs.db"

# Logging Configuration
LOG_FILE = "logs/bot.log"
LOG_LEVEL = "INFO"

# Other Settings
ADMINS = [6195379665]  # Replace with Telegram user IDs of admins