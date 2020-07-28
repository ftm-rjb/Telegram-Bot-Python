from telegram.ext import Updater , CommandHandler

updater = Updater('1292823392:AAERdhM6yeCQaZPy4WdfkUBOn5vUyn7GEX4')

def start(bot , update ):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , 'your name is ')

start_command = CommandHandler('start' , start )
try:
    updater.dispatcher.add_handler(start_command)
except NetworkError():
    pass
updater.start_polling()
print('working')
