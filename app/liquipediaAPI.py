import requests

#A list of currently available wikis
wikiList = ["ageofempires", "apexlegends", "arenafps", "arenaofvalor", "artifact", "autochess", "battalion", "battlerite", "brawlstars"," callofduty", "clashroyale", "counterstrike", "criticalops", "crossfire", "dota2", "fifa", "fighters", "fortnite", "freefire", "halo", "hearthstone", "heroes", "leagueoflegends", "magic", "overwatch", "paladins", "pokemon", "pubg", "rainbowsix", "rocketleague", "runeterra", "simracing", "smash", "squadrons", "starcraft", "starcraft2", "teamfighttactics", "teamfortress", "trackmania", "underlords", "valorant", "warcraft", "wildrift", "worldofwarcraft"]

def getPlayer (wiki, player, apiKey):
  '''Uses the wiki and player of interest and returns a JSON object of the player'''
  if wiki not in wikiList: #Validates whether the wiki exists
    return 'Invalid Wiki'
  #fetch player data
  response = requests.get(f"https://api.liquipedia.net/api/v2/player?wiki={wiki}&limit=1&conditions=%5B%5Bid%3A%3A{player}%5D%5D",
    headers={'Authorization': f'Apikey {apiKey}'})
  #Obtain json content
  data = response.json()
  if len(data['result']) == 0: #if no results
    return []
  else:
    return data['result'][0] #obtain the first (zeroeth) element of the json content

def printData (data):
  '''Returns a string filled with information from the player data'''
  content = (
        f"```{data['id']}, known as {data['romanizedname']}, is a {data['wiki']} player born on {data['birthdate']} with origins from {data['nationality']}.\n"
        f"They currently play as {data['extradata']['role']} for {data['team']} and are known for their {data['extradata']['hero']} and {data['extradata']['hero2']}.```"
        f"Check them out at:\n"
        f"Liquipedia: https://liquipedia.net/{data['wiki']}/{data['pagename']}\n" 
        f"Twitter: {data['links']['twitter']}\n"
        f"Facebook: {data['links']['facebook']}\n"
        f"Youtube: {data['links']['youtube']}\n"
        f"Reddit: {data['links']['reddit']}\n"
        f"VK: {data['links']['vk']}\n"
        f"Weibo: {data['links']['weibo']}"
        )
  return content