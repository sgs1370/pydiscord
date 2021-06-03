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

    def check_for_new(self, sleeptime):
        import requests
        url = "https://api.opensea.io/api/v1/events"
     
        import time
        now = time.time()
        tsince = now - sleeptime
        
        querystring = {"only_opensea":"false","offset":"0","limit":"20","collection_slug":"veefriends","occurred_after":tsince,"event_type":"successful"}
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
          
        return (True,events)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=60) # task runs every 60 seconds
    async def my_background_task(self):
        import time
        seconds=60.0 * 1.2
        #channel = self.get_channel(1234567) # channel ID goes here
        channel = discord.utils.get(self.get_all_channels(),name='general')
        self.counter += 1
        await channel.send(self.counter)
        if self.counter == 1:
            (status, events) = self.check_for_new(7200.0 * 5.0)
        else:
            (status, events) = self.check_for_new(seconds)
        if status:
            await channel.send("stuff:")
            for event in events:
                asset = event["asset"]
                imgsrc = asset["image_url"]
                assetname = asset["name"]
                cost = int(event["total_price"])/1000000000000000000.0
                acost = f"{cost:.5f} ETH"
                buyer = event["winner_account"]["address"]
                seller = event["seller"]["address"]
                opensea_url = asset["permalink"]
                collection_url = asset["collection"]["banner_image_url"]
                eventdate = event["transaction"]["timestamp"]

                embed = discord.Embed(title=f"A {assetname} Sold!" ,url=opensea_url,description="",color=0xFF5733)
                if collection_url is not None:
                    embed.set_thumbnail(url=collection_url)
    
                embed.set_image(url=imgsrc)
                embed.add_field(name="Name",value=assetname,inline=False)
                embed.add_field(name="Amount",value=acost,inline=False)
                embed.add_field(name="Buyer",value=buyer,inline=False)
                embed.add_field(name="Seller",value=seller,inline=False)
                embed.set_footer(text=f"Sold At {eventdate}")
                await channel.send(embed=embed)
        else:
            await channel.send("nostuff")
        msg = str(self.counter) + " " + str(time.time())
        await channel.send(msg)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in

import imgkit



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
