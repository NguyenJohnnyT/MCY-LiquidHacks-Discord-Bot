from discord.ext import commands
import logging
from config import read_from_env
from discord_slash import SlashCommand, SlashContext

# Read cofig from environment variables
bot_token, guild_id, _ = read_from_env()

# Enable basic logging into console
logging.basicConfig(level=logging.INFO)

# Set up a new bot instance
bot = commands.Bot(command_prefix="")

# Bot handles slash commands
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
  """Show log message when Bot has connected to Discord"""
  logging.info("Bot is now online in Discord")

@bot.event
async def hello_message(message):
  """Reply to any hello bot message in the channel"""
  if message.author == bot.user:
    return
  if message.content == "!hello" or "!Hello":
    await message.channel.send("I am MCY bot")

# Run the bot
bot.run(bot_token)