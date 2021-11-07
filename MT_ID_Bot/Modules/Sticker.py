from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from MT_ID_Bot.Translation import Translation
from MT_ID_Bot.Config import Config

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

# ADDED STICKER ID GETTING. COPYRIGHT UNDER AND RE-GENERATED AND
# MODED BY @MR-JINN-OF-TG AND TO @PR0FESS0R-99

@MT_ID_Bot.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
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
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  
    if message.reply_to_message.sticker:
       await message.reply(f"**𝐘𝐨𝐮𝐫 𝐬𝐭𝐢𝐜𝐤𝐞𝐫𝐬 𝐢𝐝 𝐢𝐬**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("𝐇𝐦𝐦𝐦 𝐢𝐭'𝐬 𝐧𝐨𝐭 𝐚 𝐬𝐭𝐢𝐜𝐤𝐞𝐫...!!!")
    
