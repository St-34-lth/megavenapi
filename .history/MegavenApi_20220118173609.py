import json

import requests

from Discount import Discount
from Tax import Tax

from Contact import Contact 

  
# apiKey = {"key": "2795d72f4d21ccdf@m128003"}
# payload = { 'APIKEY':apiKey['key'],"format":"json"}
# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)
# print(getter.url)
# print(getter.text)
# # https://api.megaventory.com/v2017a/APIkey/APIkeyGet?APIKEY=2795d72f4d21ccdf%40m128003&format=json

test = Discount('loyalty',20,'llt','for loyal')
print(test.getName())
print(test.getDiscountedPrice(200))

test2 = Tax('vat',24,'vat','greek vat')
print(test2.getName(),test2.getTaxedPrice(200))

c = Contact('babis','example 20','person','123456789')