import asyncio
import os
import wave

import discord
from discord.ext import voice_recv
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
            if channel.name.lower() == "study portal":
                print(f"Found voice channel: {channel.name}")

                voice_client = await channel.connect(
                    cls=voice_recv.VoiceRecvClient
                )

                print(f"Eli joined: {channel.name}")

                output_path = "data/voice_test.wav"

                audio_file = open(output_path, "wb")

                sink = voice_recv.WaveSink(audio_file)

                voice_client.listen(sink)

                print("Recording for 5 seconds...")
                print("Speak normally in Study portal.")

                await asyncio.sleep(5)

                print("Stopping recording...")

                voice_client.stop_listening()

                # Give the sink a moment to finish processing packets.
                await asyncio.sleep(0.5)

                await voice_client.disconnect()

                audio_file.close()

                print(f"Recording saved to: {output_path}")

                await client.close()
                return

    print("Study portal voice channel not found.")
    await client.close()


client.run(TOKEN)