[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Header](./README_assets/header.jpeg)
# MCY LiquidHacks 2.0 Discord Bot

A discord bot that utilizes the Liquipedia API for submission into the Team Liquid Hackathon 2.0.

### [Demo video](#)

## Test the bot
[Discord invite link](https://discord.gg/bFKMDR64Sp) (Temporary membership--You will be automatically kicked once disconnected, but this invite link does not expire.)
#

## Table of Contents
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [What is it](#Description)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Why make it](#Why)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Drawbacks and future improvements](#Drawbacks)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Installation](#Installation)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Special Thanks](#Thanks)

<a id='Description'></a>
## What is it? (Usage)
The MCY-bot is a Discord bot that queries the Liquipedia API and returns information about a user-requested player from a specific wiki.  The bot uses the `discord-py-slash-command` module which allows users to use the bot via slash commands such as `/MCY-help` or `/MCY-getplayer`.

Current available commands:
```
/MCY-help
/MCY-wiki
/MCY-getplayer <wiki> <player>
```
<a id='Why'></a>
## Why make it?
I have never successfully created and deployed a Discord bot and LiquidHacks 2.0 provided an excellent opportunity to explore and learn some new skills.

While googling a player on liquipedia is likely to be very quick, being able to do a quick slash command and displaying in the channel a player's short bio and socials may be helpful in a community setting.

<a id='Drawbacks'></a>
## Drawbacks // Future improvements
* The bot is optimized mostly for _League of Legends_, _Dota2_, and _Brood War_ queries, so querying other wikis will likely make strange contextual mistakes.
* Make it easier for the user to search for players.  It requires the user to be very exact with the player's liquipedia page name.
* Add randomizer
* Remove embeds as the bot response can be very bulky
* Add a cooldown to reduce frequency of API querying

<a id='Installation'></a>
## [Installation](Installation.md#)

1. [Obtain your tokens](Installation.md#tokens)
1. [Prepare your Discord Bot](Installation.md#bot-prepare)
1. [Local installation](Installation.md#local-deploy)
1. [Deploying to SAP cloud](Installation.md#SAP-cloud)

<a id='Thanks'></a>
## Special Thanks
[Martin](https://github.com/simachri) -- for his talk on creating and deploying a discord bot, and also an SAP BTP trial account\
[Discord bot tutorial](https://github.com/simachri/discord-bot-techlearn-sapcloud/blob/master/Project_Setup.md#deployment_cf) -- Martin's repository.  Referenced and borrowed some code here for `app.config.py` and `app.bot.py`\
[LiquidHacks 2.0](https://liquidhacks.teamliquid.com/) Team Liquid's Hackathon event\
[Liquipedia](https://www.liquipedia.net) The best website for esports information!\
[Liquipedia API](https://api.liquipedia.net) \
[SAP Business Technology Platform](https://www.sap.com/products/business-technology-platform.html)\
[Discord Slash Commands](https://discord-py-slash-command.readthedocs.io/en/latest/index.html) Module documentation used for slash commands\
[Discord Developers Documentation](https://discord.com/developers/docs/intro) Documentation on Discord API