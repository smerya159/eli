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
    print(f"Eli is online as {client.user}")


client.run(TOKEN)