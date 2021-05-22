#!/Users/sgs/disc/bin/python3

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODQ1MDI5ODQ0OTY5NDU1NjQ4.YKbBXg.O3ztMqv4BzjJ3XVztYXziyGbpMI')

# url is https://discord.com/api/oauth2/authorize?client_id=845029844969455648&permissions=0&scope=bot
# 
