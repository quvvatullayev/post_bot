from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from db import DB

db = DB('db.json')

class Post:
    def start(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        text  = "Hello, I'm a bot that can post messages to your channel✋.\n"
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

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Yes🆗', callback_data=f'Yes_{update.message.message_id}'), 
                    InlineKeyboardButton(text='No⛔️', callback_data='No')
                ]
            ]
            )

        bot.sendMessage(chat_id, 'Shall I send a message❓', reply_markup=keyboard)
        
    def add_message(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        message_id = query.data.split('_')[1]

        all_channels = db.get_all_channels()

        for channel in all_channels:
            print(channel)
            bot.forward_message(
                chat_id=channel['name'], 
                from_chat_id=chat_id, 
                message_id=message_id,
                disable_notification = True
                )
        text = "The message was sent successfully✅"
        query.edit_message_text(text, reply_markup=None)

    def delet_message(self, update: Update, context: CallbackContext):
        query = update.callback_query

        text = "The message was rejected🚫"
        query.edit_message_text(text, reply_markup=None)

    def get_text(self, update: Update, context: CallbackContext):
        bot = context.bot
        chat_id = update.message.chat_id
        text = 'Channel post for example:\n\n@channel_name'
        db.add_channel_add(chat_id, 'add_channel')
        bot.sendMessage(chat_id, text)