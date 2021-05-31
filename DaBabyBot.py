# DaBabyBot.py
'''
@re for regex patterns
@os for operating system interaction
@time for sleep
@discord for basic discord interaction
@dotenv for env functions
@random for choosing dababy audio
'''
import re
import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

# load onv and set token from .env file within same directory
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

'''
Pattern[0]
Pattern for different variations of the dababy word usage.
Use case:
dababy                          Matches: dababy
dababies                        Matches: dababies
s;adklfj; dababydasf;j          Matches: dababydasf
dsafafsdababababadbyadsfdsaf    Matches: dababababadbyadsf
asdfdsafdaboobyadsfasdf         Matches: daboobyadsf

Pattern[1]
For being a car I guess
'''
patterns = ["[dD][aA][bB]\w+[bB]\w{0,5}", "car"]

'''
Hands up emoji
'''

emoji = ["<:handsup:519312367570386962>"]

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if re.search(patterns[0], message.content):
        msg = f'LES GOOOOOO {message.author.mention}'
        await message.channel.send(msg)
        

    if re.search(patterns[1], message.content):
        msg = f'{emoji[0] * 4}I will turn a {message.author.mention} into a convertible{emoji[0] * 4}'
        await message.channel.send(msg)

    if message.content.startswith('!hello'):
        msg = f'Hello {message.author.mention}'
        await message.channel.send(msg)

    # to process commands, if we don't have this the bot is stuck in this listen loop
    print(f'A user sent a message')
    await client.process_commands(message)

@client.command(pass_context = True)
async def idolVoice(ctx):
    
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source=f"audio/dababy{random.randint(1,5)}.m4a", executable="A:/Downloads/ffmpeg-N-102631-gbaf5cc5b7a-win64-gpl/bin/ffmpeg.exe"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
    # Delete command after the audio is done playing.
    await ctx.message.delete()

# Getting the bot to leave vc
@client.command(pass_context = True)
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice is None:
        if voice.is_connected():
            await ctx.send('Dababy gotta go')
            await voice.disconnect()
        else:
            # no channel to leave
            await ctx.send('Boy if you dont shut the hell up')
    else:
        # no channel to leave
        await ctx.send('Boy if you dont shut the hell up')


# Shutdowns the bot and will only shut down if call is from owner of bot
@client.command()
async def shutdown(ctx):
    await client.close()

client.run(token)