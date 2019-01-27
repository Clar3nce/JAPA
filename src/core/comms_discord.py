import discord
import asyncio
#import async

TOKEN = "NTM5MDk5OTQ2ODU1NTYzMjY1.Dy9btA.AZQP6DyHrqmWm6ndv9Yt-zrIAts"


def init_client():
    client = discord.Client()
    return client

japa_client_discord = init_client()



def isCommand(message):
    commands = ["clear","test"]
    for i in range(len(commands)):
        if message == commands[i]:
            return commands[i]
        else:
            i += 1
    return "invalid"





@japa_client_discord.event
async def clearChat(channel, length):
    async for message in japa_client_discord.logs_from(channel,limit=int(length)+3):
        await japa_client_discord.delete_message(message)








@japa_client_discord.event
async def on_message(message):
    if message.author == japa_client_discord.user:
        return
    if message.content.startswith("!cmd"):
        msg_parts = message.content.split(" ")
        command = isCommand(msg_parts[1])
        if command == "invalid":
            msg = "Invalid Command {0.author.mention}".format(message)
            await japa_client_discord.send_message(message.channel, msg)
        elif command == "clear":
            msg = "Clearing Chat {0.author.mention}".format(message)
            await japa_client_discord.send_message(message.channel, msg)
            await clearChat(message.channel,msg_parts[2])



@japa_client_discord.event
async def on_ready():
    print("logged in as")
    print(japa_client_discord.user.name)
    print(japa_client_discord.user.id)
    print("========")



japa_client_discord.run(TOKEN)
