from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from files import UPDATE_CHANNEL, BOT_USER_NAME
from mt_id_bot.text.fsub_text import SUB_TEXT, SUB_JOIN, SUB_TRY, SUB_UPDATE

@MT_ID_Bot.on_message(filters.private & filters.forwarded)
async def info(mt_id_bot, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await mt_id_bot.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await msg.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await msg.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await msg.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{SUB_JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{SUB_TRY}", url=f"https://t.me/{BOT_USER_NAME}?start=try")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"{SUB_UPDATE} @{UPDATE_CHANNEL}")
            return
    if msg.forward_from:
        text = "<b>🤫 𝑭𝒐𝒓𝒘𝒂𝒓𝒅 𝑰𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 🤫</b> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<b>🤖 𝑩𝒐𝒕</b>"
        else:
            text += "<b>👤 𝑼𝒔𝒆𝒓</b>"
        text += f'\n\n👨‍💼 𝑵𝒂𝒎𝒆 : {msg.forward_from["first_name"]} \n'
        if msg.forward_from["username"]:
            text += f'\n🔗 𝑼𝒔𝒆𝒓𝑵𝒂𝒎𝒆 : @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n🆔 𝑰𝒅 : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️𝑬𝑹𝑹𝑶𝑹 <b><i>{hidden}</i></b> ❌️𝑬𝑹𝑹𝑶𝑹",
                quote=True,
            )
        else:
            text = f"<b>𝑭𝒐𝒓𝒘𝒂𝒓𝒅 𝑰𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 👀</b>."
            if msg.forward_from_chat["type"] == "channel":
                text += "\n\n<b>📢 𝑪𝒉𝒂𝒏𝒏𝒆𝒍</b>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "\n\n<b>🗣️ 𝑮𝒓𝒐𝒖𝒑</b>\n\n"
            text += f'📃 𝑵𝒂𝒎𝒆\n{msg.forward_from_chat["title"]} \n\n'
            if msg.forward_from_chat["username"]:
                text += f'<b>➡️ 𝑭𝒓𝒐𝒎</b> : @{msg.forward_from_chat["username"]} \n\n'
                text += f'<b>🆔 𝑰𝑫</b> : `{msg.forward_from_chat["id"]}`\n\n'
            else:
                text += f'<b>🆔 𝑰𝑫 </b> `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
