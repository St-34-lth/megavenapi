import json
import aiohttp

import asyncio
  
# apiKey = {"key": "2795d72f4d21ccdf@m128003"}
# payload = { 'APIKEY':apiKey['key'],"format":"json"}
# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)
# print(getter.url)
# print(getter.text)

import requests 
class MegavenApi:
          
    
        
         
          
          def __init__(self, _apiKey):
                    self._apiKey = _apiKey
                    self.session = requests.Session()
                    
                    self._url = "https://api.megaventory.com/v2017a/"
          
          def fetch(self, method, payload=dict(), endPoint=""):
              if method == "get":
                              
                   self.session.get(
                      'https://api.megaventory.com/v2017a/APIkey/APIkeyGet', params=payload)
        
