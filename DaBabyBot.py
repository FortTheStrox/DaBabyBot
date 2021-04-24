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

# Shutdowns the bot and will only shut down if call is from owner of bot
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

client.run(token)