import os
import sys
import asyncio
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw import functions, types
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types import Browsers
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo

from pytgcalls import idle
S = "BQAx8V0qLC8cDQX0xp6ICAQxglOeHWznUM0mCQm9QKVevKoDXLtC5aynETMtBB-5iv1ZMAlsdqeF-gC1Qbe68XUMlknUKVfGffe4PasUI9DcX2Osf7IgLMIMQ6nXTCF8Tm3F4g_BJ9wmz-85L9g1VPDlEOHvI4ndqk-DRhqPdKSAVBZIyeUGdmxiTdpl6dz_pZYfkwKp0jQTaqQt42l-FD4rYtrjLJBU2Q4fg_-sgx0s-iFQ4lcc53MLl557PCrJAduDcp2wK3reNLkU7SXHvCEec7RxNQVhYc3BB3BX9a3TucbmYyPOtqX_9Hg8rjddxTAJ8zRFrpMUk0yrZ35N9-LqXBjAwgA"
Ap = "2687507"
Hs = "2401930e935bc7b124eecc028d47f320"
app = Client(S, Ap, Hs)


call_py = PyTgCalls(app)
call_py.start()
app.send_message(-1001297289773, f'**💋 Ready to sex!**')
   # print('start')



def get_youtube_stream():
    # USE THIS IF YOU WANT ASYNC WAY
    async def run_async():
        proc = await asyncio.create_subprocess_exec(
            'youtube-dl',
            '-g',
            '-f',
            # CHANGE THIS BASED ON WHAT YOU WANT
            'best[height<=?720][width<=?1280]',
            '{link}',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        return stdout.decode().split('\n')[0]
    return asyncio.get_event_loop().run_until_complete(run_async())

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
            HighQualityAudio(),
            HighQualityVideo(),
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
        otp = await app.download_media(videos)
        try:
          await call_py.leave_group_call(message.chat.id)
        except Exception:
          pass
        try:
           call_py.join_group_call(
           message.chat.id,
           AudioVideoPiped(
           otp,
           ),
           stream_type=StreamType().pulse_stream,
           )
           f.edit(f'**VIDEO STARTED ▶️**')
        expect Exception as e:
           await app.send_message(message.chat.id, f'ERROR‼️: `{e}`)
           pass
    expect Exception as e:
           await app.send_message(message.chat.id, f'Video not found!\n `{e}`)
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
          cn = await get_youtube_stream()
          await call_py.join_group_call(
          message.chat.id,
          AudioVideoPiped(cn,
            HighQualityAudio(),
            HighQualityVideo(),
          ),
          stream_type=StreamType().pulse_stream,
          )
          h.edit(F'STARTING PLAYING: `{link}` in\n **{message.chat.title}')
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
         await app.send_message(message.chat.id, f'Stoped ⏹️')
      except Exception as e:
         return

         
          
        
@call_py.on_stream_end()
    async def stream_end_handler(client: PyTgCalls, update: Update):
        await call_py.leave_group_call(update.chat_id)
        return
     #  print(f'Stream ended in {update.chat_id}', update)
idle()
