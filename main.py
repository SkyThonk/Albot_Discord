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

        if message.content.lower() == '$ping':
            await message.channel.send('pong pong')
        
        if message.content.lower() == '$saveid':
            if qsql.search_game_id(message.author.id) == None:
                qsql.insert_game_id(message.author.id)
                emd = discord.Embed(title="Game ID",description = "Record created Suscessfully!!\nUse the following commands to save your game ids", color = 0x00ff00)
                emd.add_field(name = "Valorant", value="$valorant {Id here}",inline = False)
                emd.add_field(name = "Rockstar", value="$rockstar {Id here}",inline = False)
                emd.add_field(name = "Epic Games", value="$epic {Id here}",inline = False)
                emd.add_field(name = "Steam", value="$steam {Id here}",inline = False)
                await message.channel.send(embed = emd)
            else:
                 await message.channel.send("Your record has been already created!!")
            
        if message.content.lower() == '$showid':
            await message.channel.send(str(qsql.search_game_id(message.author.id)))
        
        if message.content.lower().split()[0] == '$valorant':
            if qsql.search_game_id(message.author.id) != None:
                qsql.update_valo(message.content.split()[1],message.author.id)
                await message.channel.send("Saved suscessfully!!")
            else:
                await message.channel.send("You did not created record first create record and try again!!")


        
        if message.content.lower() == '$deleteid':
            qsql.dele()


client = MyClient()

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)