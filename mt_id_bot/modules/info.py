from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from files import UPDATE_CHANNEL, BOT_USER_NAME
from mt_id_bot.button.cmd_button import BACK_BUTTON
from mt_id_bot.text.fsub_text import SUB_TEXT, SUB_JOIN, SUB_TRY, SUB_UPDATE

@MT_ID_Bot.on_message(filters.private & filters.command("info"))
async def info(mt_id_bot, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await mt_id_bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{SUB_JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{SUB_TRY}", url=f"https://t.me/{BOT_USER_NAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"{SUB_UPDATE} @{UPDATE_CHANNEL}")
            return

    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "𝑵𝒐𝒏𝒆😔"

        text = f"""
<b>╭──「👤」
|
├ <b>🙋🏻‍♂️ 𝑭𝒊𝒓𝒔𝒕 𝑵𝒂𝒎𝒆 : <i>{update.from_user.first_name}</i>
|
├ 🧖‍♂️ 𝑺𝒆𝒄𝒐𝒏𝒅 𝑵𝒂𝒎𝒆 : <i>{last_name}</i>
|
├ 🧑🏻‍🎓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆 :  : <i>@{update.from_user.username}</i>
|
├ 🆔 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑰𝑫 :</b> <i><code>{update.from_user.id}</code></i>
<b>|
├ 🔗 𝑷𝒓𝒐𝒇𝒊𝒍𝒆 𝑳𝒊𝒏𝒌 : <i>{update.from_user.mention}</i>
|
╰──「<i>  © @Mo_Tech_YT</i>」</b>
"""  
    reply_markup = BACK_BUTTON 
    await update.reply_text(  
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
