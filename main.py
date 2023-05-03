import random

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

import main

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

'''
COMMANDS
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

'''
EVENTS

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


'''

@client.command(pass_context=True) - This is a decorator that tells the Discord API that this function is a command that can be executed by a user. pass_context=True tells the API to pass the ctx parameter, which is a Context object, to the function. The ctx object contains information about the context in which the command was executed, such as the author of the message, the channel the message was sent in, and the server the message was sent from.

async def join(ctx: discord.ext.commands.Context): - This is the definition of the join function. It takes one parameter, ctx, which is a Context object from the Discord API. The function is marked as async, which means it can be executed asynchronously.

if ctx.author.voice: - This checks if the author of the message is currently in a voice channel.

channel = ctx.message.author.voice.channel - If the author of the message is in a voice channel, this line retrieves the voice channel object from the message and stores it in the channel variable.

await channel.connect() - This line connects the bot to the voice channel that the author of the message is currently in.

else: - If the author of the message is not in a voice channel, the code in this block is executed.

await ctx.send("You must be in a voice channel to run this command!") - This line sends a message to the channel that the command was executed in, informing the user that they need to be in a voice channel to use the join command.
'''


# When pass_context argument is set to True, it allows the command function to receive a Context object as its first parameter.
@client.command(pass_context=True)
async def join(ctx: discord.ext.commands.Context):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice: discord.VoiceClient = await channel.connect()  # a discord.VoiceClient object
        source = FFmpegPCMAudio('The Weeknd - After Hours (Audio)(1).mp3')  # name of the file we want to play
        voice.play(source)


    else:
        await ctx.send("You must be in a voice channel to run this command!")


'''
Pause Song
'''


@client.command(pass_context=True)
async def pause(ctx: discord.ext.commands.Context):
    voice: discord.VoiceProtocol = discord.utils.get(client.voice_clients,guild=ctx.guild)  # where is our bot is , what is it currently playing
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("There's no audio playing ")


'''
Resume Song
'''


@client.command(pass_context=True)
async def resume(ctx: discord.ext.commands.Context):
    voice: discord.VoiceProtocol = discord.utils.get(client.voice_clients,guild=ctx.guild)  # where is our bot is , what is it currently playing
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("There's no audio playing ")


'''
STOP Song
'''


@client.command(pass_context=True)
async def stop(ctx: discord.ext.commands.Context):
    voice: discord.VoiceProtocol = discord.utils.get(client.voice_clients,guild=ctx.guild)  # where is our bot is , what is it currently playing
    voice.stop()

@client.command(pass_context=True)
async def play(ctx: discord.ext.commands.Context):
    voice:discord.VoiceProtocol = ctx.guild.voice_client  # where is our bot is , what is it currently playing
    song_list=['Future - Low Life (feat. The Weeknd).mp3','The Weeknd - After Hours (Audio)(1).mp3','The Weeknd - Blinding Lights.mp3','The Weeknd - I Feel It Coming ft. Daft Punk (Official Video)(1).mp3','The Weeknd - Is There Someone Else (Official Audio).mp3','The Weeknd - Less Than Zero.mp3','The Weeknd - Out of Time.mp3','The Weeknd - Pray For Me.mp3','The Weeknd - Save Your Tears (Official Audio).mp3','The Weeknd - Wasted Times (Official Audio).mp3']
    x:int=random.randint(0,len(song_list)-1)
    source=FFmpegPCMAudio(song_list[x])
    player=voice.play(source)

@client.command(pass_context=True)
async def change(ctx: discord.ext.commands.Context):
     stop(ctx)
     play(ctx)



@client.command(pass_context=True)
async def leave(ctx: discord.ext.commands.Context):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in the voice channel")



'''
RUN
'''
# Token is a way of linking the discord bot with our code -> Do not share it with anyone
client.run('MTEwMjgwMTA0MDU3MjY4MjMxMA.GwbmWR.ZMjhMgWjxOkoX9XXewjWDp13pEF6PuhazGdDAM')
