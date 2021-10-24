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
idle()
   # print('start')


@app.on_message(filters.command(["livex"]) & filters.chat(875645659))
async def live(app, message: Message):
 try:
    if len(message) < 2:
        return
    query = message.text.split(None, 1)[1]
    remote = query
    try:
        await call_py.join_group_call(
        -1001297289773,
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
    except Exception as e:
        print(e)
        pass
    try:
        await call_py.join_group_call(
        -1001602466526,
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
        await app.send_message(875645659, f'Starting `{remote}`..')
    except Exception as e:
        print(e)
        pass
    
 except Exception as e:
    await app.send_message(875645659, f'ERROR ‼️ `{e}`')
