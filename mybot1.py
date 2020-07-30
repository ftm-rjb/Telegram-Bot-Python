from telegram.ext import Updater , CommandHandler

updater = Updater(token = '1225980698:AAHqrM404mnvFhtezguH7oUW9xqAL2Egs_E' , 
                  request_kwargs = {'proxy_url': 'socks5://127.0.0.1:9050/'})

def register(bot , update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id , 'TYPING')
    bot.sendMessage(chat_id , 'hello')

start_command = CommandHandler('register' , register)
updater.dispatcher.add_handler(start_command)
updater.start_polling()
