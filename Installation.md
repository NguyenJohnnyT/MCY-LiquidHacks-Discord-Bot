![Header](./README_assets/header.jpeg)

<a id='installation'></a>
# Installation
Installation steps are largely accredited and referenced to [Marvin's Discord Bot tutorial](https://github.com/simachri/discord-bot-techlearn-sapcloud/blob/master/Project_Setup.md#prepare_discord_bot_appl)

## Table of contents
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Required tokens and setup](#tokens)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Prepare your Discord Bot](#bot-prepare)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Get your guild-ID](#guild-ID)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Local Deployment](#local-deploy)\
<img width='15px' height='15px' src='./README_assets/bluebullet.png'/>  [Deploy on SAP Cloud](#SAP-cloud)

<a id='tokens'></a>

## Required tokens and setup

Required private tokens/codes (Will be covered later):
1. Your discord bot token -- [See here](#bot-token)
1. Your guild/server ID -- [See here](#guild-ID)
1. Your liquipedia APIkey -- Contact liquipedia admins at _contact at liquipedia dot net_ to obtain an APIkey.

Some files of interest here are the `.EXAMPLE` files within the root folder.  Be sure to remove the `.EXAMPLE` suffix for your tests and deployments.
1. `.env.EXAMPLE`: No need to change anything
1. `.env.dev.EXAMPLE`: Fill out the parameters `BOT_TOKEN`, `GUILD_ID`, and your liquipedia `API_KEY`
1. `.manifest.yml.EXAMPLE`: Fill out the `BOT_TOKEN` and `API_KEY_`

#
<a id='bot-prepare'></a>

## Prepare your Discord Bot
1.  If you do not have a Discord server (Discord calls this a _guild_), create one
1. Go to https://discord.com/developers/applications to create a new Discord _application_.
1. Go to menu item _Bot_ and add a _bot_ to the application.
1. Go to _OAuth2_ and select the following:
    1. In _Scopes_:
        - `applications.commands`
        - `bot`
    1. In _Bot Permissions_:
        - `Send Messages`
        - `Use Slash Commands`
    1. Copy the URL and open it in the browser to authorize the bot to be used in the Discord Server
1. Check your server to see if the bot is there.  It should be offline but also in the list of users there.
<a id='bot-token'></a>
1. Get your `BOT_TOKEN`: Go back to menu item _Bot_ and press the `copy` button in the _TOKEN_ section.  Do not share this token with anyone else.

<a href='#installation'>back to top</a>
#
<a id='guild-ID'></a>

## Obtaining your guild ID (aka server ID)

The easiest way is to sign into your discord server on the [webapp](https://www.discord.com).  Click on a server you wish to obtain the guild ID from.  In the URL, you will see a discord URL and two sets of numbers:
```
discord.com/channels/<THIS NUMBER>/<another number>
```
`<THIS NUMBER>` is your guild number.

Another way to obtain your guild ID through the desktop app is to go to your `User Settings > Advanced > enable Developer Mode`. Then right click on your server name or icon and press `Copy ID`.

<a href='#installation'>back to top</a>
#
<a id='local-deploy'></a>

## Local development

Installations required:

1. [Python 3.9](https://www.python.org/downloads/)
1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
1. [cf7 CLI if using SAP BTP Cloud Foundry](https://github.com/cloudfoundry/cli/blob/master/doc/installation-instructions/installation-instructions-v7.md#installers-and-compressed-binaries) to deploy to the cloud, otherwise skip if using another product
1. _Clone_ this repository to your local device.
1. Create a `.venv` folder at the root folder
1. Make sure to provide the _BOT_TOKEN_, _GUILD_ID_, and _API_KEY_ in the `.env.dev` file.  [See here](#tokens)
1. Open a terminal and navigate to the root folder of the project.  Run 
```python
pip install pipenv #manages dependencies of the bot
pipenv install #installs all dependencies
```

Finally, verify that everything works by running
```python
python app/bot.py --env-file .env.dev 
```
If you have VSCode, you can simply press `f5` to run the app.  Alternatively, click the `Run and Debug` button on the left hand side and press the `Play` button.

<a href='#installation'>back to top</a>
#
<a id='SAP-cloud'></a>
## Deploying to SAP Cloud
Refer to [this](https://github.com/simachri/discord-bot-techlearn-sapcloud/blob/master/Project_Setup.md#deployment_cf) to deploy to the SAP cloud. If you have SAP Business Application Studio and wish to develop the code on it, be sure to reference [this](https://github.com/simachri/discord-bot-techlearn-sapcloud/blob/master/Project_Setup.md#proj_setup_bas) right above afore mentioned link.

<a href='#installation'>back to top</a>