from telegram import Update
from telegram.ext import CallbackContext

class Post:
    def start(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        bot.send_message(chat_id=chat_id, text="Hello World!")
