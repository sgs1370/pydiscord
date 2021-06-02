#!/Users/sgs/disc/bin/python3

import discord
from discord.ext import tasks
from discord.ext import commands
import os


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=60) # task runs every 60 seconds
    async def my_background_task(self):
        #channel = self.get_channel(1234567) # channel ID goes here
        channel = discord.utils.get(self.get_all_channels(),name='general')
        self.counter += 1
        await channel.send(self.counter)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in


#@client.event
#async def on_ready(): print('We have logged in as {0.user}'.format(client))

import imgkit

def check_for_new(sleeptime):
   import requests
   url = "https://api.opensea.io/api/v1/events"

   import time
   now = time.time()
   tsince = now - sleeptime
   
   querystring = {"only_opensea":"false","offset":"0","limit":"5","collection_slug":"veefriends","occurred_after":tsince,"event_type":"successful"}
   #querystring = {"only_opensea":"false","offset":"0","limit":"5","collection_slug":"bitshields","occurred_after":tsince,"event_type":"successful"}
   
   headers = {"Accept": "application/json"}
   
   response = requests.request("GET", url, headers=headers, params=querystring)
   
   import json
   json_data = json.loads(response.text)
   
   out = json.dumps(json_data,indent=2)
   print(out)
   
   if len(json_data)< 1:
       return(False, None)

   events = json_data["asset_events"]
   if len(events) < 1:
       return(False, None)
     
   hheader = "<html><p>"
   blocks = []
   return (True,events)



 

   """
   hhtml = hheader + ("<hr>\n").join(blocks) + "</html>"
   fileh = "block.%s.html" % now
   filep = "block.%s.png" % now
   fout = open(fileh, "w")
   fout.write(hhtml)
   fout.close()
   options = { "transparent" : "" }
   imgkit.from_file(fileh,filep,options=options)
   file_d = discord.File(filep,filename=filep)
   return(True, file_d)
   """


#embed.set_image(url="attachment://hello.html")

from discord.ext import tasks

@tasks.loop(seconds=45.0, count=36000)
async def sales_watcher():
    counter = 1
    import time
    if True:
        await message.channel.send('Hello!')
        first = True
        if True:
            print("about to check")
            if first:
                sleeptime = 9.0*7200.0
            else:
                sleeptime = 40.0
             
            (status,events) = check_for_new(sleeptime)
            first = False
            if status:
                #await message.channel.send(file=file)
                await message.channel.send("stuff:")
                for event in events:
                    asset = event["asset"]
                    #block = '<img src="%s"><p>%s<p>%d<p>%s<p>' % (asset["image_url"],asset["name"],int(event["total_price])/1000000000000000000.0, event["winner_account"])
                    imgsrc = asset["image_url"]
                    assetname = asset["name"]
                    cost = int(event["total_price"])/1000000000000000000.0
                    acost = f"{cost:.5f} ETH"
                    buyer = event["winner_account"]["address"]
                    seller = event["seller"]["address"]
                    block = f'<img src="{imgsrc}">\n<p>\n<h1>Name:<br>{assetname}</h1>\n<p><h1>Price:<br>{cost:.5f} ETH</h1>\n<p><h1>Address:<br>{buyer}</h1>\n<p>'
                    #blocks.append(block)
                    opensea_url = asset["permalink"]
                    collection_url = asset["collection"]["banner_image_url"]

                    embed = discord.Embed(title=f"A {assetname} Sold!" ,url=opensea_url,description="",color=0xFF5733)
                    if collection_url is not None:
                        embed.set_thumbnail(url=collection_url)

                    embed.set_image(url=imgsrc)
                    embed.add_field(name="Name",value=assetname,inline=False)
                    embed.add_field(name="Amount",value=acost,inline=False)
                    embed.add_field(name="Buyer",value=buyer,inline=False)
                    embed.add_field(name="Seller",value=seller,inline=False)
                    await message.channel.send(embed=embed)
            else:
                await message.channel.send("nostuff")
            msg = str(counter) + " " + str(time.time())
            await message.channel.send(msg)
            time.sleep(sleeptime)
            
        #await message.channel.send(file=file)

client = MyClient()
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
