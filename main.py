import os
import sys
from pyrogram import Client, idle
from pyrogram.raw import functions, types
# pip3 install -U pytgcalls==3.0.0.dev19
# pip3 install -U git+https://github.com/pyrogram/pyrogram

import asyncio

import pytgcalls
import pyrogram

# EDIT THIS
# more info about API keys here https://docs.pyrogram.org/intro/setup#api-keys
API_ID = '6449039'
API_HASH = '709d7db09312474ff3b572c8990a2642'
SESSION = 'BQBzZwJ71UWHcXewzrVcpmYzaIsDMX5bxpPQ56IgrbPbzWYarjMvktO6OhUxImtrOilRZ_26phRjEawhdxNlgRRE_RJ2Mv_kM3QzgRuW9gdlc2FUIEOWnUjZjVs9zgAx5XNPQlHr4qGRTnipH1hB7TAqozb5p2h52tLEWB5KFsGEChqLn026PpI-hQAkvaWuPYyP4-I2PXNqXj8vYRMRg06JXfbUl7EtGgI7V2vUe10R29W-We8OhODWpoaW6FzV3JmmQteVa6jGWZ8yJpKX6uVrHln_ONRwpWbDtIekyRF2-tN4YMhZj-VifI3QKDVBl3Q1B4R1YqvDSVFNTx3Zr8vLWG45kwA'

CHAT_ID = '-1001297289773' # it can be a channel too
INPUT_SOURCE = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
# EDIT END
# client = Client(SESSION, API_ID, API_HASH)


async def main(client):
    group_call = pytgcalls.GroupCallFactory(client).get_group_call()
    await group_call.join(CHAT_ID)
    await group_call.start_video(INPUT_SOURCE)

    await pyrogram.idle()


if __name__ == '__main__':
    pyro_client = pyrogram.Client(SESSION, API_ID, API_HASH)
    pyro_client.start()

    asyncio.get_event_loop().run_until_complete(main(pyro_client))
