import sqlite3
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database File Paths
USER_DB_PATH = "database/users.db"
LOG_DB_PATH = "database/logs.db"

def create_tables():
    """Create necessary database tables if they don't exist."""
    try:
        with sqlite3.connect(USER_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE,
                    first_name TEXT,
                    last_name TEXT,
                    username TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

        with sqlite3.connect(LOG_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    command TEXT,
                    response TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

        logger.info("Database tables created successfully.")
    
    except Exception as e:
        logger.error(f"Error creating tables: {e}")

def add_user(user_id, first_name, last_name, username):
    """Add a new user to the database."""
    try:
        with sqlite3.connect(USER_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (user_id, first_name, last_name, username) 
                VALUES (?, ?, ?, ?) 
                ON CONFLICT(user_id) DO NOTHING
            """, (user_id, first_name, last_name, username))
            conn.commit()
            logger.info(f"User {user_id} registered successfully.")
    except Exception as e:
        logger.error(f"Error adding user: {e}")

def log_command(user_id, command, response):
    """Log a user's command and bot response."""
    try:
        with sqlite3.connect(LOG_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO logs (user_id, command, response) 
                VALUES (?, ?, ?)
            """, (user_id, command, response))
            conn.commit()
            logger.info(f"Logged command: {command} from User {user_id}.")
    except Exception as e:
        logger.error(f"Error logging command: {e}")

def get_user_count():
    """Returns the total number of registered users."""
    try:
        with sqlite3.connect(USER_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            return count
    except Exception as e:
        logger.error(f"Error retrieving user count: {e}")
        return 0

# Ensure tables exist
create_tables()