import json
import pathlib
import requests

apiKey = {"key": "2795d72f4d21ccdf@m128003"}
payload = { 'APIKEY':apiKey['key'],"format":"json"}
getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)
print(getter.url)
print(getter.text)
# https://api.megaventory.com/v2017a/APIkey/APIkeyGet?APIKEY=2795d72f4d21ccdf%40m128003&format=json
