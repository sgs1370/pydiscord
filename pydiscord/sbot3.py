#!/Users/sgs/disc/bin/python3

import discord
from discord.ext import tasks
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(seconds = 2.0,count=3) 
async def myLoop(counter=0):
    counter += 1
    print('Hey %d' % counter)
    await message.channel.send('Hey %d' % counter)

myLoop.start()

import imgkit
imgkit.from_file('hello.html','hello.png')

#file = discord.File("hello.html",filename="hello.html")
file = discord.File("hello.png",filename="hello.png")
#embed = discord.Embed()
#embed.set_image(url="attachment://hello.html")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        #await message.channel.send('Hello!')
        await message.channel.send(file=file)
        

client.run(os.environ['BOTTOKEN'])


"""

   52  python -m pip install imgkit
   53  python3 -m pip install imgkit
   54  vi karl.py 
   55  ./karl.py 
   56  vi karl.py 
   57  cd ~
   58  source disc/bin/activate
   59  cd -
   60  python3 -m pip install imgkit
   61  python
   62  ./karl.py 
   63  python3 -m pip install wkhtmltopdf

"""
