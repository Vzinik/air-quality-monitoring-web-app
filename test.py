import requests
from flask import jsonify
r = requests.get('https://api.github.com/events')

print(r.status_code-1)