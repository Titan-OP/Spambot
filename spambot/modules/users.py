from io import BytesIO
from time import sleep

from telegram import TelegramError, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)

import spambot.modules.sql.users_sql as sql
from spambot import DEV_USERS, LOGGER, OWNER_ID, dispatcher
from spambot.modules.helper_funcs.chat_status import dev_plus, sudo_plus
from spambot.modules.sql.users_sql import get_all_users

USERS_GROUP = 4
CHAT_GROUP = 5
DEV_AND_MORE = DEV_USERS.append(int(OWNER_ID))


def get_user_id(username):
    # ensure valid userid
    if len(username) <= 5:
        return None

    if username.startswith("@"):
        username = username[1:]

    users = sql.get_userid_by_name(username)

    if not users:
        return None

    elif len(users) == 1:
        return users[0].user_id

    else:
        for user_obj in users:
            try:
                userdat = dispatcher.bot.get_chat(user_obj.user_id)
                if userdat.username == username:
                    return userdat.id

            except BadRequest as excp:
                if excp.message == "Chat not found":
                    pass
                else:
                    LOGGER.exception("Error extracting user ID")

    return None
