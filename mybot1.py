import telegram
from telegram.ext import Updater , CommandHandler

tok = '1292823392:AAHyY7c9Scd3dw429rz6rPct1ohy5_cERRg'

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
