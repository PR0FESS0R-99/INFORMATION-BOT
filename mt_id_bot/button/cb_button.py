# PR0FESS0R-99/ID-Bot is licensed under the
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger
# works using a licensed work, under the same license. Copyright and license notices
# must be preserved. Contributors provide an express grant of patent rights.
# <https://www.gnu.org/licenses/>.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from mt_id_bot.text.scb_text import SCB_UPDATE, SCB_CODE, SCB_HELP, SCB_ID, SCB_INFO
from mt_id_bot.text.scb_text import SCB_INFO, SCB_BACK, SCB_ABOUT, SCB_CLOSE, SCB_START

CB_START = InlineKeyboardMarkup( [[
       InlineKeyboardButton(f"{SCB_UPDATE}", url=f"t.me/mo_tech_yt"),
       InlineKeyboardButton(f"{SCB_CODE}", url=f"https://github.com/PR0FESS0R-99/ID-Bot")
       ],[
       InlineKeyboardButton(f"{SCB_HELP}", callback_data="help")
       ]]
       )

CB_HELP = InlineKeyboardMarkup( [[
       InlineKeyboardButton(f"{SCB_ID}", callback_data="id"),
       InlineKeyboardButton(f"{SCB_INFO}", callback_data="info")
       ],[
       InlineKeyboardButton(f"{SCB_BACK}", callback_data="start"),
       InlineKeyboardButton(f"{SCB_CLOSE}", callback_data="close"),
       InlineKeyboardButton(f"{SCB_ABOUT}", callback_data="about")
       ]]
       )

CB_ABOUT = InlineKeyboardMarkup( [[
       InlineKeyboardButton(f"{SCB_BACK}", callback_data="help"),
       InlineKeyboardButton(f"{SCB_START}", callback_data="start"),
       InlineKeyboardButton(f"{SCB_CLOSE}", callback_data="close")
       ]]
       )


