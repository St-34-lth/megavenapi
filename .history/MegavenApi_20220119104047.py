import json
import aiohttp
import requests

  
# apiKey = {"key": "2795d72f4d21ccdf@m128003"}
# payload = { 'APIKEY':apiKey['key'],"format":"json"}
# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)
# print(getter.url)
# print(getter.text)
url= "https://api.megaventory.com/v2017a/APIkey/APIkeyGet?APIKEY=2795d72f4d21ccdf%40m128003&format=json"


import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

          print("Status:", response.status)
         

          jsonbody = await response.json()
          print(jsonbody)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
