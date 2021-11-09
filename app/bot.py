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

@slash.slash(name='MCY-help',
            description="Check MCY bot commands",
            guild_ids=guild_id)
async def helpsOnTheWay(ctx: SlashContext):
  """Gives a list of commands the user can use"""
  """Add different commands here as more commands are implemented"""
  logging.info("Received slash command /MCY-help.")
  await ctx.send(content=(
    "The following commands are available: ```/MCY-help \n!hello```"
  ))
# Run the bot
bot.run(bot_token)