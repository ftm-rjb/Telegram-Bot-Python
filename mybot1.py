import telegram
from telegram.ext import Updater , CommandHandler

tok = '1292823392:AAERdhM6yeCQaZPy4WdfkUBOn5vUyn7GEX4'

myupdater = Updater(token=tok)
mydispatcher = myupdater.dispatcher

def start(bot , update ):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , 'hellow')

start_command = CommandHandler('start' , start )
mydispatcher.add_handler(start_command)
myupdater.start_polling()
myupdater.idle()
