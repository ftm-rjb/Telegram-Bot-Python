from telegram.ext import Updater , CommandHandler , MessageHandler , Filters
from telegram.ext import PollAnswerHandler , CallbackQueryHandler , InlineQueryHandler
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import matplotlib.pyplot as plt
import random
import urllib.request
import json
import geocoder
from googletrans import Translator

#import os
#PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1329017306:AAEdUNxL56_7y9orx7ci8ak5-pl4C-GbDmA'
#REQUEST_KWARGS={'proxy_url': 'https://2.188.17.71:8080/'}


def start(bot , update , args):
    chat_id = update.effective.chat_id
    first = update.message.chat.first_name
    bot.sendChatAction(chat_id , 'TYPING')
    bot.sendMessage(chat_id , 'hello {first}'.format(first = first))

def tools(update, context):
    mykeyboard = [[InlineKeyboardButton("نمودار دایره ای", callback_data='gc')],
                  [InlineKeyboardButton("ترجمه به فارسی", callback_data='t2f')],
                  [InlineKeyboardButton("بارکد", callback_data='bc'),InlineKeyboardButton("لینک بر", callback_data='sl')]]
    reply_markup = InlineKeyboardMarkup(mykeyboard)
    update.message.reply_text('ابزار مورد نظر خود را انتخاب کنید 🛠', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data =='gc':
        #درخواست از کاربر برای ورود داده
        context.bot.send_message(chat_id=update.effective_chat.id, text="لیست اعداد را مانند مثال برای دریافت نمودار دایره ای وارد کنید [1,2,3]")

    elif query.data=='t2f':
        context.bot.send_message(chat_id=update.effective_chat.id, text="متن خود را برای ترجمه به فارسی وارد بکنید ")

def nemoodar(update,context):

    matn=update.message.text
    translator=Translator(service_urls=['translate.google.com'])
    tarjom=translator.translate(matn,dest='fa')
    context.bot.send_message(chat_id=update.effective_chat.id,text=tarjom.text)

mybot = telegram.Bot(token=tok)
dictinfo=mybot.get_me()
updater = Updater(TOKEN)#request_kwargs=REQUEST_KWARGS)
start_command = CommandHandler('start' , start , pass_args = True)
tools_command = CommandHandler('tools',tools)
nemoodar_command = CommandHandler('nemoodar',nemoodar)
#one_massage = MessageHandler(Filters.all , hi)
#one_poll = PollAnswerHandler(hi)
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(tools_command)
updater.dispatcher.add_handler(nemoodar_command)
#updater.dispatcher.add_handler(one_massage)
#updater.dispatcher.add_handler(one_poll)
updater.start_polling()
updater.idle()

'''updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://floating-fortress-50176.herokuapp.com/' + TOKEN)'''
