import logging
import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

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

bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents, help_command=None, allowed_mentions=discord.AllowedMentions.none())

async def load_cogs():
    # Change the current working directory to where the script is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Build the path to the 'cogs' directory using os.path.join for cross-platform compatibility
    cogs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cogs')

    # List all files in the 'cogs' directory
    for filename in os.listdir(cogs_dir):
        # Check if the file ends with '.py' and avoid the script itself
        if filename.endswith('.py') and filename != '__init__.py':
            cog_name = filename[:-3]  # Remove '.py' extension
            try:
                # Load the cog using the correct module path
                await bot.load_extension(f'cogs.{cog_name}')
                logging.info(f"Loaded cog {cog_name}")
            except commands.ExtensionNotFound as e:
                logging.error(f"Failed to load cog {cog_name}: {e}")
            except commands.ExtensionFailed as e:
                logging.error(f"Failed to load cog {cog_name}: {e}")


@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await load_cogs()
    synced = await bot.tree.sync()
    logging.info(f'Synced {len(synced)} commands')

bot.run(os.getenv('BOTTOKEN'))
