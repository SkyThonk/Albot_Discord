import keep_alive
import discord
from discord.ext import commands
import asyncio
import os
import qsql
import validity_check

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
            
        if message.content.lower().split()[0] == '$valorant':
            if len(message.content.lower().split()) == 2 or len(message.content.lower().split()) == 3:
                if qsql.search_game_id(message.author.id) != None:
                    if len(message.content.lower().split()) == 2:
                        if validity_check.valo_validity_check(message.content.split()[1]):
                            qsql.update_valo(message.content.split()[1],message.author.id)
                            await message.channel.send("Saved suscessfully!!")
                        else:
                            await message.channel.send("Looks like that's not a valid ID! Please try again!")
                    else:
                        if validity_check.valo_validity_check(message.content.split()[1] + message.content.split()[2]):
                            qsql.update_valo(message.content.split()[1] + ' ' + message.content.split()[2],message.author.id)
                            await message.channel.send("Saved suscessfully!!")
                        else:
                            await message.channel.send("Looks like that's not a valid ID! Please try again!")
                else:
                    await message.channel.send("You did not created record first create record and try again!!")
            else:
                await message.channel.send("Invalid Parameter!!")

        if message.content.lower().split()[0] == '$rockstar':
            if len(message.content.lower().split()) == 2:
                if qsql.search_game_id(message.author.id) != None:
                    if validity_check.ID_validity_check(message.content.split()[1]):
                        qsql.update_rockstar(message.content.split()[1],message.author.id)
                        await message.channel.send("Saved suscessfully!!")
                    else:
                        await message.channel.send("Looks like that's not a valid ID! Please try again!")
                else:
                    await message.channel.send("You did not created record first create record and try again!!")
            else:
                await message.channel.send("Invalid Parameter!!")

        if message.content.lower().split()[0] == '$epic':
            if len(message.content.lower().split()) == 2:
                if qsql.search_game_id(message.author.id) != None:
                    if validity_check.ID_validity_check(message.content.split()[1]):
                        qsql.update_epic(message.content.split()[1],message.author.id)
                        await message.channel.send("Saved suscessfully!!")
                    else:
                        await message.channel.send("Looks like that's not a valid ID! Please try again!")
                else:
                    await message.channel.send("You did not created record first create record and try again!!")
            else:
                await message.channel.send("Invalid Parameter!!")
            
        
        if message.content.lower().split()[0] == '$steam':
            if len(message.content.lower().split()) == 2:
                if qsql.search_game_id(message.author.id) != None:
                    if validity_check.ID_validity_check(message.content.split()[1]):
                        qsql.update_steam(message.content.split()[1],message.author.id)
                        await message.channel.send("Saved suscessfully!!")
                    else:
                        await message.channel.send("Looks like that's not a valid ID! Please try again!")
                else:
                    await message.channel.send("You did not created record first create record and try again!!")
            else:
                await message.channel.send("Invalid Parameter!!")

        if message.content.lower().split()[0] == '$showid':
            if len(message.content.lower().split()) == 1:
               data = qsql.search_game_id(message.author.id)
               if data != None:
                   emd = discord.Embed(title=message.author.name,description = data[5], color = 0x00ff00)
                   emd.add_field(name = "Valorant", value=data[1],inline = False)
                   emd.add_field(name = "Rockstar", value=data[2],inline = False)
                   emd.add_field(name = "Epic Games", value=data[3],inline = False)
                   emd.add_field(name = "Steam", value=data[4],inline = False)
                   await message.channel.send(embed = emd)
               else:
                    await message.channel.send("No Record Found!!")

            elif len(message.content.lower().split()) == 2:
                data = qsql.search_game_id(message.mentions[0].id)
                if data != None:
                    emd = discord.Embed(title=message.mentions[0].name,description = data[5], color = 0x00ff00)
                    emd.add_field(name = "Valorant", value=data[1],inline = False)
                    emd.add_field(name = "Rockstar", value=data[2],inline = False)
                    emd.add_field(name = "Epic Games", value=data[3],inline = False)
                    emd.add_field(name = "Steam", value=data[4],inline = False)
                    await message.channel.send(embed = emd)
                else:
                    await message.channel.send("No Record Found!!")
            else:
                await message.channel.send("Invalid Parameter!!")
        
        if message.content.lower() == '$deleteid':
            qsql.dele()

        if message.content.lower().split()[0] == '$quote':
            if len(message.content.split()) == 1:
                await message.channel.send("Invalid Parameter!!")
            else:
                if qsql.search_game_id(message.author.id) != None:
                    li = message.content.split()
                    li = ' '.join(li[1:])
                    qsql.update_quote(li,message.author.id)
                    await message.channel.send("Saved suscessfully!!")
                else:
                    await message.channel.send("You did not created record first create record and try again!!")
client = MyClient()

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)