import os
import sys
import asyncio
from pyrogram import Client, idle
from config import Config
from pyrogram.raw import functions, types
from handel.data.user import User
app = Client(
    ":memory:",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="handel.data"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")



app.start()
await lol = app.send_message(Config.CHAT_ID, "**Video Player Bot is Online**")
User.start()
await lol.edit("**Video Player Bot is Online**\n**User Id online**")
print('Started')
idle()
app.stop()
User.stop()
