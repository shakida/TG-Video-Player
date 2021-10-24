import os
import sys
import asyncio
from pyrogram import Client
from pyrogram.raw import functions, types
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo

from pytgcalls import idle
S = "BQAx8V0qLC8cDQX0xp6ICAQxglOeHWznUM0mCQm9QKVevKoDXLtC5aynETMtBB-5iv1ZMAlsdqeF-gC1Qbe68XUMlknUKVfGffe4PasUI9DcX2Osf7IgLMIMQ6nXTCF8Tm3F4g_BJ9wmz-85L9g1VPDlEOHvI4ndqk-DRhqPdKSAVBZIyeUGdmxiTdpl6dz_pZYfkwKp0jQTaqQt42l-FD4rYtrjLJBU2Q4fg_-sgx0s-iFQ4lcc53MLl557PCrJAduDcp2wK3reNLkU7SXHvCEec7RxNQVhYc3BB3BX9a3TucbmYyPOtqX_9Hg8rjddxTAJ8zRFrpMUk0yrZ35N9-LqXBjAwgA"
Ap = "2687507"
Hs = "2401930e935bc7b124eecc028d47f320"
app = Client(S, Ap, Hs)


call_py = PyTgCalls(app)
if __name__ == '__main__':
    call_py.start()
    remote = 'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4'
    call_py.join_group_call(
        -1001297289773,
        AudioVideoPiped(
            remote,
            HighQualityAudio(),
            HighQualityVideo(),
            additional_ffmpeg_parameters='EVERYTHING BEFORE THE INPUT (-i) '
                                         '-atend '
                                         'EVERYTHING AFTER ALL ARGUMENTS',
        ),
        stream_type=StreamType().pulse_stream,
    )
    idle()
