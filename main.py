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


async def main():
    await app.start()
    print('started')
    await idle()
    await app.stop()
    print('stopped')

loop = asyncio.get_event_loop()
loop.run_until_complete(app())
