import os
import sys
import asyncio
from pyrogram import Client, idle
from pyrogram.raw import functions, types

User = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)



User.start()
print('Started')
