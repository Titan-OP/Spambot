import importlib
import time
import re
from sys import argv
from typing import Optional
from spambot import (
    DEV_USERS,
    OWNER_ID,
    SUDO_USERS
)

from spambot import (
    ALLOW_EXCL,
    CERT_PATH,
    DONATION_LINK,
    LOGS,
    LOGGER,
    OWNER_ID,
    PORT,
    TOKEN,
    URL,
    WEBHOOK,
    dispatcher,
    StartTime,
    telethn,
    pbot,
    updater,
)

# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from spambot.modules import ALL_MODULES

from spambot.modules.helper_funcs.chat_status import dev_plus, sudo_plus
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown


# DEFAULTUSER = str(OWNER_USERNAME)

# help_img = "https://telegra.ph/file/6e92103071aa47ee7023e.mp4"
# dev_caption = """
# **░░░▒▒▓ᏂᏋᏝᎮ ᎷᏋᏁᏬ▓▒▒░░░**
# **/addsudo:** Use this while replying to anyone will add him as a sudo user!!
# **/rmsudo:** Use this while replying to anyone will remove him from sudo user!!
# **/leave <chat id>:** Bot will leave that chat!!
# **/updates:** Check new updates and updates the bot!!
# **/restart:** Restarts the bot!!(Too fast!! **Supersonic**)
# [©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @TeamGladiators
# """
# spam_caption = """
# **░░░▒▒▓ᏂᏋᏝᎮ ᎷᏋᏁᏬ▓▒▒░░░**
# **/spam:** Spams text for given counter!!\nSyntax: /spam <counter> <text>
# **/dspam:** Delay spam a text for given counter after given time!!
# Syntax: /dspam <seconds> <counter> <text>
# **/mspam:** Spams media for given counter!!
# Syntax: /mspam <counter>
# (replying to any media)
# **/packspam:** Spams all stickers from sticker pack!!
# Syntax: /packspam (replying to any sticker)
# **/replyraid:** Activates reply raid on the user!!
# Syntax: /replyraid (replying to anyone)
# **/dreplyraid:** Deactivates reply raid on the user!!
# Syntax: /dreplyraid (replying to anyone)
# [©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @TeamGladiators
# """
# start_img = "https://telegra.ph/file/1312f063f0395fc933edd.mp4"
# help_caption = """
# **Hᴇʏ ᴍᴀsᴛᴇʀ,
# ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜᴇ ᴡʜᴏʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴜsɪɴɢ ᴛʜᴇ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴs!**
# [©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @TeamGladiators
# """


# helpbuttons = [
#     [
#         InlineKeyboardButton(text="Spam Cmds", callback_data="spamcmds"),
#         InlineKeyboardButton(text="Dev Cmds", callback_data="devcmds")
#     ],
#     [
#         InlineKeyboardButton(text="Close", callback_data="close")
#     ]
# ]

# help_buttons = [
#     [
#         InlineKeyboardButton(text="Back", callback_data="back"),
#         InlineKeyboardButton(text="Back", callback_data="back"),
#         InlineKeyboardButton(text="Close", callback_data="close")
#     ]
# ]
# startbuttons = [
#     [
#         InlineKeyboardButton(
#             text="Repo", url="https://github.com/Gladiators-Projects/SpamBot"),
#         InlineKeyboardButton(
#             text="Support", url=f"https://t.me/Gladiators_Support"
#         ),
#     ],
#     [
#         InlineKeyboardButton(
#             text="Github Organisation", url="https://github.com/Gladiators-Projects"),
#     ]
# ]
  
# openbuttons = [
#     [
#         InlineKeyboardButton(text="Open Again", callback_data="open")
#     ]
# ]



def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time




IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("spambot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module




def error_handler(update, context):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = (
        "An exception was raised while handling an update\n"
        "<pre>update = {}</pre>\n\n"
        "<pre>{}</pre>"
    ).format(
        html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False)),
        html.escape(tb),
    )

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    context.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


@run_async
def start(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        return
    update.effective_message.reply_text(
        start_caption,
        reply_markup=InlineKeyboardMarkup(startbuttons),
        parse_mode=ParseMode.MARKDOWN,
        timeout=60,
    )
# @run_async
# @sudo_plus
# def help(update: Update, context: CallbackContext):
#     update.effective_message.reply_text(
#         help_caption,
#         reply_markup=InlineKeyboardMarkup(helpbuttons),
#         parse_mode=ParseMode.MARKDOWN,
#         timeout=60,
#     )


# @run_async
# @sudo_plus
# def help_menu(update, context):
#     query = update.callback_query
#     spam_cmd = re.match(r"spamcmds\((.+?)\)", query.data)
#     dev_cmd = re.match(r"devcmds\((.+?)\)", query.data)
#     back_cmd = re.match(r"back\((.+?)\)", query.data)
#     open_cmd = re.match(r"open\((.+?)\)", query.data)
#     close_cmd = re.match(r"close\((.+?)\)", query.data)
#     try:
#         if spam_cmd:
#             query.message.edit_text(
#                 text=spam_caption,
#                 reply_markup=InlineKeyboardMarkup(help_buttons),
#                 parse_mode=ParseMode.MARKDOWN,
#             )
#         elif dev_cmd:
#             query.message.edit_text(
#                 text=dev_caption,
#                 reply_markup=InlineKeyboardMarkup(help_buttons),
#                 parse_mode=ParseMode.MARKDOWN,
#             )
#         elif back_cmd:
#             query.message.edit_text(
#                 text=help_caption,
#                 reply_markup=InlineKeyboardMarkup(helpbuttons),
#                 parse_mode=ParseMode.MARKDOWN,
#             )
#         elif close_cmd:
#             query.message.edit_text(
#                 text=close_caption,
#                 reply_markup=InlineKeyboardMarkup(openbuttons),
#                 parse_mode=ParseMode.MARKDOWN,
#             )
#         elif open_cmd:
#             query.message.edit_text(
#                 text=help_caption,
#                 reply_markup=InlineKeyboardMarkup(helpbuttons),
#                 parse_mode=ParseMode.MARKDOWN,
#             )
#     except Exception as xy:
#         query.message.edit_text("Oops!! Something went wrong, forward this message to @Gladiators_Support\n\n" + str(xy))

def main():
    if LOGS is not None and isinstance(LOGS, str):
        try:
            dispatcher.bot.sendMessage(LOGS, "𝐆ʟᴀᴅɪᴀᴛᴏʀ𝐬 𝐒ᴘᴀᴍ-𝐁ᴏᴛ ʜᴀ𝐬 ʙᴇᴇɴ ᴅᴇᴘʟᴏʏᴇᴅ!\n➖➖➖➖➖➖➖➖➖\n𝐒ᴜᴘᴘᴏʀᴛ: @TeamGladiators\n➖➖➖➖➖➖➖➖➖")
        except Unauthorized:
            LOGGER.warning("Bot isnt able to send message to logger chat, go and check!")
        except BadRequest as e:
            LOGGER.warning(e.message)

    

#     help_handler = CommandHandler("help", help)
#     callback_handler = CallbackQueryHandler(help_menu, pattern=r"help_.*")
#     dispatcher.add_handler(help_handler)
#     dispatcher.add_handler(callback_handler)

    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Starting gladiators spambot using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN, certificate=open(CERT_PATH, "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Starting gladiators spambot...")
        updater.start_polling(timeout=15, read_latency=4, clean=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    pbot.start()
    main()
