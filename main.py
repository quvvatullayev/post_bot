from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup,User
from telegram.ext import CallbackContext
from pprint import pprint
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
    
    def add_post(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        get_summation_group = db.get_summation_group(chat_id)

        if get_summation_group is None:
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text='Yes🆗', callback_data=f'Yes_{update.message.message_id}'),
                        InlineKeyboardButton(text='No⛔️', callback_data='No')
                    ]
                ]
                )
            
            bot.sendMessage(chat_id, "will you send the message to this channel?", reply_markup=keyboard)

        else:
            text = update.message.text
            db.updeate_summation_group(text, chat_id)
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text='Yes🆗', callback_data=f'addgroup'), 
                        InlineKeyboardButton(text='No⛔️', callback_data='deletegroup')
                    ]
                ]
                )

            bot.sendMessage(chat_id, f'{text} keep this id?', reply_markup=keyboard)

    def add_group(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        chat_id = update.effective_chat.id
        get_summation_group = db.get_summation_group(chat_id)

        if get_summation_group:
            db.delete_summation_group(chat_id)
            db.add_summation_group(chat_id, update.message.text)
        else:
            db.add_summation_group(chat_id, update.message.text)

        text = "Please send the channel name📢\n\n"        
        text += "Post a message to the group id📝\n\n"
        text += "For example: -1001974646897\n\n"

        bot.send_message(chat_id=chat_id, text=text)
    
    def add_message(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        message_id = query.data.split('_')[1]
        print(message_id)

        all_channels = ['-1001974646897', '-1001974646897']

        for channel in all_channels:
            bot.copy_message(
                chat_id=channel, 
                from_chat_id=chat_id, 
                message_id=message_id
                )
            
        text = "The message was sent successfully✅"
        query.edit_message_text(text, reply_markup=None)

    def delet_message(self, update: Update, context: CallbackContext):
        query = update.callback_query

        text = "The message was rejected🚫"
        query.edit_message_text(text, reply_markup=None)

    def add_group_check(self, update: Update, context: CallbackContext):
        query = update.callback_query
        chat_id = query.message.chat_id

        get_summation_group = db.get_summation_group(chat_id)
        print(get_summation_group, '---------------------------------')
        
        db.add_group(get_summation_group['group_id'])
        db.delete_summation_group(chat_id)

        text = "The message was sent successfully✅"
        query.edit_message_text(text, reply_markup=None)

    def delet_group_check(self, update: Update, context: CallbackContext):
        query = update.callback_query
        chat_id = query.message.chat_id

        db.delete_summation_group(chat_id)

        text = "The message was rejected🚫"
        query.edit_message_text(text, reply_markup=None)