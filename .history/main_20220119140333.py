
import json
import requests
import aiohttp
import asyncio
from Discount import Discount
from Tax import Tax
from Contact import Contact
from MegavenApi import MegavenApi
from Product import Product
# test = Discount('loyalty', 20, 'llt', 'for loyal')
# print(test.getName())
# print(test.getDiscountedPrice(200))



# Name: babis
# E-mail: babis@exampletest.com
# Shipping Address: Example 8, Athens
# Phone: 1235698967


babis = Contact('babis', 1, 'Example 8, Athens', 'person',
                '1235698967', 'babis@exampletest.com')


print(babis.getAddressType(),babis.getEmail(),babis.getId(),babis.getType(),babis.getName(),babis.getPhone())
# url = "https://api.megaventory.com/v2017a/APIkey/APIkeyGet?APIKEY=&format=json"

payload = { "format":"json"}
prod = Product('test','test',10.4,12345,5,'test')

# mtest = MegavenApi('2795d72f4d21ccdf@m128003')
# print(prod.id)
# mtest.fetch('get',payload,'APIkey/APIkeyGet')
# test = mtest.insertProduct(prod)
# print(test.text)
# test = mtest.testKey('post')
# print(test.text)