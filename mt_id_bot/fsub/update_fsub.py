#  update_channel = UPDATE_CHANNEL
#    if update_channel:
#        try:
#            user = await mt_id_bot.get_chat_member(update_channel, update.chat.id)
#           if user.status == "kicked out":
#              await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
#               return
#        except UserNotParticipant:
#            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From mt_id_bot.py
#            await update.reply_text(
#                text="<b>📢 JOIN MY UPDATE CHANNEL 📢</b>",
#                reply_markup=InlineKeyboardMarkup([
#                    [ InlineKeyboardButton(text=" 💢 𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 💢 ", url=f"t.me/{UPDATE_CHANNEL}")]
#             ])
#           )
#           return
#       except Exception:
#            await update.reply_text(f"💢Add This Channel @{UPDATE_CHANNEL}")
#            return""" 
