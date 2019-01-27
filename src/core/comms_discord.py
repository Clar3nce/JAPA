import discord
#import async

TOKEN = "NTM5MDk5OTQ2ODU1NTYzMjY1.Dy9btA.AZQP6DyHrqmWm6ndv9Yt-zrIAts"

def init_client():
    client = discord.Client()
    return client





japa_client_discord = discord.Client()


@japa_client_discord.event
async def on_message(message):
    if message.author == japa_client_discord.user:
        return
    if message.content.startswith("!cmd"):
        msg = "Received command from {0.author.mention}".format(message)
        await japa_client_discord.send_message(message.channel, msg)


@japa_client_discord.event
async def on_ready():
    print("logged in as")
    print(japa_client_discord.user.name)
    print(japa_client_discord.user.id)
    print("========")



japa_client_discord.run(TOKEN)
