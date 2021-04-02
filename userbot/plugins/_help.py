# Rewritten by @keinshin
import asyncio

from userbot import ALIVE_NAME, CMD_LIST
from userbot.utils import admin_cmd
from var import Var

DEFAULTUSER = (
    str(ALIVE_NAME)
    if ALIVE_NAME
    else "Pls Go To Heroku Vars Then in  `ALIVE_NAME`place You Telegram `Username` "
)


@borg.on(admin_cmd(pattern="help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lightningusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if lightningusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "?對? " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "`Lol Try .help`")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "\n    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit("`Wait Checking..`")
                await asyncio.sleep(2)
                await event.edit(input_str + "  ?對? is not a valid plugin????!")
        else:
            light_help_strin = """**Blac userbot Heres With The Detailed Help For CMDs** ???? !\n If Faced Any Bug Please Give The Feed Back at @lightningsupport:"""
            results = await bot.inline_query(  # pylint:disable=E0602
                lightningusername, light_help_strin
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
