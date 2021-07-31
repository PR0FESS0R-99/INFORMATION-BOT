# PR0FESS0R-99/ID-Bot is licensed under the
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger
# works using a licensed work, under the same license. Copyright and license notices
# must be preserved. Contributors provide an express grant of patent rights.
# <https://www.gnu.org/licenses/>.

from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from mt_id_bot.text.cmd_text import START_MSG, HELP_MSG, ABOUT_MSG, ID_MSG, INFO_MSG
from mt_id_bot.button.cb_button import CB_START, CB_HELP, CB_ABOUT
from mt_id_bot.button.cmd_button import BACK_BUTTON

@MT_ID_Bot.on_callback_query(filters.regex(r"^(start|help|about|id|info|close)$"))
async def callback_data(mt_id_bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
    
        reply_markup = CB_START
        
        await update.message.edit_text(
            START_MSG,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    if query_data == "help":
    
        reply_markup = CB_HELP
        
        await update.message.edit_text(
            HELP_MSG,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )

    if query_data == "about":
    
        reply_markup = CB_ABOUT
        
        await update.message.edit_text(
            ABOUT_MSG,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )

    if query_data == "info":
    
        reply_markup = BACK_BUTTON
        
        await update.message.edit_text(
            INFO_MSG.format(update.from_user.first_name, update.from_user.username, update.from_user.id, update.from_user.dc_id, update.from_user.mention),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )

    if query_data == "id":
    
        reply_markup = BACK_BUTTON
        
        await update.message.edit_text(
            ID_MSG.format(update.from_user.id),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )

    elif query_data == "close":
        await update.message.delete()


