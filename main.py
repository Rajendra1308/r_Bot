import discord
from discord.ext import commands



intents = discord.Intents.all()
intents.members = True
# prefixCommand syntax -> !hello -> ! makes bot know that it's being called and command is the postfix
client=commands.Bot(command_prefix='!',intents=intents)


'''
When the bot is ready for receiving commands it will execute this function
'''
@client.event
async def on_ready():
     print('Bot Ready!')   # user will not see this, it's for the implementer
     print('--------------------------')

'''
 This is what the user will type
 
 when user types !hello 
 this function is called 
'''
@client.command()
async def hello(ctx):
    await ctx.send("Hello this is r_Bot!")    


# Token is a way of linking the discord bot with our code -> Do not share it with anyone
client.run('MTEwMjgwMTA0MDU3MjY4MjMxMA.GwbmWR.ZMjhMgWjxOkoX9XXewjWDp13pEF6PuhazGdDAM')


    