import asyncio, discord, json, random, time
from datetime import datetime

data = None; text = None

data = None
with open ("config.json", "r", encoding = 'utf-8') as f:
    data = json.load(f)

text = None
with open("ad.txt", "r", encoding = 'utf-8') as t:
    text = t.read()

if not data["token"]:
    print("You have not set a token in the config.json file, if you need help finding your user token, use this tutorial: https://linuxhint.com/get-discord-token/. Cannot continue!")

if not data["channels"]:
    print("You have not set any channels for the bot to send messages in. Open config.json and add a channel's ID. Cannot continue!")

if len(text) == 0:
    print("You have not set any text for the bot to send. Cannot continue!")

client = discord.Client()

async def send():
    for item in data['channels']:

        try:
            channel = client.get_channel(int(item))
            m = await channel.send(text)
            print(f"[{datetime.fromtimestamp((time.time())).strftime('%A, %B %d, %Y, %I:%M:%S %p')}] Sent message! - {m.jump_url}")

        except: pass

@client.event
async def on_ready():
    print(f"Logged in as {client.user}.")

    while True:
        await send()
        await asyncio.sleep(10)


client.run(data["token"], bot = False)
