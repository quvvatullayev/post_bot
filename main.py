from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from db import DB, Admin, Users

db = DB('db.json')
admin = Admin('admin.json')
user = Users('user.json')

class Post:
    def start(self, update: Update, context: CallbackContext) -> None:
        if update.message.chat.id > 0:
            username = update.message.from_user.username
            get_admin = admin.get_admin(username)

            if get_admin or username == 'ogabekquvvatullayev':
                bot = context.bot
                chat_id = update.effective_chat.id

                text  = "Hello, I'm a bot that can post messages to your channel✋.\n"
                text += "To get started, add me to your channel as an administrator and send me the channel name.\n"

                reply_markup = ReplyKeyboardMarkup(
                    keyboard=[
                        ['add channel'],
                        ['add admin'],
                    ],
                    resize_keyboard=True     
                    )

                bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
            else:
                bot = context.bot
                chat_id = update.effective_chat.id
                username = update.message.from_user.username
                first_name = update.message.from_user.first_name
                get_user = user.get_user(chat_id=chat_id)
                
                if get_user is None:
                    add_user = user.add_user(username=username, id=chat_id, first_name=first_name)
                    text = "Hello, I'm a bot that can post messages to your channel✋.\n"
                    bot.send_message(chat_id=chat_id, text=text)
                else:
                    text = "Hello, I'm a bot that can post messages to your channel✋.\n"
                    bot.send_message(chat_id=chat_id, text=text)

                
    def add_post(self, update: Update, context: CallbackContext) -> None:
        if update.message.chat.id > 0:
            bot = context.bot
            chat_id = update.effective_chat.id

            get_summation_group = db.get_summation_group(chat_id)
            get_admin = admin.get_admin(id=1)

            if get_admin:
                text = update.message.text
                get_user = user.get_user_by_username(text)

                if not get_user:
                    text = "The user was not found❌"
                    bot.send_message(chat_id, text)

                else:
                    print(get_user)
                    get_user = get_user[0]
                    first_name = get_user['first_name']
                    username = get_user['username']
                    user_id = get_user['chat_id']

                    add_admin = admin.add_admin(username=username, id=user_id, first_name=first_name)
                    delete_user = user.delete_user(chat_id=user_id)
                    delete_admin = admin.delete_admin()

                    text = "The user has been assigned to the administrator position✅"
                    bot.send_message(chat_id, text)


            elif get_summation_group is None:
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
        if update.message.chat.id > 0:
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

        all_channels = db.get_all_groups()

        for channel in all_channels:
            bot.copy_message(
                chat_id=channel['group_id'], 
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
    
    def get_id(self, update: Update, context: CallbackContext):
        if update.message.chat.id < 0:
            chat_id = update.message.chat.id
            bot = context.bot
            if chat_id < 0:
                text = f"Copied message: {chat_id}"
                bot.send_message(chat_id, text)

    def add_admin(self, update: Update, context: CallbackContext):
        bot = context.bot
        chat_id = update.effective_chat.id
        add_admin = admin.add_admin()
        text = "Send the username of the person you want to admin👨‍💻\n\n"
        text += "For example: ogabekquvvatullayev"
        bot.send_message(chat_id=chat_id, text=text)