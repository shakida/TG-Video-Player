import os
import sys
import asyncio
import pyrogram
from os import path
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw import functions, types
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types import Browsers
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import LowQualityAudio
from pytgcalls.types.input_stream.quality import LowQualityVideo
from pytgcalls.types.input_stream import AudioParameters
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputVideoStream
from pytgcalls.types.input_stream import VideoParameters


from pytgcalls import idle
S = "BQAx8V0qLC8cDQX0xp6ICAQxglOeHWznUM0mCQm9QKVevKoDXLtC5aynETMtBB-5iv1ZMAlsdqeF-gC1Qbe68XUMlknUKVfGffe4PasUI9DcX2Osf7IgLMIMQ6nXTCF8Tm3F4g_BJ9wmz-85L9g1VPDlEOHvI4ndqk-DRhqPdKSAVBZIyeUGdmxiTdpl6dz_pZYfkwKp0jQTaqQt42l-FD4rYtrjLJBU2Q4fg_-sgx0s-iFQ4lcc53MLl557PCrJAduDcp2wK3reNLkU7SXHvCEec7RxNQVhYc3BB3BX9a3TucbmYyPOtqX_9Hg8rjddxTAJ8zRFrpMUk0yrZ35N9-LqXBjAwgA"
Ap = "2687507"
Hs = "2401930e935bc7b124eecc028d47f320"
app = Client(S, Ap, Hs)


call_py = PyTgCalls(app)
call_py.start()
app.send_message(-1001297289773, f'**💋 Ready to sex!**')
   # print('start')


you = YoutubeDL(
                {
                    "outtmpl": f"downloads/%(id)s.%(ext)s",
                    "quiet": True,
                    "geo_bypass": True,
                    "nocheckcertificate": True,
                }
            )
def download(link: str) -> str:
    try:
       info = you.extract_info(link, False)
       you.download([link])
       return path.join("downloads", f"{info['id']}.{info['ext']}")
    except Exception as e:
      print(e)


@app.on_message(filters.command(["livx"]) & filters.group & ~ filters.edited)
async def live(app, message: Message):
 try:
    query = ''
    for i in message.command[1:]:
        query += '' + str(i)
  #  print(query)
    remote = query
    g = await app.send_message(message.chat.id, f'Trying...')
    try:
       await call_py.leave_group_call(message.chat.id)
    except Exception:
       # print(e)
       pass
    try:
        await call_py.join_group_call(
        message.chat.id,
        AudioVideoPiped(
            remote,
            LowQualityAudio(),
            LowQualityVideo(),
            headers={
                'User-Agent': Browsers().chrome_windows,
            },
        ),
        stream_type=StreamType().pulse_stream,
        )
        await g.delete()
        await app.send_message(message.chat.id, f'**STARTING:** `{remote}` in **{message.chat.title}**')
    except Exception as e:
        await app.send_message(message.chat.id, f'ERROR‼️ `{e}`')
      #  print(e)
        pass
    
 except Exception as e:
    await app.send_message(message.chat.id, f'ERROR ‼️ `{e}`')
 return

@app.on_message(filters.command(["plv"]) & filters.group & ~ filters.edited)
async def video(app, message: Message):
  try:
     videos = message.reply_to_message
     if videos.video or videos.document:
        f = await app.send_message(message.chat.id, f'Downloading..')
        if os.path.exists(f'VID-{message.chat.id}.raw'):
            os.remove(f'VID-{message.chat.id}.raw')
        try:
            video = await app.download_media(videos)
         #   os.system(f'ffmpeg -i "{video}" -vn -f s16le -ac 2 -ar 48000 -acodec pcm_s16le VID-{message.chat.id}.raw -y')
        #    audio = f'VID-{message.chat.id}.raw'
            await f.edit("Converting.....")
        except Exception as e:
            await app.send_message(message.chat.id, f'ERROR‼️: `{e}`')
        try:
          await call_py.leave_group_call(message.chat.id)
        except Exception:
          pass
        try:
           await call_py.join_group_call(
           message.chat.id,
           AudioVideoPiped(
           video,
           LowQualityAudio(),
           LowQualityVideo(),
           ),
           stream_type=StreamType().pulse_stream,
           )
           await f.edit(f'**VIDEO STARTED ▶️**')
        except Exception as e:
           await app.send_message(message.chat.id, f'ERROR‼️: `{e}`')
           pass
  except Exception as e:
           await app.send_message(message.chat.id, f'Video not found!\n `{e}`')
           return


@app.on_message(filters.command(["ytp"]) & filters.group & ~ filters.edited)
async def you(app, message: Message):
    try:
       query = ''
       for i in message.command[1:]:
          query += '' + str(i)
       link = query
       h = await app.send_message(message.chat.id, f'Trying to play `{link}`')
       try:
          await call_py.leave_group_call(message.chat.id)
       except Exception:
       # print(e)
          pass
       try:
          viiid = download(link)
          await call_py.join_group_call(
          message.chat.id,
          AudioVideoPiped(viiid,
            LowQualityAudio(),
            LowQualityVideo(),
          ),
          stream_type=StreamType().pulse_stream,
          )
          await h.edit(f'STARTING PLAYING: `{link}` in\n **{message.chat.title}**')
       except Exception as e:
          await app.send_message(message.chat.id, f'ERROR‼️: `{e}`')
          pass
    except Exception as e:
          await app.send_message(message.chat.id, f'ERROR ‼️: `{e}`')
          return

@app.on_message(filters.command(["kilx"]) & filters.group & ~ filters.edited)
async def kill(app, message: Message):
      try:
         await call_py.leave_group_call(message.chat.id)
         await app.send_message(message.chat.id, f'Stoped Playing ⏹️')
      except Exception as e:
         return

         
          
@call_py.on_stream_end()      
def on_stream_end(chat_id: int) -> None:
    try:
       call_py.leave_group_call(chat_id)
    except Exception as e:
       return


idle()
