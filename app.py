from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update
from main import Post


TOKEN = '5677023630:AAGdskZAvZwdRix213Ho28QaN-NZVcQtuU8'

app = Flask(__name__)

bot = Bot(TOKEN)
post = Post()

@app.route('/', methods=['POST'])
def index():
    dp = Dispatcher(bot, None, workers=0)

    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    dp.add_handler(CommandHandler('start', post.start))
    dp.add_handler(CommandHandler('id', post.get_id))
    dp.add_handler(MessageHandler(Filters.text('add admin'), post.add_admin))
    dp.add_handler(CallbackQueryHandler(post.add_group_check, pattern='addgroup'))
    dp.add_handler(CallbackQueryHandler(post.delet_group_check, pattern='deletegroup'))
    dp.add_handler(CallbackQueryHandler(post.add_message, pattern='Yes'))
    dp.add_handler(CallbackQueryHandler(post.delet_message, pattern='No'))
    dp.add_handler(MessageHandler(Filters.text('add channel'), post.add_group))
    dp.add_handler(MessageHandler(Filters.all, post.add_post))

    dp.process_update(update)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook()
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