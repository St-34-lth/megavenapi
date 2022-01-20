import json
import aiohttp
import requests
import asyncio
  
# apiKey = {"key": "2795d72f4d21ccdf@m128003"}
# payload = { 'APIKEY':apiKey['key'],"format":"json"}
# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)
# print(getter.url)
# print(getter.text)


class MegavenApi:
          
          
        
         
          
          def __init__(self, _apiKey):
                    self._apiKey = _apiKey
                    self._client = requests()
                    self._url = "https://api.megaventory.com/v2017a/"
          

          def fetch(endPoint,payload,method):
                    if method=="get":
                              
                              self._client.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet', params=payload)
        