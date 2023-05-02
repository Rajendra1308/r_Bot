import discord
from discord.ext import commands

'''

'''
intents = discord.Intents.all()
intents.members = True
# prefixCommand syntax -> !hello -> ! makes bot know that it's being called and command is the postfix
client = commands.Bot(command_prefix='!', intents=intents)

'''
When the bot is ready for receiving commands it will execute this function
'''


@client.event
async def on_ready():
    print('Bot Ready!')  # user will not see this, it's for the implementer
    print('--------------------------')


'''
 This is what the user will type
 
 when user types !hello 
 this function is called 
'''


@client.command()
async def hello(ctx):
    await ctx.send("Hello this is r_Bot!")


@client.command()
async def goodbye(ctx):
    await ctx.send("See You! Hope You have a Good Day.")


'''
It will detect when user has joined the server and print the message
'''


@client.event
async def on_member_join(member: discord.Member):
    channel = client.get_channel(1102782529162977372)  # this is channel ID from Discord


'''
It will detect when user has left the server and print the message
'''


@client.event
async def on_member_remove(member: discord.Member):
    channel = client.get_channel(1102782529162977372)  # this is channnel ID from Discord
    await channel.send(f'Goodbye {member.name}!')


@client.command(pass_context=True)
async def join(ctx: discord.ext.commands.Context):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You must be in a voice channel to run this command!")


'''

'''


@client.command(pass_context=True)
async def leave(ctx: discord.ext.commands.Context):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect(force=True)
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in the voice channel")


# Token is a way of linking the discord bot with our code -> Do not share it with anyone
client.run('MTEwMjgwMTA0MDU3MjY4MjMxMA.GwbmWR.ZMjhMgWjxOkoX9XXewjWDp13pEF6PuhazGdDAM')
