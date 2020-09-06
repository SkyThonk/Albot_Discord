import keep_alive
import discord
from discord.ext import commands
import asyncio
import os


client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hello":
        await message.channel.send('Hello!')

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)