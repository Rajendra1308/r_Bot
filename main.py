import random
import discord

from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member

'''

'''
intents = discord.Intents.all()
intents.members = True
# prefixCommand syntax -> !hello -> ! makes bot know that it's being called and command is the postfix
client = commands.Bot(command_prefix='!', intents=intents)

'''
When the bot is ready for receiving commands it will execute this function
'''
'''
IMPORTANCE OF await keyword

The await keyword in Python is used to wait for a coroutine to complete before executing the next line of code. In this specific code, the change function calls the stop and play functions using the await keyword.

If you remove the await keyword from the function calls, then the code won't wait for the functions to complete their execution before moving on to the next line. This may cause unexpected behavior or errors, especially if the functions modify some shared resource, such as a database or a file.

In short, removing the await keyword may cause the code to execute out of order and lead to unintended consequences.
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
    await ctx.send("Hello this is meee!")


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
    channel = client.get_channel(1107169359727689728)  # this is channel ID from Discord


# @client.event
# async def on_message(message:discord.Message):
#     if message.content in ["fuck", "nigga", "fucker", "motherfucker", "profanity"]:
#         await message.delete()
#         await message.channel.send("Do not use profanity words otherwise you will be kicked!")

'''
It will detect when user has left the server and print the message
'''


@client.event
async def on_member_remove(member: discord.Member):
    channel = client.get_channel(1102782529162977371)  # this is channnel ID from Discord
    await channel.send(f'Goodbye {member.name}!')


"""
    Detect Specific words
    Listen for message in voice channel
    and print the message
"""

# @client.event
# async def on_message(message):
#     if message.content == "hi":


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
    voice: discord.VoiceProtocol = discord.utils.get(client.voice_clients,
                                                     guild=ctx.guild)  # where is our bot is , what is it currently playing
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("There's no audio playing ")


'''
Resume Song
'''


@client.command(pass_context=True)
async def resume(ctx: discord.ext.commands.Context):
    voice: discord.VoiceProtocol = discord.utils.get(client.voice_clients,
                                                     guild=ctx.guild)  # where is our bot is , what is it currently playing
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("There's no audio playing ")


'''
STOP Song
'''


@client.command(pass_context=True)
async def stop(ctx: discord.ext.commands.Context):
    voice: discord.VoiceProtocol = discord.utils.get(client.voice_clients,
                                                     guild=ctx.guild)  # where is our bot is , what is it currently playing
    voice.stop()


@client.command(pass_context=True)
async def play(ctx: discord.ext.commands.Context):
    voice: discord.VoiceProtocol = ctx.guild.voice_client  # where is our bot is , what is it currently playing
    song_list = ['Future - Low Life (feat. The Weeknd).mp3', 'The Weeknd - After Hours (Audio)(1).mp3',
                 'The Weeknd - Blinding Lights.mp3',
                 'The Weeknd - I Feel It Coming ft. Daft Punk (Official Video)(1).mp3',
                 'The Weeknd - Is There Someone Else (Official Audio).mp3', 'The Weeknd - Less Than Zero.mp3',
                 'The Weeknd - Out of Time.mp3', 'The Weeknd - Pray For Me.mp3',
                 'The Weeknd - Save Your Tears (Official Audio).mp3', 'The Weeknd - Wasted Times (Official Audio).mp3',
                 'Daft Punk (feat. Julian Casablancas) - Instant Crush [Random Access Memories].mp3',
                 'Daft Punk - Digital Love (HD).mp3', 'Daft Punk - Get Lucky (Feat. Pharrell Williams).mp3',
                 'Daft Punk - Giorgio by Moroder (Official Audio).mp3',
                 'Daft Punk - Lose Yourself To Dance (Feat. Pharrell Williams).mp3',
                 'Daft Punk - One More Time [HQ].mp3', 'Daft Punk - The Game Of Love.mp3',
                 'Daft Punk - Touch (Official Audio) ft. Paul Williams.mp3', 'Daft Punk - Veridis Quo.mp3',
                 'Give Life Back to Music.mp3', 'Lil Keed - Snake snake snake snake.mp3']
    x: int = random.randint(0, len(song_list) - 1)
    source = FFmpegPCMAudio(song_list[x])
    player = voice.play(source)


@client.command(pass_context=True)
async def change(ctx: discord.ext.commands.Context):
    await stop(ctx)
    await play(ctx)


@client.command(pass_context=True)
async def leave(ctx: discord.ext.commands.Context):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in the voice channel")


'''
This function will kick the members who has the kick permissions true, meaning who can kick other people without our persmission

'''


@client.command(pass_context=True)
@has_permissions(kick_members=True)  #
async def kick(ctx: discord.ext.commands.Context, member: discord.Member, *, reason=None):
    await  member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')


'''
If a user who does not have permissions to kick people runs the above command 
'''


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have Permissions to kick people!')


@client.command(pass_context=True)
@has_permissions(ban_members=True)  #
async def ban(ctx: discord.ext.commands.Context, member: discord.Member, *, reason=None):
    await  member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned')


'''
If a user who does not have permissions to kick people runs the above command 
'''


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have Permissions to ban people!')




'''
RUN
'''
# Token is a way of linking the discord bot with our code -> Do not share it with anyone
client.run('')
