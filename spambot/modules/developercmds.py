import os
import subprocess
import sys
import time
from datetime import datetime
from math import ceil
from contextlib import suppress
from time import sleep

import spambot

from spambot import (
    DEV_USERS,
    OWNER_ID,
    MASTER_NAME,
    SUDO_USERS,
    Start_time,
    dispatcher,
)
from spambot.modules.helper_funcs.chat_status import dev_plus, sudo_plus
from telegram import TelegramError, Update
from telegram.error import Unauthorized

from spambot.modules.helper_funcs.extraction import extract_user
from telegram.ext import CallbackContext, CommandHandler, run_async, CallbackQueryHandler, MessageHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update


DEFAULTUSER = str(MASTER_NAME)

def TeamArsenic_time(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    TeamArsenic_ret = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if TeamArsenic_ret.endswith(":"):
        return TeamArsenic_ret[:-1]
    else:
        return TeamArsenic_ret


ping_buttons = [
    [
        InlineKeyboardButton(text="Check Ping", callback_data="pings")
    ]
]

@run_async
@sudo_plus
def restart(update: Update, context: CallbackContext):
    update.effective_message.reply_text("Restarting bot...")
    args = [sys.executable, "-m", "spambot"]
    os.execl(sys.executable, *args)
    

@run_async
@sudo_plus
def ping(update: Update, context: CallbackContext):
    ping_start = datetime.now()
    ping_end = datetime.now()
    ms = (ping_end-ping_start).microseconds / 1000
    uptime = TeamArsenic_time((time.time() - Start_time) * 1000)
    update.effective_message.reply_text(f"•• Pᴏɴɢ !! ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ : {ms}ᴍs\n⏳ Uᴘᴛɪᴍᴇ - {uptime}")


@run_async
@sudo_plus
def leave(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
        except TelegramError:
            update.effective_message.reply_text(
                "**Oops! Something went wrong!**"
            )
            return
        with suppress(Unauthorized):
            update.effective_message.reply_text("**Successfully left that chat!**")
    else:
        update.effective_message.reply_text("**Am I a joke to you?\nSend a valid chat id bruhh!**")


# @run_async
# @sudo_plus
# def renovate(update: Update, context: CallbackContext):
#     message = update.effective_message
#     user = update.effective_user
#     chat = update.effective_chat
#     bot, args = context.bot, context.args
    
    
    
#     sent_msg = update.effective_message.reply_text(
#         "Trying to sync with github repo..."
#     )
#     subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)

#     sent_msg_text = sent_msg.text + "\n\nI guess bot is synced... restarting in "

#     for i in reversed(range(5)):
#         sent_msg.edit_text(sent_msg_text + str(i + 1))
#         sleep(1)

#     sent_msg.edit_text("Restarted.")

#     os.system("restart.bat")
#     os.execv("start.bat", sys.argv)





LEAVE_HANDLER = CommandHandler("leave", leave)
# UPDATE_HANDLER = CommandHandler("updates", renovate)
RESTART_HANDLER = CommandHandler("restart", restart)
PING_HANDLER = CommandHandler("ping", ping)


dispatcher.add_handler(LEAVE_HANDLER)
dispatcher.add_handler(PING_HANDLER)
# dispatcher.add_handler(UPDATE_HANDLER)
dispatcher.add_handler(RESTART_HANDLER)

__mod_name__ = "developercmds"
__handlers__ = [RESTART_HANDLER, LEAVE_HANDLER, PING_HANDLER]
