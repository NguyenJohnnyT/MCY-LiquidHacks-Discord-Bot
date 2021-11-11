def correctedData (data):
  '''Replaces data with placeholders if indexing the key value is unavailable'''
  if not 'romanizedname' in data:
    data['romanizedname'] = '(name unavilable)'
  if not 'birthdate' in data or data['birthdate'] == '1970-01-01':
    data['birthdate'] = '(birthdate unavailable)'
  if not 'nationality' in data:
    data['nationality'] = "(nationality unavailable)"
  if not 'role' in data['extradata']:
    data['extradata']['role'] = "(role unavailable)"
  if data['wiki'] == 'starcraft': #starcraft
    data['extradata']['role'] = data['extradata']['faction']
  if data['wiki'] == 'leagueoflegends': #league of legends champions
    data['extradata']['hero'] = data['extradata']['signature']
    data['extradata']['hero2'] = data['extradata']['signature2']
    data['extradata']['hero3'] = data['extradata']['signature3']
  if not 'hero' in data['extradata']:
    data['extradata']['hero'] = '(N/A)'
  if not 'hero2' in data['extradata']:
    data['extradata']['hero2'] = '(N/A)'
  if not 'team' in data:
    data['team'] = 'no team (free agent)'
  if data['links']['twitter'] == "":
    data['links']['twitter'] = '`N/A`'
  if data['links']['facebook'] == "":
    data['links']['facebook'] = '`N/A`'
  if data['links']['youtube'] == "":
    data['links']['youtube'] = '`N/A`'
  if data['links']['reddit'] == "":
    data['links']['reddit'] = '`N/A`'
  if data['links']['vk'] == "":
    data['links']['vk'] = '`N/A`'
  if data['links']['weibo'] == "":
    data['links']['weibo'] = '`N/A`'
  return data

  