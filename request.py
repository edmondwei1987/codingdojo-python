import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print r.status_code
print r.encoding
print r.text
print r.json()