import discord
import asyncio
from xml_parser import CONFIG
from xml_parser import load_Default_Config
from dbg_logging import write_to_log
from dbg_logging import enable_logging


#import async

DEFAULT_CONFIG_PATH = "../configuration/config.xml"
LOGGING_CHANNEL = 0
LOGGING = False

cfg = load_Default_Config(DEFAULT_CONFIG_PATH)


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
    global LOGGING
    global LOGGING_CHANNEL
    #message.author is the same as bot username -> ignore my own messages
    if message.author == japa_client_discord.user:
        return
    #message starts with the command Identifier and is of the <cmd> command set
    if message.content.startswith(cfg.command_identifier+"cmd"):
        #split the message on ' ' to create an array of params
        msg_parts = message.content.split(" ")
        #check if the string following command identifier is a valid command 
        command = isCommand(msg_parts[1])

        #not valid command
        if command == "invalid":
            #check is verbose loggin is enabled
            if LOGGING == True:
                #write to log
                await write_to_log("Invalid Command Entered",False,LOGGING_CHANNEL)
        #valid command found 
        elif command == "clear":
            if LOGGING == True:
                #write to log
                await write_to_log("Clearing Chat", False,LOGGING_CHANNEL)
            #execute command function
            if len(msg_parts) >2:
                await clearChat(message.channel,msg_parts[2])
            else:
                await clearChat(message.channel,10)



    #check to see if the message starts with the command identifier and is part of the <debug/logging> command set
    elif message.content.startswith(cfg.command_identifier+"logging"):
        #split message into array on ' '
        msg_parts = message.content.split(" ")
        #extract the value that determines if LOGGING = True OR LOGGING = False
        logging_status = msg_parts[1]
        #LOGGING = True
        if logging_status == "enable":
            if len(msg_parts) > 2:
                LOGGING = True
                #enable logging and set LOGGING_CHANNEL
#                print(msg_parts[2])
                LOGGING_CHANNEL = await enable_logging(msg_parts[2])
                await japa_client_discord.send_message(message.channel, "Enabled Logging")
            else:
                LOGGING_CHANNEL = "logs"
                await japa_client_discord.send_message(message.channel, "Enabled Logging")
        elif logging_status == "disable":
            LOGGING = False
            await japa_client_discord.send_message(message.channel, "Enabled Disabled")




@japa_client_discord.event
async def on_ready():
    print("logged in as")
    print(japa_client_discord.user.name)
    print(japa_client_discord.user.id)
    print("========")



japa_client_discord.run(cfg.remote_interface_token)
