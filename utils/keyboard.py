from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = [
        [InlineKeyboardButton("AI Chat", callback_data="ai_chat")],
        [InlineKeyboardButton("Math Solver", callback_data="math_solver")],
        [InlineKeyboardButton("Wolfram Query", callback_data="wolfram_query")]
    ]
    return InlineKeyboardMarkup(keyboard)