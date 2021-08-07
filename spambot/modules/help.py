import importlib
import time
import re
from sys import argv
from spambot.events import gladiator
from spambot import (
    DEV_USERS,
    OWNER_ID,
    MASTER_NAME,
    SUDO_USERS
)
from spambot import (
    ALLOW_EXCL,
    CERT_PATH,
    TOKEN,
    URL,
    dispatcher,
    StartTime,
    telethn,
    pbot,
    updater,
)
import asyncio
import io
import os
from asyncio import sleep
from telethon import utils
from spambot.modules.helper_funcs.chat_status import dev_plus, sudo_plus
from spambot.modules.helper_funcs.extraction import extract_user
from telegram.ext import CallbackContext, CommandHandler, run_async, CallbackQueryHandler, MessageHandler, DispatcherHandlerStop
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update




DEFAULTUSER = str(MASTER_NAME)
help_img = "https://telegra.ph/file/6e92103071aa47ee7023e.mp4"
dev_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**


**/ping:** Check ping of the server!!
**/addsudo:** Use this while replying to anyone will add him as a sudo user!!
**/rmsudo:** Use this while replying to anyone will remove him from sudo user!!
**/leave <chat id>:** Bot will leave that chat!!
**/updates:** Check new updates and updates the bot!!
**/restart:** Restarts the bot!!(Too fast!! **Supersonic**)

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @TeamGladiators
"""
spam_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

**/spam:** Spams text for given counter!!\nSyntax: /spam <counter> <text>
**/uspam:** Spams text continuosly!!\nSyntax: /uspam <text>
**/dspam:** Delay spam a text for given counter after given time!!
Syntax: /dspam <seconds> <counter> <text>
**/mspam:** Spams media for given counter!!
Syntax: /mspam <counter>
(replying to any media)
**/packspam:** Spams all stickers from sticker pack!!
Syntax: /packspam (replying to any sticker)
**/replycurse:** Activates reply and curse on the user!!
Syntax: /replycurse (replying to anyone)
**/dreplycurse:** Deactivates reply and curse on the user!!
Syntax: /dreplycurse (replying to anyone)

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @TeamGladiators
"""
start_img = "https://telegra.ph/file/1312f063f0395fc933edd.mp4"
help_caption = """
**Hᴇʏ ᴍᴀsᴛᴇʀ,
ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜᴇ ᴡʜᴏʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴜsɪɴɢ ᴛʜᴇ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴs!**

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @TeamGladiators
"""
start_caption = f"""
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ.
I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ-ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ!
I'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇsᴛʀᴏʏ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ 🔥🔥🔥
I ᴄᴀɴ sᴘᴀᴍ ᴄᴏɴᴛɪɴᴜᴏsʟʏ ᴡɪᴛʜ ʟᴇss ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀ ᴀɴᴅ ᴡɪᴛʜ ᴍᴏʀᴇ ᴀᴄᴄᴜʀᴀᴄʏ!**
**█▓▒­░⡷⠂ᗰᗩՏTᗴᖇ⠂⢾░▒▓█**
**『 [{DEFAULTUSER}](tg://user?id={OWNER_ID}) 』**

[©️](https://telegra.ph/file/ec3c057fcba5594151601.jpg) @TeamGladiators
"""
close_caption = """
**Hᴇʟᴘ ᴍᴇɴᴜ ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ!!**

©️ @TeamGladiators
"""
helpbuttons = [
    [
        InlineKeyboardButton(text="Spam Cmds", callback_data="spamcmds"),
        InlineKeyboardButton(text="Dev Cmds", callback_data="devcmds")
    ],
    [
        InlineKeyboardButton(text="Close", callback_data="close")
    ]
]

help_buttons = [
    [
        InlineKeyboardButton(text="Back", callback_data="back"),
        InlineKeyboardButton(text="Close", callback_data="close")
    ]
]
startbuttons = [
    [
        InlineKeyboardButton(
            text="Repo", url="https://github.com/Gladiators-Projects/SpamBot"),
        InlineKeyboardButton(
            text="Support", url=f"https://t.me/Gladiators_Support"
        ),
    ],
    [
        InlineKeyboardButton(
            text="Github Organisation", url="https://github.com/Gladiators-Projects"),
    ]
]
  
openbuttons = [
    [
        InlineKeyboardButton(text="Open Again", callback_data="open")
    ]
]
   
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
@run_async
@sudo_plus
def help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        help_caption,
        reply_markup=InlineKeyboardMarkup(helpbuttons),
        parse_mode=ParseMode.MARKDOWN,
        timeout=60,
    )


@run_async
@sudo_plus
def help_menu(update, context):
    query = update.callback_query
    if query.data == "spamcmds":
        query.message.edit_text(
            text=spam_caption,
            reply_markup=InlineKeyboardMarkup(help_buttons),
            parse_mode=ParseMode.MARKDOWN,
        )
    if query.data == "devcmds":
        query.message.edit_text(
            text=dev_caption,
            reply_markup=InlineKeyboardMarkup(help_buttons),
            parse_mode=ParseMode.MARKDOWN,
        )
    if query.data == "back":
        query.message.edit_text(
            text=help_caption,
            reply_markup=InlineKeyboardMarkup(helpbuttons),
            parse_mode=ParseMode.MARKDOWN,
        )
    if query.data == "open":
        query.message.edit_text(
            text=help_caption,
            reply_markup=InlineKeyboardMarkup(helpbuttons),
            parse_mode=ParseMode.MARKDOWN,
        )
    if query.data == "close":
        query.message.edit_text(
            text=close_caption,
            reply_markup=InlineKeyboardMarkup(openbuttons),
            parse_mode=ParseMode.MARKDOWN,
        )






start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
spamcmds_handler = CallbackQueryHandler(help_menu, pattern="spamcmds")
devcmds_handler = CallbackQueryHandler(help_menu, pattern="devcmds")
back_handler = CallbackQueryHandler(help_menu, pattern="back")
open_handler = CallbackQueryHandler(help_menu, pattern="open")
close_handler = CallbackQueryHandler(help_menu, pattern="close")
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(open_handler)
dispatcher.add_handler(close_handler)
dispatcher.add_handler(spamcmds_handler)
dispatcher.add_handler(devcmds_handler)
dispatcher.add_handler(back_handler)
