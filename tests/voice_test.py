import os

import discord
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set.")


intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    for guild in client.guilds:
        for channel in guild.voice_channels:
            if channel.members:
                print(f"Found user in voice channel: {channel.name}")

                await channel.connect()
                print(f"Eli joined: {channel.name}")

                return

    print("No users found in a voice channel.")


client.run(TOKEN)