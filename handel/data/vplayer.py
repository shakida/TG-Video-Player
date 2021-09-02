import os
import time
import ffmpeg
import asyncio
from asyncio import sleep
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pytgcalls import GroupCallFactory
CHAT_ID = Config.CHAT_ID
from handel.data.lol import User
STREAM = {9}
VIDEO_CALL = {}

group_call_factory = GroupCallFactory(User, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)

@Client.on_message(filters.command(["vplay"]) & (filters.chat(CHAT_ID) | filters.group))
async def stream(client, m: Message):
    if 1 in STREAM:
        await m.reply_text("Video overwrited!!")
        return
    media = m.reply_to_message
    if not media:
        await m.reply_text("**Reply a video**")
        return
    elif media.video or media.document:
        msg = await m.reply_text("**Downloading..**")
        if os.path.exists(f'VID-{CHAT_ID}.raw'):
            os.remove(f'VID-{CHAT_ID}.raw')
        try:
            video = await client.download_media(media)
            os.system(f'ffmpeg -i "{video}" -vn -f s16le -ac 2 -ar 48000 -acodec pcm_s16le -filter:a "atempo=0.81" VID-{CHAT_ID}.raw -y')
        except Exception as e:
            await msg.edit(f"`{e}")
            pass
        await sleep(7)
        group_call = group_call_factory.get_file_group_call(f'VID-{CHAT_ID}.raw')
        try:
            await group_call.start(CHAT_ID)
            await group_call.set_video_capture(video)
            VIDEO_CALL[CHAT_ID] = group_call
            await msg.edit("**Video playing..**")
            try:
                STREAM.remove(0)
            except:
                pass
            try:
                STREAM.add(1)
            except:
                pass
        except FloodWait as e:
            await sleep(e.x)
            if not group_call.is_connected:
                await group_call.start(CHAT_ID)
                await group_call.set_video_capture(video)
                VIDEO_CALL[CHAT_ID] = group_call
                await msg.edit("**Video playing..**")
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
        except Exception as e:
            await msg.edit(f"`{e}")
            return
    else:
        await m.reply_text("**Reply a video**")
        return

@Client.on_message(filters.command(["end"]) & (filters.chat(CHAT_ID) | filters.group))
async def endstream(client, m: Message):
    if 0 in STREAM:
        await m.reply_text("**Nothing is playing**!!")
        return
    try:
        await VIDEO_CALL[CHAT_ID].stop()
        await m.reply_text("**Stopped Playing!**")
        try:
            STREAM.remove(1)
        except:
            pass
        try:
            STREAM.add(0)
        except:
            pass
    except Exception as e:
        await m.reply_text(f"`{e}")
        return

# Fuck bye 
