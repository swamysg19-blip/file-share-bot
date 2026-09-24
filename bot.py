import os
from pyrogram import Client, filters
from flask import Flask
import threading

# Flask web server to satisfy Render web service port requirement
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot is running actively!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app_web.run(host="0.0.0.0", port=port)

# Pyrogram Telegram Bot
bot = Client(
    "FileShareBot",
    api_id=32365018,
    api_hash="b38f338dda9b9fb2902710bfe8dcfff",
    bot_token="8560444041:AAEZ65J_BmP6qr4_fHXoMaJ5260AUY1Nh7Y"
)

@bot.on_message(filters.command("start"))
def start_handler(client, message):
    message.reply_text(f"Namaskara {message.from_user.mention}! Naanu File Share Bot.")

if __name__ == "__main__":
    # Start Flask in a separate thread
    t = threading.Thread(target=run_web)
    t.start()

    print("Bot is starting...")
    bot.run()
