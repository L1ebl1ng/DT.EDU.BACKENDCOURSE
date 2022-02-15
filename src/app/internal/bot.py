import logging
import sys
import telegram
from telegram import Bot
from telegram.ext import CommandHandler, Updater
from app.internal.transport.bot.handlers import *
from config.settings import TOKEN

bot = Bot(TOKEN)
try:
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error(f"Invalid TOKEN.")
    sys.exit(1)


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('set_phone', set_phone))
    dp.add_handler(CommandHandler('me', me))
    return dp


def run_bot():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    setup_dispatcher(dp)

    bot_info = Bot(TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"'{bot_link}' начал неистовую работу")

    updater.start_polling()
    updater.idle()