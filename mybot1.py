from telegram.ext import Updater , CommandHandler , MessageHandler , Filters ,PollAnswerHandler
#import os
#PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1329017306:AAEdUNxL56_7y9orx7ci8ak5-pl4C-GbDmA'
#REQUEST_KWARGS={'proxy_url': 'https://2.188.17.71:8080/'}


def hi(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id , 'TYPING')
    bot.sendMessage(chat_id , 'hello' + args[0])
    bot.sendMessage(chat_id , 'your id is:' + args[1])

def main():
    updater = Updater(TOKEN)#request_kwargs=REQUEST_KWARGS)
    hi_command = CommandHandler('hi' , hi)
    one_massage = MessageHandler(Filters.all , hi)
    one_poll = PollAnswerHandler(hi)
    updater.dispatcher.add_handler(hi_command)
    updater.dispatcher.add_handler(one_massage)
    updater.dispatcher.add_handler(one_poll)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    updater.stop()
'''updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://floating-fortress-50176.herokuapp.com/' + TOKEN)'''
