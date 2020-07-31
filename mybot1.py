from telegram.ext import Updater , CommandHandler
import os
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1329017306:AAG6tozyUJqhZsUT9X-s-JE9JPCqQDnw4Wo'
def register(bot , update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id , 'TYPING')
    bot.sendMessage(chat_id , 'hello')
    
def main():    
    updater = Updater(TOKEN , use_context=True)
    start_command = CommandHandler('hi' , register)
    updater.dispatcher.add_handler(start_command)
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://desolate-bayou-80201.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()