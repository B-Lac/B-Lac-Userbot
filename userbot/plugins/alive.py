# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# modified by Pawan jatt
# Kang with credits else gay...
import asyncio
import os
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME
from userbot.thunderconfig import Config
from userbot.utils import admin_cmd, sudo_cmd

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else " B乛LAC Uʂҽɾზσƚ"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
Blacversion = "1.5"
ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

Jatt = bot.uid
# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/74cd131c1cc3aa962f9a9.mp4"

""" =======================CONSTANTS====================== """
pm_caption = "**𝔹𝕃𝔸ℂ 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 𝕀𝕊 𝕆ℕ𝕃𝕀ℕ𝔼**\n\n"

pm_caption += f"😈𝔹𝕃𝔸ℂ 𝕌𝕊𝔼ℝ𝔹𝕆𝕋😈       : __**{Blacversion}**__\n"

pm_caption += "🛡️𝕋𝔼𝕃𝔼𝕋ℍ𝕆ℕ🛡️ : `1.19.0` \n"

pm_caption += f"⚜️𝕊𝕌𝔻𝕆⚜️            : `{sudou}`\n"

pm_caption += "⚠️ℂℍ𝔸ℕℕ𝔼𝕃⚠️   : [𝕁𝕆𝕀ℕ](https://t.me/BLAC_USERBOT)\n"

pm_caption += "🔥ℂℝ𝔼𝔸𝕋𝕆ℝ🔥    : [ℕ𝕆𝕆𝔹 ℍ𝔼ℝ𝔼](https://t.me/ERROR_404_USER_NOT_FOUNDED)\n\n"

pm_caption += "🔥𝔹𝕃𝔸ℂ 𝔾𝔸ℕ𝔾 𝕆𝕎ℕ𝔼ℝ🔥    : [𝕁𝔸𝕊𝕊𝔸 𝕁𝔸𝕋𝕋](https://t.me/JATTGAMINGYT11)\n\n"

pm_caption += "    [✨ℝ𝔼ℙ𝕆✨](https://github.com/B-Lac/B-Lac-Userbot) 🔹 [📜𝕃𝕀ℂ𝔼ℕ𝕊𝔼📜](https://github.com/B-Lac/B-Lac-Userbot/blob/master/LICENSE)\n"

pm_caption += f"➾ **𝕄𝕐 𝕄𝔸𝕊𝕋𝔼ℝ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"

pm_caption += (
    "[╔══╦╗╔══╦═╗\n║╔╗║║║╔╗║╔╝\n║╔╗║╚╣╠╣║╚╗\n╚══╩═╩╝╚╩═╝](https://t.me/BLAC_USERBOT)"
)


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
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


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(alive):
    """For .alive command, check if the bot is running."""
    if ALIVE_PHOTTO:
        pm_caption = "** B乛LAC Uʂҽɾზσƚ 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
        pm_caption += "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/BLAC_USERBOT)\n"
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/BLAC_USERBOT_GROUP)\n"
        )
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://github.com/B-Lac/B-Lac-Userbot/blob/master/License)\n"
        pm_caption += (
            "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [  B乛LAC Uʂҽɾზσƚ ](https://t.me/BLAC_USERBOT)\n"
        )
        pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/BLAC_USERBOT)"
        await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(
            alive.chat_id, ALIVE_PHOTTO, caption=pm_caption, link_preview=False
        )
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/74cd131c1cc3aa962f9a9.mp4")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(
            alive.chat_id,
            "** B乛LAC Uʂҽɾზσƚ 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
            f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
            "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
            "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/BLAC_USERBOT)\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/BLAC_USERBOT_GROUP)\n"
            "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://github.com/B-Lac/B-Lac-Userbot/blob/master/License)\n"
            "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [  B乛LAC Uʂҽɾზσƚ ](https://t.me/BLAC_USERBOT)\n"
            "[ ┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/BLAC_USERBOT)",
            link_preview=False,
        )
        await alive.delete()
