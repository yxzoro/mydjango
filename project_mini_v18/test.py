

import requests

r = requests.request('get', 'http://127.0.0.1:8000/X', auth=('a', 'b'))

print r