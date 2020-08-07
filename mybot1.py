import telegram
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , PollAnswerHandler , CallbackQueryHandler , InlineQueryHandler , ConversationHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent , InlineKeyboardButton, InlineKeyboardMarkup , ReplyKeyboardMarkup, ReplyKeyboardRemove , ParseMode
import logging
from telegram.utils import helpers

TOKEN = '1329017306:AAEdUNxL56_7y9orx7ci8ak5-pl4C-GbDmA'
#REQUEST_KWARGS={'proxy_url': 'https://2.188.17.71:8080/'}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

L = []

ONE , TWO , THREE , FOUR = range(4)

def start(update, context):
    reply_keyboard = [['چت با دوستان' , 'دریافت ارسالها']]
    update.message.reply_text(
        'سلام خوش آمدید',
        'یکی از دو گزینه را انتخاب کنید',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    if update.message.text == 'چت با دوستان':
        return ONE
    if update.message.text == 'دریافت ارسالها':
        return TWO

    #url = helpers.create_deep_linked_url(bot.get_me().username)

def one(update , context):
    update.message.reply_text('لطفا آی دی موردنظر را بفرستید' ,
                              reply_markup=ReplyKeyboardRemove())
    return THREE

def three(update , context):
    id = update.message.text
    update.message.reply_text('لطفا بیام خود را بنویسید' ,
                              reply_markup=ReplyKeyboardRemove())
    return FOUR

def four(update , context):
    pm = update.message.text
    L.append(pm)
    context.bot.sendMessage(int(id) , pm)
    update.message.reply_text('خدانگهدار',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def two(update , context):
    context.bot.sendMessage(int(id) , L)
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text('خدانگهدار',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():

    # Create the Updater and pass it your bot's token.
    updater = Updater(token = TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            ONE: [MessageHandler(Filters.regex('^(چت با دوستان|دریافت ارسالها)$'), one)],

            TWO: [MessageHandler(Filters.regex('^(چت با دوستان|دریافت ارسالها)$'), two)],

            THREE: [MessageHandler(Filters.text & ~Filters.command, three)],

            FOUR: [MessageHandler(Filters.text & ~Filters.command, four)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()


'''
def start(update, context):
    reply_keyboard = [['زن' , 'مرد']]
    update.message.reply_text(
        'سلام خوش آمدید',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER

def gender(update, context):
    user = update.message.from_user
    logger.info(" %s جنسیت: %s", user.first_name, update.message.text)
    update.message.reply_text('اگر مایلید شهر خود را ارسال کنید' ,
                              reply_markup=ReplyKeyboardRemove())
    L.append("%s جنسیت: %s", %(user.first_name, update.message.text))

    return CITY

def city(update , context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("لوکیشن %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    update.message.reply_text('لطفا سن خود را وارد کنید')

    return AGE

def skip_city(update, context):
    user = update.message.from_user
    logger.info('%s شهر را نفرستاد', user.first_name)
    update.message.reply_text('لطفا سن خود را وارد کنید')

    return AGE

def age(update , context):
    user = update.message.from_user
    logger.info("سن %s: %s", user.first_name, update.message.text)
    update.message.reply_text('متشکرم')

    return ConversationHandler.END

def cancel(update, context):
    user = update.message.from_user
    logger.info("%s کنسل کرد ", user.first_name)
    update.message.reply_text('خدانگهدار',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(token = TOKEN, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [MessageHandler(Filters.regex('^(زن|مرد)$'), gender)],

            CITY: [MessageHandler(Filters.location, city),
                       CommandHandler('skip', skip_city)],

            AGE: [MessageHandler(Filters.text & ~Filters.command, age)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()
'''

'''updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://floating-fortress-50176.herokuapp.com/' + TOKEN)'''
