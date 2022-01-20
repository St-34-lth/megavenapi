import json
import aiohttp
import requests
import asyncio
  
# apiKey = {"key": "2795d72f4d21ccdf@m128003"}
# payload = { 'APIKEY':apiKey['key'],"format":"json"}
# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)
# print(getter.url)
# print(getter.text)
url= "https://api.megaventory.com/v2017a/APIkey/APIkeyGet?APIKEY=2795d72f4d21ccdf%40m128003&format=json"

class MegavenApi:
          def __init__(self, _apiKey):
                    self._apiKey = _apiKey
         


          async def fetch(url,payload):
                    async with aiohttp.ClientSession(headers=payload) as session, session.get(url) as response:
                            

                                        print("Status:", response.status)
                                        

                                        jsonbody = await response.json()
                                        print(jsonbody)

          # loop = asyncio.get_event_loop()
          # loop.run_until_complete(fetch())


# async def fetch(url, headers=''):

#     async with ClientSession(headers=headers) as session, session.get(url) as res:

#         ret = await res.json()
#         return ret
