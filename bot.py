import asyncio
from pyrogram import Client, filters
import config

app = Client(
    "FileShareBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text(
        f"Namaskara {message.from_user.mention}! Naanu File Share Bot. Nannalli movie athava file kachdare link kottu kalsutte."
    )

async def main():
    await app.start()
    print("Bot is running...")
    await asyncio.idle()

if __name__ == "__main__":
    asyncio.run(main())
