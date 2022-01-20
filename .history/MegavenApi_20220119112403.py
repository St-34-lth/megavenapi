import json
import aiohttp
import requests
import asyncio
  
# apiKey = {"key": "2795d72f4d21ccdf@m128003"}

# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)
# print(getter.url)
# print(getter.text)


class MegavenApi:
          
    
        
         
          
          def __init__(self, _apiKey):
                    
                    self._session = requests.Session()
                    self._apiKey ={'APIKEY':_apiKey}
                    self._url = "https://api.megaventory.com/v2017a/"
          
          def fetch(self, method, payload=dict(), endPoint=""):
              if method=="post":
                    pass

              if method == "get":
                    payload = dict(self._apiKey, **payload)
                    res = self._session.get(self._url+endPoint, params=payload)
                    return res.text
          
          def insertProduct(self,product):
                    
                              
                    
                    
                              self.fetch('post',payload,'Product/ProductUpdate')
                    