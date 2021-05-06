from telethon import events

from userbot import ALIVE_NAME, bot

currentversion = "4.9"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Black Lightning"
PM_IMG = "https://d.top4top.io/p_1952tw95n1.jpg"
pm_caption = "➥ **المساعد:** `عبر الانترنت`\n\n"
pm_caption += "➥ **حصائيات الأنظمة**\n"
pm_caption += "➥ **نسخة Telethon:** `1.15.0` \n"
pm_caption += "➥ **بايثون:** `3.7.4` \n"
pm_caption += "➥ **حالة قاعدة البيانات‌‌:**  `وظيفي`\n"
pm_caption += "➥ **الفرع الحالي** : `رئيس`\n"
pm_caption += f"➥ **إصدار** : `{النسخة الحالية‌‌}`\n"
pm_caption += f"➥ **مديري** : {المستخدم الافتراضي} \n"
pm_caption += "➥ **قاعدة بيانات** : `عمل بشكل صحيح`\n\n"
pm_caption += "➥ **رخصة** : [المطور حسين كريم v3.0](https://t.me/IXKKl)\n"
pm_caption += "➥ **حقوق النشر** : By [@IXKKl](GitHub.com/Kenshin)\n"
pm_caption += "[المطور حسين كريم🇮🇶](https://t.me/joinchat/HybiMjGk2Xg2ZDkx)"


@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
