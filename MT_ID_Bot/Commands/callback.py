from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from MT_ID_Bot.Translation import Translation
from MT_ID_Bot.Config import Config
from MT_ID_Bot.Commands.Buttons import START_BUTTON, HELP_BUTTON, ABOUT_BUTTON
from MT_ID_Bot.Commands.Commands import developer, co_developer, source, mt_chat, mt_bot

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe

@MT_ID_Bot.on_callback_query()
async def cb_handler(client, query):

    if query.data == "start":
        await query.answer()

        await query.message.edit_text(
            Translation.START_MSG.format(query.from_user.mention),
            reply_markup=START_BUTTON,
            disable_web_page_preview=True
        )
        return

    elif query.data == "help":
        await query.answer()

        await query.message.edit_text(
            Translation.HELP_MSG,
            reply_markup=HELP_BUTTON,
            disable_web_page_preview=True
        )
        return

    elif query.data == "about":
        await query.answer()

        await query.message.edit_text(
            Translation.ABOUT_MSG.format(BOT_USERNAME, developer, co_developer, mt_chat, mt_bot, source),
            reply_markup=ABOUT_BUTTON,
            disable_web_page_preview=True
        )
        return

    elif query.data == "close":
        await query.message.delete()
        
