# DaBabyBot.py
'''
@re for regex patterns
@os for operating system interaction
@random for random selection functions
@discord for basic discord interaction
@dotenv for env functions
@urllib.parse, @urllib.request, @re
'''
import re
import os
import random
import discord
import urllib.parse, urllib.request, re
from discord.ext import commands
from dotenv import load_dotenv

# load onv and set token from .env file within same directory
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
patterns = "dababy"

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if re.search(patterns, message.content):
        msg = f'LES GOOOOOO {message.author.mention}'
        await message.channel.send(msg)

    if message.content.startswith('!hello'):
        msg = f'Hello {message.author.mention}'
        await message.channel.send(msg)

    # to process commands, if we don't have this the bot is stuck in this listen loop
    print(f'A user sent a message')
    await client.process_commands(message)

# need this for voice package: pip install -U discord.py[voice]
# Trying to get the bot to join vc
@client.command(pass_context = True)
async def join(ctx):
    # if the user is in a vc it'll run the command but if they're not, then it'll send a message
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else: 
        await ctx.send("Bruh moment, you aren't in a fucking vc")


# Getting the bot to leave vc
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Dababy gotta go')
    else:
        await ctx.send('Boy if you dont shut the hell up')


# Shutdowns the bot and will only shut down if call is from owner of bot
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

client.run(token)