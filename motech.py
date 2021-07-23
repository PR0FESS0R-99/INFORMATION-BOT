import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from files import UPDATE_CHANNEL

Motechyt = Client(
            "MT ID BOT",
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

# start and Update channel added
@Motechyt.on_message(filters.private & filters.command("start"))
async def start(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="<b>📢 JOIN MY UPDATE CHANNEL 📢</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 💢 𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 💢 ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"💢Add This Channel @{UPDATE_CHANNEL}")
            return  

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
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="<b>📢 JOIN MY UPDATE CHANNEL 📢</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 💢 𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 💢 ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"💢Add This Channel @{UPDATE_CHANNEL}")
            return 

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
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="<b>📢 JOIN MY UPDATE CHANNEL 📢</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 💢 𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 💢 ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"💢Add This Channel @{UPDATE_CHANNEL}")
            return 

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
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await msg.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await msg.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await msg.reply_text(
                text="<b>📢 JOIN MY UPDATE CHANNEL 📢</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 💢 𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 💢 ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"💢Add This Channel @{UPDATE_CHANNEL}")
            return 
    if msg.forward_from:
        text = "<b>🤫Forward Information🤫</b> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<b>🤖Bot</b>"
        else:
            text += "<b>👤User</b>"
        text += f'\nn👨‍💼Name{msg.forward_from["first_name"]} \n'
        if msg.forward_from["username"]:
            text += f'\n🔗 UserName : @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n🆔 ID : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️ERROR {hidden} ❌️ERROR",
                quote=True,
            )
        else:
            text = f"<b>Forward Information👀</b>."
            if msg.forward_from_chat["type"] == "channel":
                text += "\n\n<b>📢 Channel</b>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "\n\n<b>🗣️ Group</b>\n\n"
            text += f'📃 Name\n{msg.forward_from_chat["title"]} \n\n'
            if msg.forward_from_chat["username"]:
                text += f'<b>➡️ From</b> : @{msg.forward_from_chat["username"]} \n\n'
                text += f'<b>🆔 ID</b> : `{msg.forward_from_chat["id"]}`\n\n'
            else:
                text += f'<b>🆔 ID</b> `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
     
# Sticker ID WOULD GET COPYRIGHT UNDER AND RE GENERATED AND MODED BY @MR-JINN-OFTG
@Motechyt.on_message(filters.private & ~filters.forwarded & ~filters.command(["start", "about", "help", "id"]))
async def stickers(idbot, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="<b>📢 JOIN MY UPDATE CHANNEL 📢</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 💢 𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 💢 ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return

    if msg.sticker:
        await msg.reply(f"This Sticker's ID is `{msg.sticker.file_id}`", quote=True)
    else:
        await msg.reply(f"Your Telegram ID is : `{msg.from_user.id}`")       
Motechyt.run()

    
