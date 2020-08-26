import keep_alive
import discord
from discord.ext import commands
import asyncio
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower() == 'ping':
            await message.channel.send('pong pong')


client = MyClient()

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)