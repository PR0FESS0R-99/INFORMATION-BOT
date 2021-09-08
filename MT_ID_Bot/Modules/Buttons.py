from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

ID_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 Join My Updates 📢", url=f"t.me/mo_tech_yt")
       ]]
       )
INFO_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 Join My Updates 📢", url=f"t.me/mo_tech_yt")
       ]]
       )
ID_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("↗️ 𝐆𝐞𝐭 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 ↗️", callback_data="info")
       ],[
       InlineKeyboardButton("🔙 𝐁𝐚𝐜𝐤 𝐓𝐨 𝐇𝐞𝐥𝐩 🔙", callback_data="help")
       ]]
       )
INFO_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 Join My Updates 📢", url=f"t.me/mo_tech_yt")
       ]]
       )
