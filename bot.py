import pyrogram

app = pyrogram.Client(
    "FileShareBot",
    api_id=32365018,
    api_hash="b38f338dda9b9fb2902710bfe8dcfff",
    bot_token="8560444041:AAEZ65J_BmP6qr4_fHXoMaJ5260AUY1Nh7Y"
)

@app.on_message(pyrogram.filters.command("start"))
def start_handler(client, message):
    message.reply_text(f"Namaskara {message.from_user.mention}! Naanu File Share Bot.")

print("Bot is starting successfully...")
app.run()
