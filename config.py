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