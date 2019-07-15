import discord
import asyncio
import time
import random

print("Loading userdata...")
from userdata import *

print("Starting Discord Message Bot...\n")

print("Loading modules...\n")

for x in dictList:
    print("{} by {} loaded successfully!".format(x["name"], x["creator"]))

print("\n")

bot = discord.Client()

bot.dictlist = dictList
bot.channelDeatils = channelDetails


@bot.event
async def on_ready():
    print("Successfully connected to {}!\n".format(bot.user.name))
    print("Welcome to the console!\nThis is where you control all of this!\nHere are some helpful commands:\n/exec <script>     Executes a script\n/send <message>      Send a normal message without a script\n/exit            Logs off and exits the program.\n")
    channelId = discord.Object(id=channelDetails["channelId"])
    while True:
        command = input(">")
        if command.startswith("/exec"):
            #execute command
            scrToExec = command[6:]
            for x in bot.dictlist:
                if x["execname"] == scrToExec:
                    currentscript = x
            
            if currentscript["isScript"] == 1:
                #exec script
                print("You chose:")
                print("{} by {}\n".format(currentscript["name"], currentscript["creator"]))
                print("Are you sure you want to execute it? (y/N)")
                execQuestion = input(">")
                execQuestion = execQuestion.lower()
                if execQuestion == "y":
                    #send script
                    replayTimes = currentscript["playTimes"]
                    messagesSent = 0
                    messagesFailed = 0
                    messagesAttempted = 0
                    while replayTimes > 0:
                        for str in currentscript["messages"]:
                            messagesAttempted = messagesAttempted + 1
                            if currentscript["randomSend"] == 1:
                                str = random.choice(currentscript["messages"])
                            try:
                                await bot.send_message(channelId, str)
                                messagesSent = messagesSent + 1
                                print("Message number {} sent successfully!".format(messagesAttempted))
                            
                            except Exception as e:
                                messagesFailed = messagesFailed + 1
                                print("Message number {} failed! Error: {}".format(messagesAttempted, e))
                            
                            replayTimes = replayTimes - 1

                            await asyncio.sleep(currentscript["globalDelay"])

                    print("Script {} finished!".format(currentscript["name"]))
                    print("Result:\nMessages attempted: {}\nMessages sent: {}\nMessages failed: {}".format(messagesAttempted, messagesSent, messagesFailed))

                else:
                    print("Okay. Aborting...\n")
                    asyncio.sleep(1)
            
            else:
                print("Script not executable!")
                asyncio.sleep(1)
        
        elif command == "/exit":
            bot.close()
            exit()
        
        elif command.startswith("/send"):
            msgToSend = command[6:]
            try:
                await bot.send_message(channelId, msgToSend)
                print("Sending message 1 succeded!")
            except Exception as e1:
                print("Sending message 1 failed! Error:", e1)
        
        else:
            print("Command", command, "does not exist!\n")
        
    




if details["isBot"] == 0:
    try:
        bot.run(details["email"], details["password"])
    except Exception:
        print("Failed to connect to Discord!")
        print("Closing in 5 seconds...")
        time.sleep(5)
        exit()

elif details["isBot"] == 1:
    try:
        bot.run(details["botToken"])
    except Exception:
        print("Failed to connect to Discord!")
        print("Closing in 5 seconds...")
        time.sleep(5)
        exit()
