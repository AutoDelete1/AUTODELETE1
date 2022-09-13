import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "8192282"))
API_HASH = environ.get("API_HASH", "990a85e4f02364ddf5927728e75450b5")
BOT_TOKEN = environ.get("BOT_TOKEN", "2003350455:AAH0J2h2lm6vUeUrSjustbl8Z1jiQi1IyVY")
SESSION = environ.get("SESSION", "BQCQ-iY7B6PuFhpxxK0u9WnQqdivMLrIEHilv7z01uPqQI5A8zeiFqRciEmk4w0vhFbA23dnWP6lz9Nzo865NzenHi-rjxgIv2djUjhgSy3apmiCEAYVtir6CbG7ppxS0uw2RV1AEwJUxhtDhLGXDeBbEssN5ME16vpVhL5EgM54_fXbQLd_Tm4XivB01wn8WenUKmujfDdW2o-IEdk9hV-r5VtNV8CWjjGegBDouvxVexx71SP-LJ3wzt4ouPnqWOji3Ar-IU1xK8drcntLs5EI7f7cDM2wTQUv0_Tz1-cJgsVxW0HrXFH6grZiUmDr8czq6otAUitKUvlMxPKxTGMzMRtyrQA")
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
