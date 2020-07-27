from telegram.ext import Updater , CommandHandler

updater = Updater('1292823392:AAGV58CHQ9OxyR8YCCva7Ojmv1QqnZRHCNI')

def start(bot , update ):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id , 'your name is ')

start_command = CommandHandler('start' , start )

updater.dispatcher.add_handler(start_command)

updater.start_polling()
