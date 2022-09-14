import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "8192282"))
API_HASH = environ.get("API_HASH", "990a85e4f02364ddf5927728e75450b5")
BOT_TOKEN = environ.get("BOT_TOKEN", "BQBcfJkCzoK8zGZQph3ExaDAQGuYcITCjwEgSKTZ8UHlr04OGXAQFAVmeUTLMNA_AM838vWJEveiDZxUo6NuT2lmwoOb9YBpWyFiUG6go6J9iUzfhbvqCbynWL4CVKa6bNYWfjhhwV3MEDbJgiUJLXGUsZiXSAdviL-vMr4Kz2FvIiP2CtpUi0BaMc73RUb9ox6Yhd6jTmU0cn1FeyYm8qnNYwv3NIBIvAC8udvD28Gd3ZoN9FC0-4AFBhcezlXyHxwARwTGDftbJ_bsyNlLrJBC48uyPoGKfbCaki93nzG_xe79uL0WNxojgGOfsMHp6TmGRXN-oMAP8Wy9PaSuPtrwMRtyrQA")
SESSION = environ.get("SESSION", "VUitKUvlMxPKxTGMzMRtyrQA")
TIME = int(environ.get("TIME", "10"))
GROUPS = []
for grp in environ.get("GROUPS", "-1001681225968").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS", "823882413").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
