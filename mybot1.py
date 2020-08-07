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

CHECK_THIS_OUT = 'check-this-out'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'

def start(update, context):
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, CHECK_THIS_OUT, group=True)
    text = "Feel free to tell your friends about it:\n\n" + url
    update.message.reply_text(text)

def deep_linked_level_1(update, context):
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    text = "Awesome, you just accessed hidden functionality! " \
           " Now let's get back to the private chat."
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Continue here!', url=url)
    )
    update.message.reply_text(text, reply_markup=keyboard)


def deep_linked_level_2(update, context):
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, USING_ENTITIES)
    text = "You can also mask the deep-linked URLs as links: " \
           "[▶️ CLICK HERE]({}).".format(url)
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


def deep_linked_level_3(update, context):
    payload = context.args
    update.message.reply_text("Congratulations! This is as deep as it gets 👏🏻\n\n"
                              "The payload was: {}".format(payload))

def main():

    # Create the Updater and pass it your bot's token.
    updater = Updater(token = TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # More info on what deep linking actually is (read this first if it's unclear to you):
    # https://core.telegram.org/bots#deep-linking

    # Register a deep-linking handler
    dp.add_handler(CommandHandler("start", deep_linked_level_1, Filters.regex(CHECK_THIS_OUT)))

    # This one works with a textual link instead of an URL
    dp.add_handler(CommandHandler("start", deep_linked_level_2, Filters.regex(SO_COOL)))

    # We can also pass on the deep-linking payload
    dp.add_handler(CommandHandler("start",
                                  deep_linked_level_3,
                                  Filters.regex(USING_ENTITIES),
                                  pass_args=True))

    # Make sure the deep-linking handlers occur *before* the normal /start handler.
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

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

if __name__ == '__main__':
    main()

'''updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://floating-fortress-50176.herokuapp.com/' + TOKEN)'''
