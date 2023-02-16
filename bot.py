#!/usr/bin/python3
import os

import discord

TOKEN = open('.token.txt').read().split()[0]
print(TOKEN)
intents = discord.Intents.all()
print(intents)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    m = str(message.content)

    print(f'Message {m} by {username}')

    if message.author == client.user: return

    if m.lower() in ["tjena", "hej"]:
        await message.channel.send(f'Tjenixen, {username}')
    elif m.lower() == "bye":
        await message.channel.send(f'Bye {username}')
    elif 'zoler' in m.lower():
        await message.add_reaction('🦊')

client.run(TOKEN)
