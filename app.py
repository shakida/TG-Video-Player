from pyrogram import Client, idle

app = Client("shakida")
app.start()
print("Started")

idle()

app.stop()
print("stoped")




