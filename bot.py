from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update
from main import Post

TOKEN = '5677023630:AAGdskZAvZwdRix213Ho28QaN-NZVcQtuU8'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

post = Post()

dispatcher.add_handler(CommandHandler('start', post.start))
dispatcher.add_handler(CommandHandler('id', post.get_id))
dispatcher.add_handler(MessageHandler(Filters.text('add admin'), post.add_admin))
dispatcher.add_handler(MessageHandler(Filters.text('admin list'), post.admin_list))
dispatcher.add_handler(MessageHandler(Filters.text('channel list'), post.channel_list))
dispatcher.add_handler(MessageHandler(Filters.text('delete channel'), post.delete_channel))
dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex('^delete_group'), post.delete_channel))
# dispatcher.add_handler(MessageHandler(Filters.text('delete admin'), post.delete_admin))
dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex('^delete'), post.delete_admin))
dispatcher.add_handler(CallbackQueryHandler(post.add_group_check, pattern='addgroup'))
dispatcher.add_handler(CallbackQueryHandler(post.delet_group_check, pattern='deletegroup'))
dispatcher.add_handler(CallbackQueryHandler(post.add_message, pattern='Yes'))
dispatcher.add_handler(CallbackQueryHandler(post.delet_message, pattern='No'))
dispatcher.add_handler(MessageHandler(Filters.text('add channel'), post.add_group))
dispatcher.add_handler(MessageHandler(Filters.all, post.add_post))

updater.start_polling()
updater.idle()