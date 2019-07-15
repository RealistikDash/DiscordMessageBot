details = {
    "isScript" : 0, #0 = cannot be executed, 1 = it can
    "name" : "User Credentials",
    "creator" : "Default",
    "execname" : "details", #required even if script is not executable
    "isBot" : 0, #0 = login to discord account, 1 = login to discord bot
    "email" : "email",
    "password" : "password",
    "botToken" : "" #leave empty if using a discord acc
}

channelDetails = {
    "isScript" : 0,
    "name" : "Channel Details",
    "creator" : "Default",
    "execname" : "channeldetails",
    "channelId" : 453226417782784000
}

testScript = {
    "isScript" : 1, #lets the program know if this is a readable preset
    "execname" : "test", #this name will be used if the user wants to execute the script
    "name" : "Sample Script", #name of the script
    "creator" : "RealistikDash", #script creator
    "playTimes" : 1, #how many times you want the script to play
    "globalDelay" : 1, #THe delay between when each message is sent
    "randomSend" : 1, #instead of sending the messages cronologically, it will send them randomly (1 = random, 0 = not)
    "messages" : [
        "message1",
        "message2",
		"message3"
    ], #all the messages you want to send. Each str is sent as a seperate message
}

dictList = [
    details,
    channelDetails,
    testScript
] #IMPORTANT! MAKE SURE TO PUT ALL THE DICTIONARIES IN HERE OR THE PROGRAM WILL IGNORE THEM!
