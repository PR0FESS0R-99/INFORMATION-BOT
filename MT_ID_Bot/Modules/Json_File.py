from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MT_ID_Bot.Modules.Buttons import JSON_BUTTON

@Client.on_message(filters.command(["json", "response"]), group=1)
async def response_json(bot, update):
    json = update.reply_to_message
    with BytesIO(str.encode(str(json))) as json_file:
        json_file.name = "JSON.text"
        await json.reply_document(
            document=json_file,
            reply_markup=JSON_BUTTON,
            quote=True
        )
        try:
            os.remove(json_file)
        except:
            pass
