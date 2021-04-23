# DaBabyBot.py
'''
@os for operating system interaction
@random for random selection functions
@discord for basic discord interaction
@dotenv for env functions
@urllib.parse, @urllib.request, @re
'''
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
    
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = f'Hello {message.author.mention}'
        await message.channel.send(msg)

    if message.content.startswith('!dababy'):
        msg = f'LES GOOOOOO {message.author.mention}'
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