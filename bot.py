from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from main import Post

TOKEN = '5677023630:AAGdskZAvZwdRix213Ho28QaN-NZVcQtuU8'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

post = Post()

dispatcher.add_handler(CommandHandler('start', post.start))
dispatcher.add_handler(MessageHandler(Filters.text('add channel'), post.get_text))
dispatcher.add_handler(MessageHandler(Filters.all, post.add_post_imge))

updater.start_polling()
updater.idle()