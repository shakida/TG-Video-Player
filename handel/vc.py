from pyrogram import Client, idle

app = Client(Op)
app.start()
print("Started")


idle()

app.stop()
print("stoped")
