import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Motechyt = Client(
         "MT ID BOT",
         bot_token =os.environ.get("BOT_TOKEN", ""),
         api_id =int(os.environ.get("APP_ID", 12345)),
         api_hash =os.environ.get("API_HASH")
    )

@Motechyt.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    text = """
<b> 👋Hello {}

<b>I CAN GET ANY PUBLIC AND PRIVATE CHANNEL ID

FORWARD A MESSAGE FROM YOUR CHANNEL TO GET YOUR CHANNEL ID.

FOR USER ID USE:- /id

More information /info</b>
""".format(bot.from_user.mention)
    reply_markup =  MT_START
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

MT_START = InlineKeyboardMarkup(
     [[
        InlineKeyboardButton("🗣️Group", url=f"t.me/mo_tech_group"),
        InlineKeyboardButton("📑Bot List", url=f"t.me/mo_tech_yt"),
        InlineKeyboardButton("✳️Source", url=f"https://github.com/PR0FESS0R-99/ID-Bot")
     ]]
   )

@Motechyt.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None🥲"
    text = f"""
🙋🏻‍♂️ First Name : {update.from_user.first_name}

🧖‍♂️ Your Second Name : {last_name}

🧑🏻‍🎓 Your Username : {update.from_user.username}

🆔 Your Telegram ID : {update.from_user.id}

🔗 Your Profile Link : {update.from_user.mention}

© @Mo_Tech_YT
""" 
    reply_markup = MT_START 
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Motechyt.on_message(filters.private & filters.command("id"))
async def id(motech, update):
    text = f"""
🆔 Your Telegram ID : {update.from_user.id}
"""
    reply_markup = MT_START
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

Motechyt.run()
