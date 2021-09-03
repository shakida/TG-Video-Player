import os
import sys
import asyncio
from pyrogram import Client, idle
from config import Config
from pyrogram.raw import functions, types

app = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH,
    plugins=dict(root="handel.data"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

await app.start()
print('started')
await pyrogram.idle()

await app.stop()
print('stopped')
