import html
import json
import os
from typing import Optional

from spambot import (
    DEV_USERS,
    OWNER_ID,
    SUDO_USERS,
    dispatcher,
)
from spambot.modules.helper_funcs.chat_status import (
    dev_plus,
    sudo_plus,
)
from spambot.modules.helper_funcs.extraction import extract_user
from telegram import ParseMode, TelegramError, Update
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html



def check_user_id(user_id: int, context: CallbackContext) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "That's not a user stupid!!"

    elif user_id == bot.id:
        reply = "Bots cant control me!!"

    else:
        reply = None
    return reply

@run_async
@dev_plus
def addsudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    if user_id in SUDO_USERS:
        message.reply_text("This member is already a Sudo user!!")
        return ""
    SUDO_USERS.append(user_id)

    update.effective_message.reply_text(
        rt
        + "\nSuccessfully set set {} to sudo user!!".format(
            user_member.first_name
        )
    )

@run_async
@dev_plus
def rmsudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    if user_id not in SUDO_USERS:
        message.reply_text("This member is not a Sudo user!!")
        return ""
    SUDO_USERS.remove(user_id)
    
    update.effective_message.reply_text(
        rt
        + "\nSuccessfully removed {} from sudo user!!".format(
            user_member.first_name
        )
    )

SUDO_HANDLER = CommandHandler(("addsudo"), addsudo)
RMSUDO_HANDLER = CommandHandler(("rmsudo"), rmsudo)

dispatcher.add_handler(SUDO_HANDLER)
dispatcher.add_handler(RMSUDO_HANDLER)

__mod_name__ = "sudos"
__handlers__ = [
    SUDO_HANDLER,
    RMSUDO_HANDLER,
]
