import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Motechyt = Client(
            "MT ID BOT",
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

@Motechyt.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    text = f"""
<b> 👋Hello {motech.from_user.mention}

<b>I CAN GET ANY PUBLIC AND PRIVATE CHANNEL ID

FORWARD A MESSAGE FROM YOUR CHANNEL TO GET YOUR CHANNEL ID.

CLICK /ID GET YOUR ID

CLICK /INFO GET YOUR TELEGRAM INFO </b>
"""
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
async def info(motech, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None🥲"
    text = f"""
<b>🙋🏻‍♂️ First Name :</b> {update.from_user.first_name}

<b>🧖‍♂️ Second Name :</b> {last_name}

<b>🧑🏻‍🎓 Username :</b> @{update.from_user.username}

<b>🆔 Telegram ID :</b> <code>{update.from_user.id}</code>

<b>🔗 Profile Link :</b> {update.from_user.mention}

<b>  © @Mo_Tech_YT</b>
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
🆔 Your Telegram ID : <code>{update.from_user.id}</code>
"""
    reply_markup = MT_START
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

Motechyt.run()
