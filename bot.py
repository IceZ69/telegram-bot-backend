# bot.py
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging to see errors and information
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get your secret bot token from a system "environment variable"
# This is much safer than writing your token directly in the code.
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    # If the token isn't found, the bot can't start.
    raise ValueError("No BOT_TOKEN found in environment variables")

# This function defines what happens when a user sends the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when the command /start is issued."""
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Hello, {user_name}! I am your bot, running on a server!")

def main() -> None:
    """This is the main function that starts and runs the bot."""
    # Create the main Application object
    application = Application.builder().token(BOT_TOKEN).build()

    # Tell the bot to listen for the "/start" command and run the "start" function when it sees it.
    application.add_handler(CommandHandler("start", start))

    # Start the bot and keep it running until you manually stop it.
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()