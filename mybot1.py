from telegram.ext import Updater , CommandHandler
import os
import logging
PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = 'OnlineContactsBot'


updater = Updater('1292823392:AAGV58CHQ9OxyR8YCCva7Ojmv1QqnZRHCNI')

def start(bot , update , args):
    bot.sendChatAction(update.message.chat_id , 'TYPING');

    bot.sendMessage(update.message.chat_id , 'your name is :' + args[0])

start_command = CommandHandler('start' , start , pass_args = True)

updater.dispatcher.add_handler(start_command)

updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://dry-caverns-33147.herokuapp.com/' + TOKEN)
