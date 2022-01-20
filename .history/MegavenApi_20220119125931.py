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
                    
                  
                    self._apiKey ={'APIKEY':_apiKey}
                    self._url = "https://api.megaventory.com/v2017a/"
          
          def fetch(self, method, payload=dict(), endPoint=""):
                    form = {'format': 'json'}
                    headers={'Content-Type': 'application/json'}
                    
                    
                    if method=="post":
                              url = self._url+endPoint
                              # params= {'format':form['format']}
                              
                              res = requests.post(url, data=payload,headers=headers)
                              print(res.url)
                              return res.json()
                    
                    
                    
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
                   
                    endPoint = "Product/ProductUpdate"
                   
                    
                    mvProduct = {'mvProduct':{'ProductID': product.id, 'ProductType': f'{product.type}','ProductSKU':f'{product.sku}','ProductDescription':f'{product.description}'}}
                    
                    mvRecordAction = {'mvRecordAction':"Insert"}
                    
                    productSellingPrice = {'ProductSellingPrice':product.price}
                    
                    payload = dict({"APIKEY": self._apiKey['APIKEY']}, ** mvProduct, **mvRecordAction, **productSellingPrice)
                   
                  
                    # url = self._url+endPoint+'?APIKEY='+self._apiKey['APIKEY']
                    # print(url,payload)
                    return self.fetch('post',payload,endPoint)
                    
                    print(json.dumps(payload))
                    
          def testKey(self,method):
                    endPoint = "APIkey/APIkeyGet"
                    method= method
                    payload = {'APIKEY':self._apiKey['APIKEY']}
                    
                    res = self.fetch(method,payload,'APIkey/APIkeyGet')
                    print(res.text)