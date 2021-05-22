import discord
from discord.ext import commands
import os
import Data
import Functions

client = discord.Client()




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(Data.Admins)
    if 'nigger' in message.content or 'Nigg3r' in message.content or 'Niger' in message.content or 'n1gger' in message.content or 'nigg3r' in message.content:
        await message.author.ban()
        await message.channel.send('User Banned :/')
        

    if message.content.startswith('$'):
        Splitmessage = message.content.split(' ')

        if Splitmessage[0] == '$Admins':
            if Functions.Authenticate(message.author):
                adminlist = []
                for x in Data.Admins:
                    adminlist.append(x.name)
                    await message.author.send(adminlist)
        
        elif Splitmessage[0] == '$Logout':
            if Functions.Authenticate(message.author):
                for x in Data.Admins:
                    await x.send(str(message.author.name) + ' has logged out')
                Data.Admins.remove(message.author)

        elif Splitmessage[0] == '$Login':
            if len(Splitmessage) == 3:
                if Functions.Login(message.author,Splitmessage[1],Splitmessage[2]):
                    for x in Data.Admins:
                        await x.send(str(message.author.name) + " Has logged in")
            if len(Splitmessage) == 2:
                if Functions.Login(message.author,Splitmessage[1],'None'):
                    for x in Data.Admins:
                        await x.send(str(message.author.name) + " Has logged in")


    elif '-clear all' in message.content and message.author.permissions_in(message.channel).manage_messages:
        if message.author in Data.Admins:
            deleted = await message.channel.purge(limit=10000)
            await message.channel.send('All messages deleted.')
            

        

client.run('ODM3MTA4OTA1MTcxNjE1NzU0.YInwaw.OjC47_Fhh-Tx1q6MbD-MSamRwZ0')