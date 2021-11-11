from discord.ext import commands
import logging
import requests
from requests.models import HTTPError
from config import read_from_env
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from liquipediaAPI import getPlayer, printData
from dataCorrection import correctedData

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
  if message.content == "!hello" or message.content == "!Hello":
    await message.channel.send("I am MCY bot")
  if message.content == "!bye":
    await message.channel.send("Good bye")

@slash.slash(
  name='MCY-help',
  description="Check MCY bot commands",
  guild_ids=guild_id
)
async def helpsOnTheWay(ctx: SlashContext):
  """Gives a list of commands the user can use"""
  """Add different commands here as more commands are implemented"""
  logging.info("Received slash command /MCY-help.")
  await ctx.send(content=(
    "The following commands are available: ```/MCY-help - Check MCY bot commands"\
    "\n/MCY-getPlayer - Enter a wiki and a player name to get a short bio about the player."\
    "\n!hello - Bot says hello!"\
    "\n!bye - Bot says bye!```"
  ))

@slash.slash(
  name='MCY-wiki',
  description="Get a list of available wikis",
  guild_ids=guild_id)
async def wikiList(ctx: SlashContext):
  """Displays a list of liquipedia wikis"""
  logging.info("Received slash command /MCY-wiki.")
  await ctx.send(content=(
    "The following wikis are available in alphabetical order.\n"\
    "```ageofempires, apexlegends, arenafps, arenaofvalor, artifact, autochess, battalion, battlerite, brawlstars, callofduty, clashroyale, counterstrike, criticalops, crossfire, dota2, fifa, fighters, fortnite, freefire, halo, hearthstone, heroes, leagueoflegends, magic, overwatch, paladins, pokemon, pubg, rainbowsix, rocketleague, runeterra, simracing, smash, squadrons, starcraft, starcraft2, teamfighttactics, teamfortress, trackmania, underlords, valorant, warcraft, wildrift, worldofwarcraft```"
  ))

@slash.slash(
  name='MCY-getPlayer',
  description="Get information about a player, leave blank for random",
  guild_ids=guild_id,
  options=[
    create_option(
      name='wiki',
      description='type !wiki for a list of available wikis',
      required=True,
      option_type=3
    ),
    create_option(
      name='player',
      description='Give a player name. Hint: Case sensitive, match their name on liquipedia page',
      required=True,
      option_type=3
    )
  ])
async def showPlayerStats(ctx: SlashContext, wiki:str, player:str, ):
  logging.info("Received slash command /MCY-getPlayer")
  try:
    await ctx.defer()
    data = getPlayer(wiki, player, apiKey)
    if len(data) != 0:
      data = correctedData(data)
      content = printData(data)
      await ctx.send(content=content)
    else:
      if player[0].isupper():
        await ctx.send(content=f'```No results found for {player}```')
      else:
        correctedPlayer = player[0].upper() + player[1:len(player)]
        await ctx.send(content=f'```No results found for {player} (have you tried {correctedPlayer}?)```')
  except HTTPError as err:
    logging.exception(f"Liuqipedia API returned an error {err.response.text}.")
    await ctx.send("Calling liquipedia API failed. See console log for details")

# Run the bot
bot.run(bot_token)