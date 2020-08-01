from telegram.ext import Updater , CommandHandler , MessageHandler , Filters ,PollAnswerHandler
#import os
#PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1329017306:AAEdUNxL56_7y9orx7ci8ak5-pl4C-GbDmA'
#REQUEST_KWARGS={'proxy_url': 'https://2.188.17.71:8080/'}


def start(bot , update , args):
    chat_id = update.message.chat_id
    first = update.message.chat.first_name
    last = update.message.chat.last_name
    bot.sendChatAction(chat_id , 'TYPING')
    bot.sendMessage(chat_id , 'hello {first} {last}'.format(first = first , last = last))

def contacts(bot , update ):
    chat_id = update.message.chat_id
    bot.sendContacts(chat_id , phone_number=09125384132, first_name='mom', last_name='mah')

def main():
    updater = Updater(TOKEN)#request_kwargs=REQUEST_KWARGS)
    start_command = CommandHandler('start' , start , pass_args = True)
    contacts_command = CommandHandler('contacts' , contacts)
    #one_massage = MessageHandler(Filters.all , hi)
    #one_poll = PollAnswerHandler(hi)
    updater.dispatcher.add_handler(start_command)
    updater.dispatcher.add_handler(contacts_command)
    #updater.dispatcher.add_handler(one_massage)
    #updater.dispatcher.add_handler(one_poll)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
'''updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://floating-fortress-50176.herokuapp.com/' + TOKEN)'''
