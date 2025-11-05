import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Apna bot token
BOT_TOKEN = "8305054986:AAE6IomvLntAbNX-7Fiy9DO344HDiJamoEs"

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Start command handler - Welcome message
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
    
    # Custom keyboard
    keyboard = [
        ["/start", "/help"],
        ["/about", "Hello 👋"],
        ["Kaise ho?", "Mast hai! 😎"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

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
    **Purpose:** Tere saath baat karna aur help karna
    **Status:** Always Active! 🔥

    **Moto:** "Har message ka reply, har user ki help!" 💪
    """
    await update.message.reply_text(about_text)

# Har message ka reply dene wala function
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_name = update.message.from_user.first_name
    
    # Different responses based on message content
    responses = {
        "hello": f"Hello {user_name}! Kaise ho bhai? 😊",
        "hi": f"Hi {user_name}! Mast hai? 🚀",
        "kaise ho": f"Main toh mast hoon {user_name}! Tu bata? 😄",
        "how are you": f"I'm great {user_name}! Thanks for asking! 👍",
        "bye": f"Bye bye {user_name}! Phir milte hain 👋",
        "thank you": f"You're welcome {user_name}! 😊",
        "thanks": f"Koi baat nahi {user_name}! 😄",
        "mast hai": f"Waah {user_name}! Mazaa aa gaya! 🔥",
        "good": f"Shabaash {user_name}! 😎",
        "nice": f"Thanks {user_name}! 😊",
        "awesome": f"Wow {user_name}! You're awesome too! 🎉",
        "kya kar rahe ho": f"Tere saath baat kar raha hoon {user_name}! 😄",
        "what are you doing": f"Chatting with you {user_name}! 💬",
        "hii": f"Hii {user_name}! 😊",
        "hey": f"Hey {user_name}! What's up? 🚀",
        "hello 👋": f"Hello {user_name}! 👋",
        "mast hai! 😎": f"Bohot hard bhai! 🔥",
    }
    
    # Check if message matches any predefined response
    response = responses.get(user_message.lower())
    
    if response:
        await update.message.reply_text(response)
    else:
        # Random creative responses for other messages
        creative_responses = [
            f"Achha message hai '{user_message}'! 😄",
            f"{user_name}, tu bolta hai '{user_message}' - interesting! 🤔",
            f"Waah bhai! '{user_message}' likha hai! 🔥",
            f"Hmm... '{user_message}'... Nice thought {user_name}! 👍",
            f"{user_name}, main bhi yahi soch raha tha! Great minds think alike! 😎",
            f"Teri baat sahi hai '{user_message}'! 💯",
            f"Maza aa gaya padhke! '{user_message}' 👏",
            f"Bohot khoob {user_name}! '{user_message}' 😊",
            f"Main bhi agree karta hoon! '{user_message}' ✅",
            f"Perfect {user_name}! '{user_message}' 🎯"
        ]
        
        import random
        random_response = random.choice(creative_responses)
        await update.message.reply_text(random_response)

# Main function
def main():
    # Bot application create karo
    application = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    
    # Message handler for all text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Bot start karo
    print("🤖 Bot running...")
    print("📍 Telegram mein jaake apne bot ko message karo!")
    print("🚀 Har message ka reply milega!")
    application.run_polling()

if __name__ == "__main__":
    main()