import requests

def getPlayer (wiki, player, apiKey):
  response = requests.get(f"https://api.liquipedia.net/api/v2/player?wiki={wiki}&limit=1&conditions=%5B%5Bid%3A%3A{player}%5D%5D",
    headers={'Authorization': f'Apikey {apiKey}'})
  data = response.json()
  if len(data['result']) == 0:
    return []
  else:
    return data['result'][0]

