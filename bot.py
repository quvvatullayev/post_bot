from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from main import Post

TOKEN = '5230794877:AAF7Y5UR88eR4hYSwVuSecoL6SYUFEdDICY'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

post = Post()

dispatcher.add_handler(CommandHandler('start', post.start))

updater.start_polling()
updater.idle()