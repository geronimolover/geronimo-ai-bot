from pyrogram import Client, idle
from config import Config

bot = Client(
    "geronimo-bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins={"root": "plugins"}
)

if __name__ == "__main__":
    bot.start()
    print("🤖 Bot started — synced with Telegram.")
    idle()
    bot.stop()
    print("🛑 Bot stopped.")

