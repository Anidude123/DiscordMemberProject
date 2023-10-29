import requests

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.guilds = True  # Enable guild intents
intents.members = True  # Enable member intents

client = discord.Client(intents=intents)
#Looping through all guilds of the specific bot
@client.event
async def on_ready():
    print("Bot is ready.")
    for guild in client.guilds:
        print(f"{guild.name} - {guild.id}")
        
        members = []
        async for member in guild.fetch_members(limit=None):  # Fetch all members
            members.append(member.name)
                
        for member in guild.members:
            print(f"Member: {member.name}")
            print(f"ID: {member.id}")
            print(f"Discriminator: {member.discriminator}")
            print(f"Display Name: {member.display_name}")
            print(f"Mention: {member.mention}")
            print(f"Status: {member.status}")
            print(f"Roles: {', '.join([role.name for role in member.roles])}")
            print(f"Voice Channel: {member.voice.channel.name if member.voice else 'Not in a voice channel'}")

        print(f"Total members: {len(members)}")
        print(f"Member names in the server:\n" + '\n'.join(members))
    

client.run('YOUR_BOT_TOKEN')

