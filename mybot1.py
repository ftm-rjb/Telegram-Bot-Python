from telegram.ext import Updater , CommandHandler

updater = Updater('1292823392:AAERdhM6yeCQaZPy4WdfkUBOn5vUyn7GEX4')

def start(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id , 'TYPING');
    bot.sendMessage(chat_id , 'your name is: ' + args[0])

start_command = CommandHandler('start' , start , pass_args = True)
updater.dispatcher.add_handler(start_command)
updater.start_polling()
