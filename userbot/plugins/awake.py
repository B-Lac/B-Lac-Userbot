"""Check if userbot awake or not . 

"""
from userbot import ALIVE_NAME
from userbot.Config import Var
from userbot.utils import admin_cmd

ALIVE_PIC = Var.ALIVE_PHOTTO
if ALIVE_PIC is None:
    ALIVE_PIC = "https://l.top4top.io/m_194605zdm0.mp4"


DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)

ALIVE_MESSAGE = Var.ALIVE_MSG
if ALIVE_MESSAGE is None:
    ALIVE_MESSAGE = "**🔱Black Lightning IS Awake🔱 \n\n\n**"
    ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
    ALIVE_MESSAGE += f"`Telethon: TELETHON-15.0.0 \n\n`"
    ALIVE_MESSAGE += f"`Python: PYTHON-3.8.5 \n\n`"
    ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n\n`"
    ALIVE_MESSAGE += f"`Support Channel` : @IXKKl \n\n"
    ALIVE_MESSAGE += f"`MY BOSS🤗`: {DEFAULTUSER} \n\n "


# @command(outgoing=True, pattern="^.h$")
@borg.on(admin_cmd(pattern=r"h"))
async def amireallyalive(h):
    """For .awake command, check if the bot is running."""
    await awake.delete()
    await borg.send_file(awake.chat_id, ALIVE_PIC, caption=ALIVE_MESSAGE)
