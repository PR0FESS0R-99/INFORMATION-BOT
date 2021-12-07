from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


# Inline Mode
@MT_ID_Bot.on_inline_query()
async def answer(_, inline_query):
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title=f"Your Telegram ID is {inline_query.from_user.id}",
				input_message_content=InputTextMessageContent(
					f"My Telegram ID is `{inline_query.from_user.id}`"
				),
				description="Tap to send your ID to current chat",
				thumb_url="https://telegra.ph/file/ff43cd1685dafe59ef7bb.jpg",
			)
		],
		cache_time=1,
	)
