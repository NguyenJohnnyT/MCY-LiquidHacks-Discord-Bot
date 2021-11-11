def correctedData (data):
  '''Replaces data with placeholders if indexing the key value  is unavailable'''
  if not 'romanizedname' in data:
    data['romanizedname'] = '(name unavilable)'
  if not data['birthdate'] or data['birthdate'] == '1970-01-01':
    data['birthdate'] = '(birthdate unavailable)'
  if not data['nationality']:
    data['nationality'] = "(nationality unavailable)"
  if not 'role' in data['extradata']:
    data['extradata']['role'] = "(role unavailable)"
  if data['wiki'] == 'starcraft': #starcraft
    data['extradata']['role'] = data['extradata']['faction']
  if not 'hero' in data['extradata']:
    data['extradata']['hero'] = '(N/A)'
  if not 'hero2' in data['extradata']:
    data['extradata']['hero2'] = '(N/A)'
  if not data['team']:
    data['team'] = 'no team (free agent)'
  if not data['links']['twitter']:
    data['links']['twitter'] = 'N/A'
  if not data['links']['facebook']:
    data['links']['facebook'] = 'N/A'
  if not data['links']['youtube']:
    data['links']['youtube'] = 'N/A'
  if not data['links']['reddit']:
    data['links']['reddit'] = 'N/A'
  if not data['links']['vk']:
    data['links']['vk'] = 'N/A'
  if not data['links']['weibo']:
    data['links']['weibo'] = 'N/A'
  return data

  