from telegram.ext import Updater , CommandHandler
TOKEN = '1292823392:AAERdhM6yeCQaZPy4WdfkUBOn5vUyn7GEX4'

updater = Updater(TOKEN)

def start(bot , update ):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , 'your name is ')

start_command = CommandHandler('start' , start )
updater.dispatcher.add_handler(start_command)
updater.start_polling()
print('working')
