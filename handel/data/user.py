import asyncio
from pyrogram import Client, filters
from config import Config
from pytgcalls import PyTgCalls



User = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)
Call = PyTgCalls(User)


run = Call.start()
