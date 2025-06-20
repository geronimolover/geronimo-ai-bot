from pyrogram import Client
import os
from config import Config

bot = Client(
    "geronimo_bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    bot.run()
