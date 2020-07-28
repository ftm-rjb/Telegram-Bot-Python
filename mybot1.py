from telegram.ext import Updater , CommandHandler
TOKEN = '1292823392:AAHyY7c9Scd3dw429rz6rPct1ohy5_cERRg'

updater = Updater(TOKEN)

def start(bot , update ):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , 'your name is ')

start_command = CommandHandler('start' , start )
updater.dispatcher.add_handler(start_command)
updater.start_polling()
print('working')
