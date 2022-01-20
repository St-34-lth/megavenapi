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
                    res = self._session.post(self._url+endPoint,data=payload)
                    print(res.url)
                    print(res.status_code)
                    
                    
                    
              if method == "get":
                    payload = dict(self._apiKey, **payload)
                    res = self._session.get(self._url+endPoint, params=payload)
                    return res.text

#   "APIKEY": "string",
#   "mvProduct": {
#     "ProductID": "int",
#     "ProductType": "string",
#     "ProductSKU": "string",
#     "ProductEAN": "string",
#     "ProductDescription": "string",}
#        
#      
          def insertProduct(self,product):
                    
                   
                    mvProduct = {'mvProduct':{'ProductID': product.id, 'ProductType': f'{product.type}','ProductSKU':f'{product.sku}','ProductDescription':f'{product.description}'}}
                    mvRecordAction = {'mvRecordAction':"Insert"}
                    productSellingPrice = {'ProductSellingPrice':product.price}
                    
                    payload = dict(self._apiKey, **mvProduct, **mvRecordAction, **productSellingPrice)
                    
                    # print(payload) 
                    self.fetch('post',payload,'Product/ProductUpdate')
                    