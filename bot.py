import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import config

logging.basicConfig(level=logging.INFO)

app = Client(
    "FileShareBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        f"Namaskara {message.from_user.mention}! Naanu File Share Bot. Nannalli movie athava file kachdare link kottu kalsutte."
    )

print("Bot is running...")
app.run()
