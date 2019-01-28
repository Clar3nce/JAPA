import discord

japa_client_discord = discord.Client()



@japa_client_discord.event
async def enable_logging(loggingChan):
    for server in japa_client_discord.servers:
        for channel in server.channels:
            if channel.name == loggingChan:
                print(channel.name)
                return channel.id

@japa_client_discord.event
async def disable_logging():
    LOGGING = False
    LOGGING_CHANNEL = "logs"

@japa_client_discord.event
async def write_to_log(logMsg, error, chan):
    print(chan)
    logs = discord.Object(id=chan)
    print(logs.id)
    if error != True:
        #error has been detected
        msg = "[ERROR] " + logMsg
        await japa_client_discord.send_message(logs.id, msg)
    else:
        msg = "[LOG] "+ logMsg
        await japa_client_discord.send_message(logs.id, msg)




    
