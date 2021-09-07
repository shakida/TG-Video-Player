import os
import time
import ffmpeg
import asyncio
from asyncio import sleep
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from handel.data.user import User, Call
CHAT_ID = Config.CHAT_ID
instant = {}


@Client.on_message(filters.command(["vplay"]) & (filters.chat(CHAT_ID) | filters.group))
async def video(client, m: Message):
    media = m.reply_to_message
    if not media:
        await m.reply_text("**Reply a video !!**")
        return
    elif media.video or media.document:
        msg = await m.reply_text("**Downloading..**")
        if os.path.exists(f'{CHAT_ID}.raw'):
               os.remove(f'{CHAT_ID}.raw')
        video1 = await client.download_media(media)
        await msg.edit("**Converting...**")
        os.system(f'ffmpeg -i {video1} -f s16le -ac 1 -ar 48000 audio.raw -f rawvideo -r 24 -pix_fmt yuv420p -vf scale={SCALING}:-1 video.raw -y')
        videox = 'video.raw'
        audiox = 'audio.raw'
        await sleep(3)
        try:
            await Call.join_group_call({CHAT_ID},
            InputAudioStream(
            audiox,
            AudioParameters(
                bitrate=48000,
            ),
            InputVideoStream(
            videox,
            VideoParameters(
                width=640,
                height=360,
                frame_rate=24,
               ),
            ),
            stream_type=StreamType().local_stream,)
        except Exception as e:
            await m.reply_text(f"**Error ‼️:**\n`{e}`")
            pass
        
    else:
        await m.reply_text("**Error ‼️**")
        return

@Client.on_message(filters.command(["end"]) & (filters.chat(CHAT_ID) | filters.group))
async def end(client, m: Message):
    try:
        Call.leave_group_call({CHAT_ID}) 
        await m.reply_text("**Stopped Playing!**")
    except Exception as e:
        await m.reply_text(f"**Error ‼️:**\n`{e}`")
        return

# Fuck bye 
