# simple_client.py

# This only works for discord bots btw, so yeah

import os
import random
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') # you could just define your token here, and remove line 9 if you want

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await messenger()

async def messenger():
    things = ['what say: ', 'message: ', 'what to say: ']
    channel = client.get_channel(715095207602946121)
    await client.wait_until_ready()
    while True:
        message = input(f'Channel: {channel}\n---------------\n' + random.choice(things))
        await asyncio.sleep(1)
        if len(message) > 1:
            await channel.send(message)

client.run(TOKEN)

