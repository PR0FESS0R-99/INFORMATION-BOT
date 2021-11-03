from pyrogram import filters
from pyrogram import Client as MT_ID_Bot

# ADDED STICKER ID GETTING. COPYRIGHT UNDER AND RE-GENERATED AND
# MODED BY @MR-JINN-OF-TG AND TO @PR0FESS0R-99
  
@MT_ID_Bot.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**𝐘𝐨𝐮𝐫 𝐬𝐭𝐢𝐜𝐤𝐞𝐫𝐬 𝐢𝐝 𝐢𝐬**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("𝐇𝐦𝐦𝐦 𝐢𝐭'𝐬 𝐧𝐨𝐭 𝐚 𝐬𝐭𝐢𝐜𝐤𝐞𝐫...!!!")
    
