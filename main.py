from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from db import DB

db = DB('db.json')

class Post:
    def start(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        text  = "Hello, I'm a bot that can post messages to your channel.\n"
        text += "To get started, add me to your channel as an administrator and send me the channel name.\n"

        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                ['add channel']
            ],
            resize_keyboard=True     
            )

        bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
    
    def add_post_imge(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        all_channels = db.get_all_channels()

        for channel in all_channels:
            print(channel)
            bot.forward_message(
                chat_id=channel['name'], 
                from_chat_id=chat_id, 
                message_id=update.message.message_id
                )
    def get_text(self, update: Update, context: CallbackContext):
        bot = context.bot
        chat_id = update.message.chat_id
        text = 'Channel post for example:\n\n@channel_name'
        bot.sendMessage(chat_id, text)