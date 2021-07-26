import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from files import BOT_TOKEN, API_ID, API_HASH

if __name__ == "__main__" :
    plugins = dict(
        root="mt_id_bot"
    )
    mt_botz = Client(
        "MT ID BOT",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins,
        workers=100
    )
    mt_botz.run()
