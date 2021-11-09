from discord.ext import commands
import logging
import requests
from requests.models import HTTPError
from config import read_from_env
from discord_slash import SlashCommand, SlashContext
from liquipediaAPI import getPlayer

# Read cofig from environment variables
bot_token, guild_id, _, apiKey = read_from_env()
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
async def on_message(message):
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

@slash.slash(name='MCY-getPlayer',
            description="Get information about a player",
            guild_ids=guild_id,)
async def getRandomPlayer(ctx: SlashContext):
  logging.info("Received slash command /MCY-getPlayer")
  try:
    await ctx.defer()
    data = getPlayer(apiKey = apiKey)
    if len(data['result']) != 0:
      await ctx.send(content=(f"```{data['result'][0]}```"))
    else:
      await ctx.send(content='No results found')
  except HTTPError as err:
    logging.exception(f"Liuqipedia API returned an error {err.response.text}.")
    await ctx.send("Calling liquipedia API failed. See console log for details")

# Run the bot
bot.run(bot_token)