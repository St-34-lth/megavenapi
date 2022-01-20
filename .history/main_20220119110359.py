import json
import requests
import aiohttp
import asyncio
from Discount import Discount
from Tax import Tax
from Contact import Contact
from MegavenApi import MegavenApi

# test = Discount('loyalty', 20, 'llt', 'for loyal')
# print(test.getName())
# print(test.getDiscountedPrice(200))

# test2 = Tax('vat', 24, 'vat', 'greek vat')
# print(test2.getName(), test2.getTaxedPrice(200))

# c = Contact('babis', 'example 20', 'person', '123456789')
# print(c.getName(), c.getAddress(), c.getPhone())
url = "https://api.megaventory.com/v2017a/APIkey/APIkeyGet?APIKEY=&format=json"
payload = { "format":"json"}
mtest = MegavenApi('2795d72f4d21ccdf@m128003')

mtest.fetch('get',payload)
