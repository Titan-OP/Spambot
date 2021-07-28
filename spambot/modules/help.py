from spambot.events import register
from spambot import (
    DEV_USERS,
    OWNER_ID,
    OWNER_USERNAME,
    SUDO_USERS
)
import asyncio
import io
import os
from asyncio import sleep
from telethon import utils
client = tbot


DEFAULTUSER = str(OWNER_USERNAME)

help_img = "https://telegra.ph/file/6e92103071aa47ee7023e.mp4"
help_caption = """
**░░░▒▒▓ᏂᏋᏝᎮ ᎷᏋᏁᏬ▓▒▒░░░**

**/addsudo:** use this while replying to anyone will add him as a sudo user!!

**/rmsudo:** use this while replying to anyone will remove him from sudo user!!

**/spam:** Spams text for given counter!!\nSyntax: /spam <counter>;<text>

**/dspam:** Delay spam a text for given counter after given time!!
Syntax: /dspam <seconds>;<counter>;<text>

**/mspam:** Spams media for given counter!!
Syntax: /mspam <counter>
(replying to any media)

**/packspam:** Spams all stickers from sticker pack!!
Syntax: /packspam (replying to any sticker)

**/replyraid:** Activates reply raid on the user!!
Syntax: /replyraid (replying to anyone)

**/dreplyraid:** Deactivates reply raid on the user!!
Syntax: /dreplyraid (replying to anyone)

©️ @TeamGladiators
"""

start_img = "https://telegra.ph/file/1312f063f0395fc933edd.mp4"
start_caption = f"""
Now let me introduce myself.
I am most powerfull Spam-Bot ever made!
I'm here to destroy your opponent 🔥[🔥](https://telegra.ph/file/1312f063f0395fc933edd.mp4)🔥
I can spam continuosly with less flood-wait error and more accuracy!

_↼★᭄ꦿ᭄ꦿmaster★᭄ꦿ᭄ꦿ⇀_
**『 [{DEFAULTUSER}](tg://user?id={OWNER_ID}) 』**

©️ @TeamGladiators
"""



startbuttons = [
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
        InlineKeyboardButton(text="Back", callback_data="back")
        InlineKeyboardButton(text="Close", callback_data="close")
    ]
]


helpbuttons = [
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
  

# @register(pattern="^/start(?: |$)(.*)")
# async def gladiators(event):
#  if "-" not in str(event.chat_id):
#    try:
#        await event.client.send_file(event.chat_id, start_img, caption=f"Now let me introduce myself.\nI am most powerfull spam-bot ever made\nI'm here to destroy your opponent!!\nI can spam continuosly with less flood-wait error and more accuracy!\n\n_↼★᭄ꦿ᭄ꦿmaster★᭄ꦿ᭄ꦿ⇀_\n**『 [{DEFAULTUSER}](tg://user?id={OWNER_ID}) 』**\n\n©️ @TeamGladiators")
#    except:
#        await event.client.send_message(event.chat_id, f"Now let me introduce myself.\nI am most powerfull spam-bot ever made\nI'm here to destroy your opponent!!\nI can spam continuosly with less flood-wait error and more accuracy!\n\n_↼★᭄ꦿ᭄ꦿmaster★᭄ꦿ᭄ꦿ⇀_\n**『 [{DEFAULTUSER}](tg://user?id={OWNER_ID}) 』**\n\n©️ @TeamGladiators")


# @register(pattern="^/help(?: |$)(.*)")
# async def gladiators(event):
#   if event.sender_id in SUDO_USERS or event.sender_id in DEV_USERS:
#     if "-" in str(event.chat_id):
#         try:
#             await event.reply(help_img, caption=f"**░░░▒▒▓ᏂᏋᏝᎮ ᎷᏋᏁᏬ▓▒▒░░░**\n\n**/addsudo:** use this while replying to anyone will add him as a sudo user!!\n\n**/rmsudo:** use this while replying to anyone will remove him from sudo user!!\n\n**/spam:** Spams text for given counter!!\nSyntax: /spam <counter>;<text>\n\n**/dspam:** Delay spam a text for given counter after given time!!\nSyntax: /dspam <seconds>;<counter>;<text>\n\n**/mspam:** Spams media for given counter!!\nSyntax: /mspam <counter>\n(replying to any media)\n\n**/packspam:** Spams all stickers from sticker pack!!\nSyntax: /packspam\n(replying to any sticker)\n\n**/replyraid:** Activates reply raid on the user!!\nSyntax: /replyraid\n(replying to anyone)\n\n**/dreplyraid:** Deactivates reply raid on the user!!\nSyntax: /dreplyraid\n(replying to anyone)\n\n©️ @TeamGladiators")
#         except:
#             await event.reply(f"**░░░▒▒▓ᏂᏋᏝᎮ ᎷᏋᏁᏬ▓▒▒░░░**\n\n**/addsudo:** use this while replying to anyone will add him as a sudo user!!\n\n**/rmsudo:** use this while replying to anyone will remove him from sudo user!!\n\n**/spam:** Spams text for given counter!!\nSyntax: /spam <counter>;<text>\n\n**/dspam:** Delay spam a text for given counter after given time!!\nSyntax: /dspam <seconds>;<counter>;<text>\n\n**/mspam:** Spams media for given counter!!\nSyntax: /mspam <counter>\n(replying to any media)\n\n**/packspam:** Spams all stickers from sticker pack!!\nSyntax: /packspam\n(replying to any sticker)\n\n**/replyraid:** Activates reply raid on the user!!\nSyntax: /replyraid\n(replying to anyone)\n\n**/dreplyraid:** Deactivates reply raid on the user!!\nSyntax: /dreplyraid\n(replying to anyone)\n\n©️ @TeamGladiators")
#     else:
#         try:
#             await event.client.send_file(event.chat_id, help_img, caption="**░░░▒▒▓ᏂᏋᏝᎮ ᎷᏋᏁᏬ▓▒▒░░░**\n\n**/addsudo:** use this while replying to anyone will add him as a sudo user!!\n\n**/rmsudo:** use this while replying to anyone will remove him from sudo user!!\n\n**/spam:** Spams text for given counter!!\nSyntax: /spam <counter>;<text>\n\n**/dspam:** Delay spam a text for given counter after given time!!\nSyntax: /dspam <seconds>;<counter>;<text>\n\n**/mspam:** Spams media for given counter!!\nSyntax: /mspam <counter>\n(replying to any media)\n\n**/packspam:** Spams all stickers from sticker pack!!\nSyntax: /packspam\n(replying to any sticker)\n\n**/replyraid:** Activates reply raid on the user!!\nSyntax: /replyraid\n(replying to anyone)\n\n**/dreplyraid:** Deactivates reply raid on the user!!\nSyntax: /dreplyraid\n(replying to anyone)\n\n©️ @TeamGladiators")
#         except:
#             await event.client.send_message(event.chat_id, "**░░░▒▒▓ᏂᏋᏝᎮ ᎷᏋᏁᏬ▓▒▒░░░**\n\n**/addsudo:** use this while replying to anyone will add him as a sudo user!!\n\n**/rmsudo:** use this while replying to anyone will remove him from sudo user!!\n\n**/spam:** Spams text for given counter!!\nSyntax: /spam <counter>;<text>\n\n**/dspam:** Delay spam a text for given counter after given time!!\nSyntax: /dspam <seconds>;<counter>;<text>\n\n**/mspam:** Spams media for given counter!!\nSyntax: /mspam <counter>\n(replying to any media)\n\n**/packspam:** Spams all stickers from sticker pack!!\nSyntax: /packspam\n(replying to any sticker)\n\n**/replyraid:** Activates reply raid on the user!!\nSyntax: /replyraid\n(replying to anyone)\n\n**/dreplyraid:** Deactivates reply raid on the user!!\nSyntax: /dreplyraid\n(replying to anyone)\n\n©️ @TeamGladiators")

    
@run_async
def start(update: Update, context: CallbackContext):
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
