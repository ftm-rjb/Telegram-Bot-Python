from telegram.ext import Updater , CommandHandler

updater = Updater(token = '1329017306:AAG6tozyUJqhZsUT9X-s-JE9JPCqQDnw4Wo')

def register(bot , update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id , 'TYPING')
    bot.sendMessage(chat_id , 'hello')

start_command = CommandHandler('hi' , register)
updater.dispatcher.add_handler(start_command)
updater.start_polling()
