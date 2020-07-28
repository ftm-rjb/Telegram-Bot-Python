import telegram
from telegram.ext import Updater , CommandHandler

tok = '1292823392:AAERdhM6yeCQaZPy4WdfkUBOn5vUyn7GEX4'

def start(bot , update ):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , 'hellow')

mybot = telegram.Bot(token=tok)
dictinfo=mybot.get_me()

myupdater = Updater(token=tok, use_context=True)
mydispatcher = myupdater.dispatcher

start_command = CommandHandler('start' , start )
mydispatcher.add_handler(start_command)
updater.start_polling()
