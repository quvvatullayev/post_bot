from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update
from main import Post


TOKEN = '5961163643:AAFgyilG0if7Ud0xwHJG-r-PZbohqOZKrDE'

app = Flask(__name__)

bot = Bot(TOKEN)
post = Post()

@app.route('/', methods=['POST'])
def index():
    dispatcher = Dispatcher(bot, None, workers=0)

    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    dispatcher.add_handler(CommandHandler('start', post.start))
    dispatcher.add_handler(CommandHandler('id', post.get_id))
    dispatcher.add_handler(MessageHandler(Filters.text('add admin'), post.add_admin))
    dispatcher.add_handler(MessageHandler(Filters.text('admin list'), post.admin_list))
    dispatcher.add_handler(MessageHandler(Filters.text('channel list'), post.channel_list))
    dispatcher.add_handler(MessageHandler(Filters.text('delete channel'), post.delete_channel))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex('^delete_group'), post.delete_channel))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex('^delete'), post.delete_admin))
    dispatcher.add_handler(CallbackQueryHandler(post.add_group_check, pattern='addgroup'))
    dispatcher.add_handler(CallbackQueryHandler(post.delet_group_check, pattern='deletegroup'))
    dispatcher.add_handler(CallbackQueryHandler(post.add_message, pattern='Yes'))
    dispatcher.add_handler(CallbackQueryHandler(post.delet_message, pattern='No'))
    dispatcher.add_handler(MessageHandler(Filters.text('add channel'), post.add_group))
    dispatcher.add_handler(MessageHandler(Filters.all, post.add_post))
    dispatcher.process_update(update)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook('https://createpostbot.pythonanywhere.com')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
    

@app.route('/deletewebhook', methods=['GET', 'POST'])
def delete_webhook():
    s = bot.delete_webhook()
    if s:
        return "webhook delete ok"
    else:
        return "webhook delete failed"