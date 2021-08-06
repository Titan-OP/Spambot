"""
Credits to:
  t.me/TeamGladiators
  t.me/TeamUltroid
"""

from spambot.events import gladiator
from spambot import (
    DEV_USERS,
    OWNER_ID,
    SUDO_USERS
)
import asyncio
import io
import os
from asyncio import sleep
from telethon import utils
from telethon.tl.functions.messages import GetStickerSetRequest
from spambot.modules.helper_funcs.alternate import typing_action
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName

@typing_action
@gladiator(pattern="^/spam(?: |$)(.*)")
async def gladiators(event):
  if event.sender_id in SUDO_USERS or event.sender_id in DEV_USERS:
    try:
      xD = event.text[6:]
      ldr = xD.split(" ", 1)
      counter = int(ldr[0])
      mesg = ldr[1]
      if counter > 99:
        return await event.reply("Please give value less than or equal to 99.")
      for i in range(counter):
        await event.client.send_message(event.chat, mesg)
        await asyncio.sleep(1.5)
    except Exception as xy:
      await event.reply("Oops!! Something went wrong, forward this message to @Gladiators_Support\n\n" + str(xy))


@typing_action
@gladiator(pattern="^/dspam(?: |$)(.*)")
async def gladiators(event):
  if event.sender_id in SUDO_USERS or event.sender_id in DEV_USERS:
    try:
      xD = event.text[7:]
      lst = xD.split(" ", 2)
      tme = float(lst[0])
      counter = int(lst[1])
      mesg = lst[2]
      for i in range(counter):
        await event.client.send_message(event.chat, mesg)
        await asyncio.sleep(tme)
    except Exception as xy:
      await event.reply("Oops!! Something went wrong, forward this message to @Gladiators_Support\n\n" + str(xy))



@typing_action
@gladiator(pattern="^/mspam(?: |$)(.*)")
async def gladiators(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
      try:
        reply = await e.get_reply_message()
        text = e.text.split()
        counter = int(text[1])
        counter += 1
        media = await reply.download_media( "SpamBot/downloads/")
        for i in range(1, counter):
          await e.client.send_file(e.chat_id, media)
          await asyncio.sleep(2)
        os.remove(media)
      except Exception as xy:
        await e.reply("Oops!! Something went wrong, forward this message to @Gladiators_Support\n\n" + str(xy))

@typing_action
@gladiator(pattern="^/packspam(?: |$)(.*)")
async def _(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
      try:
        x = await e.get_reply_message()
        if not (x and x.media and hasattr(x.media, "document")):
          return await e.reply("`Reply To Sticker Only.`")
        set = x.document.attributes[1]
        sset = await e.client(
          GetStickerSetRequest(
            InputStickerSetID(
              id=set.stickerset.id,
              access_hash=set.stickerset.access_hash,
            )
          )
        )
        pack = sset.set.short_name
        docs = [
          utils.get_input_document(x)
          for x in (
            await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
          ).documents
        ]
        for xx in docs:
          await e.client.send_file(e.chat_id, file=(xx))
          await asyncio.sleep(2)
      except Exception as xy:
        await e.reply("Oops!! Something went wrong, forward this message to @Gladiators_Support\n\n" + str(xy))
        
        
@typing_action
@gladiator(pattern="^/bigspam(?: |$)(.*)")
async def gladiators(event):
  if event.sender_id in SUDO_USERS or event.sender_id in DEV_USERS:
    try:
      xD = event.text[9:]
      ldr = xD.split(" ", 1)
      counter = int(ldr[0])
      mesg = ldr[1]
      for i in range(counter):
        await event.client.send_message(event.chat, mesg)
        await asyncio.sleep(2)
    except Exception as xy:
      await event.reply("Oops!! Something went wrong, forward this message to @Gladiators_Support\n\n" + str(xy))



@typing_action
@gladiator(pattern="^/uspam(?: |$)(.*)")
async def gladiators(event):
  if event.sender_id in SUDO_USERS or event.sender_id in DEV_USERS:
    try:
      xD = event.text[7:]
      a = 1
      while a == 1:
        await event.client.send_message(event.chat, xD)
        await asyncio.sleep(2)
    except Exception as xy:
      await event.reply("Oops!! Something went wrong, forward this message to @Gladiators_Support\n\n" + str(xy))
