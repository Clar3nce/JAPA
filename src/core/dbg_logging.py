import discord


japa_client_discord = discord.Client()

LOGGING = True
global LOGGING_CHANNEL 



@japa_client_discord.event
async def enable_logging(loggingChan):
    LOGGING = True
    for channel in japa_client_discord.servers:
        if channel.name == loggingChan:
            LOGGING_CHANNEL = discord.Object(id=channel.id)



@japa_client_discord.event
async def disable_logging():
    LOGGING = False
    LOGGING_CHANNEL = "logs"

@japa_client_discord.event
async def write_to_log(logMsg, error):
    if error != True:
        #error has been detected
        msg = "[ERROR] " + logMsg
        await japa_client_discord.send_message(LOGGING_CHANNEL, msg)
    else:
        msg = "[LOG] "+ logMsg
        await japa_client_discord.send_message(LOGGING_CHANNEL, msg)




    
