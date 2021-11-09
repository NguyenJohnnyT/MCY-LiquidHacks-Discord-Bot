from discord.ext import commands
import logging
from config import read_from_env
from discord_slash import SlashCommand, SlashContext

bot_token, guild_id, _ = read_from_env()

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="")

slash = SlashCommand(bot, sync_commands=True)

bot.run(bot_token)