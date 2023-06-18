import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests

intents = discord.Intents.default()
intents.members = True
intents.messages = True  # Enable the 'messages' intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"ปลากะพงฮับ | {bot.user.name}"))

load_dotenv()
token = os.getenv("TOKEN")
bot.run(token)
