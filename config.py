import os

class Config(object):

      # Bot Fater 
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      # MT MyTelegramOrg Bot
      APP_ID = int(os.environ.get("APP_ID", 12345))
      # MT MyTelegramOrg Bot
      API_HASH = os.environ.get("API_HASH")
