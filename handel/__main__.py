import os
import sys
import asyncio
from pyrogram import Client, idle
from config import Config
from pyrogram.raw import functions, types

User = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)

Bot = Client(
    ":memory:",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="handel.data"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")



Bot.start()
User.start()
print("Bot & User started")

idle()
Bot.stop()
User.stop()
