#created by @cyper666
"""xoxbot: Avaible commands: .xnxx picx les<link>
"""


import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="xnxx?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=264121194))
              await event.client.send_message(chat, "💋2016 Videolar🔞{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Unblock @SeXn1bot```")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("😐")
          else: 
             await event.delete()
             await event.client.send_file(event.chat_id, response.message)

@borg.on(admin_cmd(pattern="picx?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=264121194))
              await event.client.send_message(chat, "♨️Old photo👙{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Unblock @SeXn1bot```")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("😐")
          else: 
             await event.delete()
             await event.client.send_file(event.chat_id, response.message)
             
@borg.on(admin_cmd(pattern="les?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=264121194))
              await event.client.send_message(chat, "🔞Uz_sex♨️{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Unblock @SeXn1bot```")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("😐")
          else: 
             await event.delete()
             await event.client.send_file(event.chat_id, response.message)
             
