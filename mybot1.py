from telegram.ext import Updater , CommandHandler

updater = Updater('1292823392:AAGV58CHQ9OxyR8YCCva7Ojmv1QqnZRHCNI')

def start(bot , update , args):
    bot.sendChatAction(update.message.chat_id , 'TYPING');

    bot.sendMessage(update.message.chat_id , 'your name is :' + args[0])

start_command = CommandHandler('start' , start , pass_args = True)

updater.dispatcher.add_handler(start_command)

updater.start_polling()
updater.idle()
