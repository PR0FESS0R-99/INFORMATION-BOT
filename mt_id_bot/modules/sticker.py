from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from files import UPDATE_CHANNEL, BOT_USER_NAME
from mt_id_bot.button.cmd_button import BACK_BUTTON
from mt_id_bot.text.fsub_text import SUB_TEXT, SUB_JOIN, SUB_TRY, SUB_UPDATE

# ADDED STICKER ID GETTING. COPYRIGHT UNDER AND RE-GENERATED AND
# MODED BY @MR-JINN-OF-TG AND TO @PR0FESS0R-99

@MT_ID_Bot.on_message(filters.private & ~filters.forwarded & ~filters.command(["start", "id"]))
async def stickers(mt_id_bot, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await mt_id_bot.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await msg.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
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

    if msg.sticker:
        await msg.reply(f"𝑻𝒉𝒊𝒔 𝑺𝒕𝒊𝒄𝒌𝒆𝒓'𝒔 𝑰𝑫 𝒊𝒔 `{msg.sticker.file_id}`", quote=True)
    else:
        await msg.reply(f"𝒀𝒐𝒖𝒓 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑰𝑫 𝒊𝒔 : `{msg.from_user.id}`")       

