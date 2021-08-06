from spambot import telethn as tbot
from spambot.events import gladiator
import os
import asyncio
import os
import time
from datetime import datetime
from spambot import OWNER_ID, DEV_USERS
from spambot import TEMP_DOWNLOAD_DIRECTORY as path
from spambot import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime
water = './spambot/resources/jarv.jpg'
client = tbot




from spambot.events import load_module
import asyncio
import os
from datetime import datetime
from pathlib import Path

@gladiator(pattern="^/rpg")
async def install(event):
    if event.fwd_from:
        return
    if event.sender_id == OWNER_ID or event.sender_id == DEV_USERS:
        pass
    else:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "spambot/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.reply("Done\n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                k = await event.reply("**Error!**",
                )
                await asyncio.sleep(2)
                await k.delete()
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()
