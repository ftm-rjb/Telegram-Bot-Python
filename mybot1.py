import telegram
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , PollAnswerHandler , CallbackQueryHandler , InlineQueryHandler , ConversationHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent و InlineKeyboardButton, InlineKeyboardMarkup , ReplyKeyboardMarkup, ReplyKeyboardRemove
import random
import urllib.request
import json
from googletrans import Translator
import logging

TOKEN = '1329017306:AAEdUNxL56_7y9orx7ci8ak5-pl4C-GbDmA'
#REQUEST_KWARGS={'proxy_url': 'https://2.188.17.71:8080/'}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

GENDER , AGE , CITY = range(3)

def start(update, context):
    reply_keyboard = [['zan' , 'mard']]

    update.message.reply_text(
        'سلام خوش آمدید' ,
        '/cancel را بزنید برای خارج شدن \n\n' ,
        'جنسیت خود را وارد کنید',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER

def gender(update, context):
    user = update.message.from_user
    logger.info(" %s جنسیت: %s", user.first_name, update.message.text)
    update.message.reply_text('اگر مایلید شهر خود را ارسال کنید' ,
                              reply_markup=ReplyKeyboardRemove())

    return CITY

def city(update , context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("لوکیشن %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    update.message.reply_text('لطفا سن خود را وارد کنید')

    return AGE

def skip_city(update, context):
    user = update.message.from_user
    logger.info("کاربر %s لوکیشن خود را نفرستاد", user.first_name)
    update.message.reply_text('لطفا سن خود را وارد کنید')

    return AGE

def age(update , context):
    user = update.message.from_user
    logger.info(" %s سن: %s", user.first_name, update.message.text)
    update.message.reply_text('باتشکر')

    return ConversationHandler.END

def cancel(update, context):
    user = update.message.from_user
    logger.info("کاربر %s کنسل کرد", user.first_name)
    update.message.reply_text('خدانگهدار',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def main():
    updater = Updater(token = TOKEN, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],

            CITY: [MessageHandler(Filters.location, city),
                       CommandHandler('skip', skip_city)],

            AGE: [MessageHandler(Filters.text & ~Filters.command, age)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

updater.start_polling()
updater.idle()

'''updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://floating-fortress-50176.herokuapp.com/' + TOKEN)'''
