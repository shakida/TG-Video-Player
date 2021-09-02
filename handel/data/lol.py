import asyncio
from pyrogram import Client
from config import Config


User = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)
