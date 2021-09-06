import os
import re
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    CHAT_ID = int(os.environ.get("CHAT_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_STRING = os.environ.get("SESSION_STRING", "")
