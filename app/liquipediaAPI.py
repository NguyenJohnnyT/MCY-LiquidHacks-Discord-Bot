import requests

def getPlayer (apiKey):
  response = requests.get("https://api.liquipedia.net/api/v2/player?wiki=starcraft2&order=pagename%20DESC&limit=1&conditions=%5B%5Bnationality%3A%3ASouth%20Korea%5D%5D%20AND%20%5B%5Bearnings%3A%3A%3E100000%5D%5D",
    headers={'Authorization': f'Apikey {apiKey}'})
  data = response.json()
  print(data)
  return data

