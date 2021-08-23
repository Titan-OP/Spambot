import importlib
import time
import re
from datetime import datetime
from math import ceil
from sys import argv
from spambot.events import gladiator
from spambot import (
    DEV_USERS,
    OWNER_ID,
    MASTER_NAME,
    Start_time,
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

DEFAULTUSER = str(MASTER_NAME)
help_img = "https://telegra.ph/file/6e92103071aa47ee7023e.mp4"
dev_caption = """
**★ 𝐇ᴇʟᴘ✘𝐌ᴇɴᴜ ★**


**/ping:** Check ping of the server!!

**/addsudo:** Use this while replying to anyone will add him as a sudo user!!

**/rmsudo:** Use this while replying to anyone will remove him from sudo user!!

**/leave <chat id>:** Bot will leave that chat!!

**/updates:** Check new updates and updates the bot!!

**/restart:** Restarts the bot!!(Too fast!! **Supersonic**)

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @ToxicSpamxD
"""
spam_caption = """
**★ 𝐇ᴇʟᴘ✘𝐌ᴇɴᴜ ★**

**/spam:** Spams text for given counter!!\nSyntax: /spam <counter> <text>

**/uspam:** Spams text continuosly!!\nSyntax: /uspam <text>

**/dspam:** Delay spam a text for given counter after given time!!
Syntax: /dspam <seconds> <counter> <text>

**/wspam:** Spams words in a message!!\nSyntax: /wspam <text>

**/mspam:** Spams media for given counter!!
Syntax: /mspam <counter>
(replying to any media)

**/packspam:** Spams all stickers from sticker pack!!
Syntax: /packspam (replying to any sticker)

**/hang:** Spams hanging message for given counter!!
Syntax: /hang <counter>

**/curse:** Activates curse on the user for given range!!
Syntax: /curse @telegram 10 or /curse 10 (replying to anyone)

**/ucurse:** Activates curse on the user for unlimited range!!
Syntax: /ucurse @telegram or /ucurse (replying to anyone)

**/replycurse:** Activates reply and curse on the user!!
Syntax: /replycurse (replying to anyone)

**/dreplycurse:** Deactivates reply and curse on the user!!
Syntax: /dreplycurse (replying to anyone)

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @ToxicSpamxD
"""
start_img = "https://telegra.ph/file/d8e19ed588fcc7f0050e2.jpg"
help_caption = """
**Hᴇʏ ᴍᴀsᴛᴇʀ,
ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜᴇ ᴡʜᴏʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴜsɪɴɢ ᴛʜᴇ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴs!**

[©️](https://telegra.ph/file/6e92103071aa47ee7023e.mp4) @ToxicSpamxD
"""
start_caption = f"""
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ.**
**I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ-ʙᴏᴛ.**

**|•Mʏ ɴᴀᴍᴇ ɪꜱ Tᴏxɪᴄ✘SᴘᴀᴍBᴏᴛ•|**

**I'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇsᴛʀᴏʏ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ.😈😈**
**I ᴄᴀɴ sᴘᴀᴍ ᴄᴏɴᴛɪɴᴜᴏsʟʏ ᴡɪᴛʜ ʟᴇss ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀꜱ ᴀɴᴅ ᴡɪᴛʜ ᴍᴏʀᴇ ᴀᴄᴄᴜʀᴀᴄʏ!!**

**🅼🅰🆂🆃🅴🆁**
**『 [{DEFAULTUSER}](tg://user?id={OWNER_ID}) 』**

[©️](https://telegra.ph/file/d8e19ed588fcc7f0050e2.jpg) @ToxicSpamxD
"""
close_caption = """
**Tᴏxɪᴄ✘SᴘᴀᴍBᴏᴛ Hᴇʟᴘ ᴍᴇɴᴜ ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ!!**

©️ @ToxicSpamxD
"""
helpbuttons = [
    [
        InlineKeyboardButton(text="Sᴘᴀᴍ Cᴍᴅs", callback_data="spamcmds"),
        InlineKeyboardButton(text="Dᴇᴠ Cᴍᴅs", callback_data="devcmds")
    ],
    [
        InlineKeyboardButton(text="Cʜᴇᴄᴋ Pɪɴɢ", callback_data="pings")
    ],
    [
        InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close")
    ]
]

help_buttons = [
    [
        InlineKeyboardButton(text="Bᴀᴄᴋ", callback_data="back"),
        InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close")
    ]
]
startbuttons = [
    [
        InlineKeyboardButton(
            text="Rᴇᴘᴏ", url="https://github.com/Titan-OP/SpamBot"),
        InlineKeyboardButton(
            text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/ToxicSpamxD"
        ),
    ],
    [
        InlineKeyboardButton(
            text="Cʀᴇᴀᴛᴏʀ", url="Https://t.me/ToxicBoyxD"),
    ]
]
  
openbuttons = [
    [
        InlineKeyboardButton(text="Oᴘᴇɴ Aɢᴀɪɴ", callback_data="open")
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
    if query.data == "pings":
        ping_start = datetime.now()
        ping_end = datetime.now()
        ms = (ping_end-ping_start).microseconds / 1000
        uptime = TeamArsenic_time((time.time() - Start_time) * 1000)
        pong = f"""
        ✘• Pᴏɴɢ •✘
        ••➖➖➖➖➖➖••
        📍 Pɪɴɢ Sᴘᴇᴇᴅ : {ms}ᴍs
        🔮 Uᴘᴛɪᴍᴇ : {uptime}
        ••➖➖➖➖➖➖••
               © @ToxicSpamxD
        """
        query.answer(pong, alert=True)
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
PINGS_HANDLER = CallbackQueryHandler(help_menu, pattern="pings")

dispatcher.add_handler(PINGS_HANDLER)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(open_handler)
dispatcher.add_handler(close_handler)
dispatcher.add_handler(spamcmds_handler)
dispatcher.add_handler(devcmds_handler)
dispatcher.add_handler(back_handler)
