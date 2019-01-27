import discord
import asyncio
#import async

TOKEN = "NTM5MDk5OTQ2ODU1NTYzMjY1.Dy9btA.AZQP6DyHrqmWm6ndv9Yt-zrIAts"

MSG_HISTORY = []



def init_client():
    client = discord.Client()
    return client
japa_client_discord = discord.Client()

def log_message(msgLog,message):
    msgLog.append(message)

@japa_client_discord.event
async def clearChat(channel):
    async for message in japa_client_discord.logs_from(channel,limit=100):
        await japa_client_discord.delete_message(message)
        print(message.content)



def isCommand(message):
    commands = ["clear","test"]
    if message == commands[0]:
        #do commands function
        response = "clear"

    elif message == commands[1]:
        response = "test"

    else:
        response = "[#]Invalid Command"

    return response






@japa_client_discord.event
async def on_message(message):
    if message.content != None:
        log_message(MSG_HISTORY,message)
    msg_parts = message.content.split(" ")
    if message.author == japa_client_discord.user:
        return
    if message.content.startswith("!cmd"):
        msg = "Received command"
        await japa_client_discord.send_message(message.channel, msg)
        msg = isCommand(msg_parts[1])
        if msg == "[#]Invalid Command":
            msg = "Invalid Command {0.author.mention}".format(message)
            await japa_client_discord.send_message(message.channel, msg)
        elif msg == "clear":
            msg = "Clearing Chat {0.author.mention}".format(message)
            await japa_client_discord.send_message(message.channel, msg)
            await clearChat(message.channel)



@japa_client_discord.event
async def on_ready():
    print("logged in as")
    print(japa_client_discord.user.name)
    print(japa_client_discord.user.id)
    print("========")



japa_client_discord.run(TOKEN)
