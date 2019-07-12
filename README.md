# DiscordMessageBot
Send or spam Discord messages with an easy to use Python based script tool.

# What it does

This tool lets you program your own sets of messages however you want them.

Want to spam a channel? Want to send a copypasta? Want to easily distribute your message scripts with your mates? 

With this you easily can?

# What it does so far

-Send individual messages without scripts

-Send scripted messages

-Easy distribution and addition of scripts

# How to make a message script?

Your scripts will be located in the userdata.py file as dictionaries. To add one, paste it above the last line (make sure it's not below) and add it to the dictList list (last line).

So how do you make your own one?

```python
scriptTemplate = {
    "isScript" : 1, 
    "execname" : "", 
    "name" : "", 
    "creator" : "",
    "globalDelay" : 0,
    "playTimes" : 1,
    "messages" : [
        "message1",
        "message2"
    ],
}
```

Above is a blank version of a script. Here is a table that explains what everything does:

| Value  | Explanation |
| ------------- | ------------- |
| isScipt  | Decides whether the script can be ran with /exec (1= yes, 0=no)  |
| execname  | What name to use to run the scipt via /exec  |
| name | The name of the script |
| creator | The name of the creator |
| globalDelay | The delay between performing an action by the script |
| playTimes | How many times the script will repeat |
| messages | A list of messages that will be sent cronologically |

When you're done, make sure you don't forget to add the dict to the dictList list. It should look something like this after you've added it:

```python
dictList = [
    details,
    channelDetails,
    testScript,
    scriptTemplate
]
```

# What is planned

I plan to add:

-Custom delays in a script

-Custom prompts in a script
