import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Bot token environment variable se lega
BOT_TOKEN = os.environ.get('8305054986:AAE6IomvLntAbNX-7Fiy9DO344HDiJamoEs')

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    welcome_text = f"""
🎉 **Welcome {user_name}!** 🎉

**Namaste Bhai! 🙏**

Main tera personal bot hoon! 
Tujhe har cheez mein help karunga.

🔥 **Meri Special Features:**
• Har message ka reply dunga
• Tere saath baat karunga
• Help karunga

**Bas tu message type karta ja, main reply karta rahunga!** 😄
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📖 **Help Section**

**Commands:**
/start - Welcome message
/help - Yeh help menu
/about - Bot ke bare mein

**Kuch bhi type karo** - Main reply karunga! 💬
    """
    await update.message.reply_text(help_text)

# About command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
🤖 **About This Bot**

**Creator:** Tera Bhai 👦
**Language:** Python 🐍
**Purpose:** Tere saath baat karna
**Status:** 24/7 Active! 🔥
    """
    await update.message.reply_text(about_text)

# Har message ka reply
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_name = update.message.from_user.first_name
    
    responses = {
        "hello": f"Hello {user_name}! Kaise ho bhai? 😊",
        "hi": f"Hi {user_name}! Mast hai? 🚀", 
        "kaise ho": f"Main toh mast hoon {user_name}! Tu bata? 😄",
        "how are you": f"I'm great {user_name}! Thanks for asking! 👍",
        "bye": f"Bye bye {user_name}! Phir milte hain 👋",
        "thank you": f"You're welcome {user_name}! 😊",
    }
    
    response = responses.get(user_message.lower())
    if response:
        await update.message.reply_text(response)
    else:
        creative_responses = [
            f"Achha message hai '{user_message}'! 😄",
            f"{user_name}, interesting thought! 🤔",
            f"Waah bhai! '{user_message}' 🔥",
            f"Hmm... '{user_message}'... Nice! 👍",
        ]
        import random
        await update.message.reply_text(random.choice(creative_responses))

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot running on GitHub...")
    application.run_polling()

if __name__ == "__main__":
    main()