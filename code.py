import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant
from files import UPDATE_CHANNEL

pr0fess0r_99 = Client(
            "MT ID BOT",
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

@pr0fess0r_99.on_message(filters.command("start"))
async def start(idbot: pr0fess0r_99, msg: Message):
        try:
            if await idbot.get_chat_member(update_channel, msg.chat.id).status == "kicked out":
               await msg.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            await msg.reply_text("Join My Update Channel",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text=" 💢 𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 💢 ", url=f"t.me/{UPDATE_CHANNEL}")]])
            )
            return

    text = f"""
<b> 👋Hello {msg.from_user.mention}</b>

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
        InlineKeyboardButton("✳️Source", url=f"https://github.com/PR0FESS0R-99/ID-Bot-V1")
     ]]
   )

pr0fess0r_99.run()
