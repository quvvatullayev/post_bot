from telegram import Update
from telegram.ext import CallbackContext
from db import DB

db = DB('db.json')

class Post:
    def start(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        text  = "Hello, I'm a bot that can post messages to your channel.\n"
        text += "To get started, add me to your channel as an administrator and send me the channel name.\n"

        bot.send_message(chat_id=chat_id, text=text)
    
    def add_post_imge(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        text  = "Send me the image you want to post to your channel.\n"
        text += "To cancel, send /cancel.\n"
        all_channels = db.get_all_channels()

        for channel in all_channels:
            print(channel)
            bot.send_message(chat_id=channel['name'], text="Hello, I'm a bot that can post messages to your channel.\n")

        # image = update.message.photo[-1].get_file().file_path

        # bot.send_message(chat_id=chat_id, text=text)