import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Motechyt = Client(
            "MT ID BOT",
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

# start 
@Motechyt.on_message(filters.private & filters.command("start"))
async def start(motech, update):
    text = f"""
<b> 👋Hello {update.from_user.mention}</b>

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

# Button Controler 
MT_START = InlineKeyboardMarkup(
     [[
        InlineKeyboardButton("🗣️Group", url=f"t.me/mo_tech_group"),
        InlineKeyboardButton("📑Bot List", url=f"t.me/mo_tech_yt"),
        InlineKeyboardButton("✳️Source", url=f"https://github.com/PR0FESS0R-99/ID-Bot")
     ]]
   )

# telegram information from motech.py
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

# Forwarded message id from motech.py
@Motechyt.on_message(filters.private & filters.forwarded)
async def forwarded(motech, msg):
    if msg.forward_from:
        text = "🤫Forward Information🤫\n\n"
        if msg.forward_from["is_bot"]:
            text += "<b>🤖Bot</b>\n\n"
        else:
            text += "<b>👤User</b>\n\n"
        text += f'\n👨‍💼Name{msg.forward_from["first_name"]} \n'
        if msg.forward_from["username"]:
            text += f'🔗 UserName : @{msg.forward_from["username"]} \nID : `{msg.forward_from["id"]}`'
        else:
            text += f'🆔 ID : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"Forward detected but unfortunately, {hidden} has enabled forwarding privacy, so I can't get their id",
                quote=True,
            )
        else:
            text = f"🤫Forward Information🤫. \n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<b>📢 Channel</b>\n\n"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<b>🗣️ Group</b>\n\n"
            text += f'📃 Name\n{msg.forward_from_chat["title"]} \n\n'
            if msg.forward_from_chat["username"]:
                text += f'<b>➡️ From</b> : @{msg.forward_from_chat["username"]} \n\n'
                text += f'<b>🆔 ID</b> : `{msg.forward_from_chat["id"]}`\n\n'
            else:
                text += f'<b>🆔 ID</b> `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)

Motechyt.run()
