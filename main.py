import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Remove any default handlers to avoid duplicate logs
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Set up clean logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                logging.info(f"Loaded cog {filename[:-3]}")
            except commands.ExtensionFailed as e:
                logging.error(f"Failed to load cog {filename[:-3]}: {e}")

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await load_cogs()
    synced = await bot.tree.sync()
    logging.info(f'Synced {len(synced)} commands')

bot.run(os.getenv('BOTTOKEN'))
