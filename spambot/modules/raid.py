#Credits to @TeamGladiators

import re
import asyncio
import random
import os
from typing import Optional
from telethon import events
from telegram import Update, Bot


from spambot import (
    DEV_USERS,
    OWNER_ID,
    SUDO_USERS,
    dispatcher,
)
from spambot.modules.helper_funcs.chat_status import (
    sudo_plus,
)
from spambot.modules.helper_funcs.extraction import extract_user
from spambot.modules.helper_funcs.filters import CustomFilters
from telegram import ParseMode, TelegramError, Update
from telegram.ext import CallbackContext, CommandHandler, run_async, MessageHandler
from telegram.utils.helpers import mention_html
from spambot.events import register
from spambot import telethn as tbot

def check_user_id(user_id: int, context: CallbackContext) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "That's not a user stupid!!"

    elif user_id == bot.id:
        reply = "Why should I abuse an innocent bot -_-!!"

    else:
        reply = None
    return reply


replies = [
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI VAHEEN NHI HAI KYA? 9 MAHINE RUK SAGI VAHEEN DETA HU 🤣🤣🤩",
    "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA ✈️🛫",
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGI💣",
    "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI MAA KI CHUT KAKTE 🤱 GALI KE KUTTO 🦮 ME BAAT DUNGA PHIR 🍞 BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT",
    "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE 🆙🆒😙",
    "TERI MAA KI CHUT ME ✋ HATTH DALKE 👶 BACCHE NIKAL DUNGA 😍",
    "TERI BEHN KI CHUT ME KELE KE CHILKE 🍌🍌😍",
    "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE",
    "TERI VAHEEN DHANDHE VAALI 😋😛",
    "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI",
    "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚",
    "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE 😱😱",
    "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 🤩🤩",
    "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL 😈😈",
    "TERA PEHLA BAAP HU MADARCHOD ",
    "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA 🤡😹",
    "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGA🙌🏻☠️ ",
    "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHOD🤘🏻🙌🏻☠️ ",
    "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA 🙄🤭🤭",
    "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGA☝🏻☝🏻😬",
    "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI👀👯 ",
    "TERI MAA KI CHUT MEI BATTERY LAGA KE POWERBANK BANA DUNGA 🔋 🔥🤩",
    "TERI MAA KI CHUT MEI C++ STRING ENCRYPTION LAGA DUNGA BAHTI HUYI CHUT RUK JAYEGIIII😈🔥😍",
    "TERI MAA KE GAAND MEI JHAADU DAL KE MOR 🦚 BANA DUNGAA 🤩🥵😱",
    "TERI CHUT KI CHUT MEI SHOULDERING KAR DUNGAA HILATE HUYE BHI DARD HOGAAA😱🤮👺",
    "TERI MAA KO REDI PE BAITHAL KE USSE USKI CHUT BILWAUNGAA 💰 😵🤩",
    "BHOSDIKE TERI MAA KI CHUT MEI 4 HOLE HAI UNME MSEAL LAGA BAHUT BAHETI HAI BHOFDIKE👊🤮🤢🤢",
    "TERI BAHEN KI CHUT MEI BARGAD KA PED UGA DUNGAA CORONA MEI SAB OXYGEN LEKAR JAYENGE🤢🤩🥳",
    "TERI MAA KI CHUT MEI SUDO LAGA KE BIGSPAM LAGA KE 9999 FUCK LAGAA DU 🤩🥳🔥",
    "TERI VAHEN KE BHOSDIKE MEI BESAN KE LADDU BHAR DUNGA🤩🥳🔥😈",
    "TERI MAA KI CHUT KHOD KE USME CYLINDER ⛽️ FIT KARKE USMEE DAL MAKHANI BANAUNGAAA🤩👊🔥",
    "TERI MAA KI CHUT MEI SHEESHA DAL DUNGAAA AUR CHAURAHE PE TAANG DUNGA BHOSDIKE😈😱🤩",
    "TERI MAA KI CHUT MEI CREDIT CARD DAL KE AGE SE 500 KE KAARE KAARE NOTE NIKALUNGAA BHOSDIKE💰💰🤩",
    "TERI MAA KE SATH SUAR KA SEX KARWA DUNGAA EK SATH 6-6 BACHE DEGI💰🔥😱",
    "TERI BAHEN KI CHUT MEI APPLE KA 18W WALA CHARGER 🔥🤩",
    "TERI BAHEN KI GAAND MEI ONEPLUS KA WRAP CHARGER 30W HIGH POWER 💥😂😎",
    "TERI BAHEN KI CHUT KO AMAZON SE ORDER KARUNGA 10 rs MEI AUR FLIPKART PE 20 RS MEI BECH DUNGA🤮👿😈🤖",
    "TERI MAA KI BADI BHUND ME ZOMATO DAL KE SUBWAY KA BFF VEG SUB COMBO [15cm , 16 inches ] ORDER COD KRVAUNGA OR TERI MAA JAB DILIVERY DENE AYEGI TAB USPE JAADU KRUNGA OR FIR 9 MONTH BAAD VO EK OR FREE DILIVERY DEGI🙀👍🥳🔥",
    "TERI BHEN KI CHUT KAALI🙁🤣💥",
    "TERI MAA KI CHUT ME CHANGES COMMIT KRUGA FIR TERI BHEEN KI CHUT AUTOMATICALLY UPDATE HOJAAYEGI🤖🙏🤔",
    "TERI MAUSI KE BHOSDE MEI INDIAN RAILWAY 🚂💥😂",
    "TU TERI BAHEN TERA KHANDAN SAB BAHEN KE LAWDE RANDI HAI RANDI 🤢✅🔥",
    "TERI BAHEN KI CHUT MEI IONIC BOND BANA KE VIRGINITY LOOSE KARWA DUNGA USKI 📚 😎🤩",
    "TERI RANDI MAA SE PUCHNA BAAP KA NAAM BAHEN KE LODEEEEE 🤩🥳😳",
    "TU AUR TERI MAA DONO KI BHOSDE MEI METRO CHALWA DUNGA MADARXHOD 🚇🤩😱🥶",
    "TERI MAA KO ITNA CHODUNGA TERA BAAP BHI USKO PAHCHANANE SE MANA KAR DEGA😂👿🤩",
    "TERI BAHEN KE BHOSDE MEI HAIR DRYER CHALA DUNGAA💥🔥🔥",
    "TERI MAA KI CHUT MEI TELEGRAM KI SARI RANDIYON KA RANDI KHANA KHOL DUNGAA👿🤮😎",
    "TERI MAA KI CHUT ALEXA DAL KEE DJ BAJAUNGAAA 🎶 ⬆️🤩💥",
    "TERI MAA KE BHOSDE MEI GITHUB DAL KE APNA BOT HOST KARUNGAA 🤩👊👤😍",
    "TERI BAHEN KA VPS BANA KE 24*7 BASH CHUDAI COMMAND DE DUNGAA 🤩💥🔥🔥",
    "TERI MUMMY KI CHUT MEI TERE LAND KO DAL KE KAAT DUNGA MADARCHOD 🔪😂🔥",
    "SUN TERI MAA KA BHOSDA AUR TERI BAHEN KA BHI BHOSDA 👿😎👊",
    "TUJHE DEKH KE TERI RANDI BAHEN PE TARAS ATA HAI MUJHE BAHEN KE LODEEEE 👿💥🤩🔥",
    "SUN MADARCHOD JYADA NA UCHAL MAA CHOD DENGE EK MIN MEI ✅🤣🔥🤩",
    "APNI AMMA SE PUCHNA USKO US KAALI RAAT MEI KAUN CHODNEE AYA THAAA! TERE IS PAPA KA NAAM LEGI 😂👿😳",
    "TOHAR BAHIN CHODU BBAHEN KE LAWDE USME MITTI DAL KE CEMENT SE BHAR DU 🏠🤢🤩💥",
    "TUJHE AB TAK NAHI SMJH AYA KI MAI HI HU TUJHE PAIDA KARNE WALA BHOSDIKEE APNI MAA SE PUCH RANDI KE BACHEEEE 🤩👊👤😍",
    "TERI MAA KE BHOSDE MEI SPOTIFY DAL KE LOFI BAJAUNGA DIN BHAR 😍🎶🎶💥",
    "TERI MAA KA NAYA RANDI KHANA KHOLUNGA CHINTA MAT KAR 👊🤣🤣😳",
    "TERA BAAP HU BHOSDIKE TERI MAA KO RANDI KHANE PE CHUDWA KE US PAISE KI DAARU PEETA HU 🍷🤩🔥",
    "TERI BAHEN KI CHUT MEI APNA BADA SA LODA GHUSSA DUNGAA KALLAAP KE MAR JAYEGI 🤩😳😳🔥",
    "TOHAR MUMMY KI CHUT MEI PURI KI PURI KINGFISHER KI BOTTLE DAL KE TOD DUNGA ANDER HI 😱😂🤩",
    "TERI MAA KO ITNA CHODUNGA KI SAPNE MEI BHI MERI CHUDAI YAAD KAREGI RANDI 🥳😍👊💥",
    "TERI MUMMY AUR BAHEN KO DAUDA DAUDA NE CHODUNGA UNKE NO BOLNE PE BHI LAND GHUSA DUNGA ANDER TAK 😎😎🤣🔥",
    "TERI MUMMY KI CHUT KO ONLINE OLX PE BECHUNGA AUR PAISE SE TERI BAHEN KA KOTHA KHOL DUNGA 😎🤩😝😍",
    "TERI MAA KE BHOSDA ITNA CHODUNGA KI TU CAH KE BHI WO MAST CHUDAI SE DUR NHI JA PAYEGAA 😏😏🤩😍",
    "SUN BE RANDI KI AULAAD TU APNI BAHEN SE SEEKH KUCH KAISE GAAND MARWATE HAI😏🤬🔥💥",
    "TERI MAA KA YAAR HU MEI AUR TERI BAHEN KA PYAAR HU MEI AJA MERA LAND CHOOS LE 🤩🤣💥",
    "MADARCHOD",
    "BHOSDIKE",
    "LAAAWEEE KE BAAAAAL",
    "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL",
    "MADRCHOD..",
    "TERI MA KI CHUT..",
    "LWDE KE BAAALLL.",
    "MACHAR KI JHAAT KE BAAALLLL",
    "TERI MA KI CHUT M DU TAPA TAP?",
    "TERI MA KA BHOSDAA",
    "TERI BHN SBSBE BDI RANDI.",
    "TERI MA OSSE BADI RANDDDDD",
    "TERA BAAP CHKAAAA",
    "KITNI CHODU TERI MA AB OR..",
    "TERI MA CHOD DI HM NE",
    "TERI MA KE STH REELS BNEGA ROAD PEE",
    "TERI MA KI CHUT EK DAM TOP SEXY",
    "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP",
    "LUND KE CHODE TU KEREGA TYPIN",
    "SPEED PKD LWDEEEE",
    "BAAP KI SPEED MTCH KRRR",
    "LWDEEE",
    "PAPA KI SPEED MTCH NHI HO RHI KYA",
    "ALE ALE MELA BCHAAAA",
    "CHUD GYA PAPA SEEE",
    "KISAN KO KHODNA OR",
    "SALE RAPEKL KRDKA TERA",
    "HAHAHAAAAA",
    "KIDSSSS",
    "TERI MA CHUD GYI AB FRAR MT HONA",
    "YE LDNGE BAPP SE",
    "KIDSSS FRAR HAHAHH",
    "BHEN KE LWDE SHRM KR",
    "KITNI GLIYA PDWEGA APNI MA KO",
    "NALLEE",
    "SHRM KR",
    "MERE LUND KE BAAAAALLLLL",
    "KITNI GLIYA PDWYGA APNI MA BHEN KO",
    "RNDI KE LDKEEEEEEEEE",
    "KIDSSSSSSSSSSSS",
    "Apni gaand mein muthi daal",
    "Apni lund choos",
    "Apni ma ko ja choos",
    "Bhen ke laude",
    "Bhen ke takke",
    "Abla TERA KHAN DAN CHODNE KI BARIII",
    "BETE TERI MA SBSE BDI RAND",
    "LUND KE BAAAL JHAT KE PISSSUUUUUUU",
    "LUND PE LTKIT MAAALLLL KI BOND H TUUU",
    "KASH OS DIN MUTH MRKE SOJTA M TUN PAIDA NA HOTAA",
    "GLTI KRDI TUJW PAIDA KRKE",
    "SPEED PKDDD",
    "Gaand main LWDA DAL LE APNI MERAAA",
    "Gaand mein bambu DEDUNGAAAAAA",
    "GAND FTI KE BALKKK",
    "Gote kitne bhi bade ho, lund ke niche hi rehte hai",
    "Hazaar lund teri gaand main",
    "Jhaant ke pissu-",
    "TERI MA KI KALI CHUT",
    "Khotey ki aulda",
    "Kutte ka awlat",
    "Kutte ki jat",
    "Kutte ke tatte",
    "TETI MA KI.CHUT , tERI MA RNDIIIIIIIIIIIIIIIIIIII",
    "Lavde ke bal",
    "muh mei lele",
    "Lund Ke Pasine",
    "MERE LWDE KE BAAAAALLL",
    "HAHAHAAAAAA",
    "CHUD GYAAAAA",
    "Randi khanE KI ULADDD",
    "Sadi hui gaand",
    "Teri gaand main kute ka lund",
    "Teri maa ka bhosda",
    "Teri maa ki chut",
    "Tere gaand mein keede paday",
    "Ullu ke pathe",
    "SUNN MADERCHOD",
    "TERI MAA KA BHOSDA",
    "BEHEN K LUND",
    "TERI MAA KA CHUT KI CHTNIIII",
    "MERA LAWDA LELE TU AGAR CHAIYE TOH",
    "GAANDU",
    "CHUTIYA",
    "TERI MAA KI CHUT PE JCB CHADHAA DUNGA",
    "SAMJHAA LAWDE",
    "YA DU TERE GAAND ME TAPAA TAP��",
    "TERI BEHEN MERA ROZ LETI HAI",
    "TERI GF K SAATH MMS BANAA CHUKA HU���不�不",
    "TU CHUTIYA TERA KHANDAAN CHUTIYA",
    "AUR KITNA BOLU BEY MANN BHAR GAYA MERA�不",
    "TERIIIIII MAAAA KI CHUTTT ME ABCD LIKH DUNGA MAA KE LODE",
    "TERI MAA KO LEKAR MAI FARAR",
    "RANIDIII",
    "BACHEE",
    "CHODU",
    "RANDI",
    "RANDI KE PILLE",
    "TERIIIII MAAA KO BHEJJJ",
    "TERAA BAAAAP HU",
    "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA",
    "Teri maa KO SARAK PE LETAA DUNGA",
    "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA",
    "Teri maa KI CHUT MÉ KAALI MITCH",
    "TERI MAA SASTI RANDI HAI",
    "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD",
    "TERI MAAA RANDI HAI",
    "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD",
    "TERI MAA KAAA BHOSDAA",
    "TERI MAA KI CHUT ME LAPTOP",
    "Teri maa RANDI HAI",
    "TERI MAA KO BISTAR PE LETAAKE CHODUNGA",
    "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD",
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA",
    "TERI MAA KE GAND ME DETOL DAAL DUNGA",
    "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD",
    "TERI MAA KO SARAK PE LETAAA DUNGAAA",
    "TERI MAA KAA BHOSDA",
    "MERAAA LUND PAKAD LE MADARCHOD",
    "CHUP TERI MAA AKAA BHOSDAA",
    "TERIII MAA CHUF GEYII KYAAA LAWDEEE",
    "TERIII MAA KAA BJSODAAA",
    "MADARXHODDD",
    "TERIUUI MAAA KAA BHSODAAA",
    "TERIIIIII BEHENNNN KO CHODDDUUUU MADARXHODDDD",
    "NIKAL MADARCHOD",
    "RANDI KE BACHE",
    "TERA MAA MERI FAN",
    "TERI SEXY BAHEN KI CHUT OP",
]

chutiya = []








@tbot.on(events.NewMessage(incoming=True))
async def _(event):
  if event.sender.id in chutiya:
    await event.reply(random.choice(replies))



@run_async
@sudo_plus
def raid(update: Update, context: CallbackContext) -> str:
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
        message.reply_text("This member is a Sudo user!!")
        return ""
    chutiya.append(user_id)

    update.effective_message.reply_text(
        rt
        + "\nSuccessfully started reply raid on {} !!".format(
            user_member.first_name
        )
    )

@run_async
@sudo_plus
def draid(update: Update, context: CallbackContext) -> str:
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

    if user_id not in chutiya:
        message.reply_text("Never started reply raid on this user!!")
        return ""
    chutiya.remove(user_id)
    
    update.effective_message.reply_text(
        rt
        + "\nSuccessfully stopped reply raid on {} !!".format(
            user_member.first_name
        )
    )

RAID_HANDLER = CommandHandler(("replyraid"), raid)
DRAID_HANDLER = CommandHandler(("dreplyraid"), draid)

dispatcher.add_handler(RAID_HANDLER)
dispatcher.add_handler(DRAID_HANDLER)

__mod_name__ = "raid"
__handlers__ = [
    RAID_HANDLER,
    DRAID_HANDLER,
    
]
