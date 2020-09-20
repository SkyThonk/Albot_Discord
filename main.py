import keep_alive
import discord
from discord.ext import commands
import asyncio
import os
import qsql


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower() == 'ping':
            await message.channel.send('pong pong')
        
        if message.channel.id == 428432032276938753 or message.channel.id == 747078225372643399:
            qsql.insert_data(message.content)
            await message.channel.send('data saved suscess')

        if message.content == 'showdata':
            await message.channel.send(str(qsql.show_data()))



client = MyClient()

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)