import json
from telegram import Update
from telegram.ext import CallbackContext
from app.internal.services.user_service import *


def start(update: Update, context: CallbackContext) -> None:
    create_user(username=update.effective_user.username)
    update.message.reply_text(f'Ну здарова')


def set_phone(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        update.message.reply_text('Не правильно, широкую на широкую нада')
        return
    set_user_phone(username=update.effective_user.username, phone=context.args[0])
    update.message.reply_text('Скам машина АКТИВИРОВАНА')


def me(update: Update, context: CallbackContext) -> None:
    person = get_data(update.effective_user.username)
    if person:
        update.message.reply_text(json.dumps(person, indent=2, ensure_ascii=False))