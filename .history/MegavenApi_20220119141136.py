import json
# from types import NoneType
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
                   

                    if method=="post":
                              url = self._url+endPoint
                              params= {'format':form['format']}
                              res = requests.post(url, json=payload,params=params)
                              print(res.status_code,res.text)
                              return res
                    
                    
                    if method == "get":
                              payload = dict(self._apiKey, **payload, **form)
                              res = self._session.get(self._url+endPoint, params=payload)
                              return res
    
          def insertProduct(self,product):
                   
                    endPoint = "Product/ProductUpdate"
                    method = 'post'
                    try:
                    
                              mvProduct = {'mvProduct':{'ProductID': product.id, 'ProductType': f'{product.type}','ProductSKU':f'{product.sku}','ProductDescription':f'{product.description}'}}
                              
                              mvRecordAction = {'mvRecordAction':"Insert"}
                              
                              productSellingPrice = {'ProductSellingPrice':product.price}
                              
                              payload = dict(
                                  {"APIKEY": self._apiKey['APIKEY']}, ** mvProduct, **mvRecordAction, **productSellingPrice)
                              print(payload)
                              return self.fetch(method, payload, endPoint)
                    
                    except AttributeError:
                              print('Invalid product entries')
                   
      
          def testKey(self,method):
                    endPoint = "APIkey/APIkeyGet"
                    method= method
                    payload = {'APIKEY':self._apiKey['APIKEY']}
                    
                    res = self.fetch(method,payload,'APIkey/APIkeyGet')
                    return res 
          
          def contactPersonUpdate(self,contact):
                    endPoint = "ContactPerson/ContactPersonUpdate"
                    method = 'post'
                    if contact.getType()=='person':
                        
                              ContactFullAddress = {"AddressType": contact.getAddressType()}
                              mvContactPerson = {"mvContactPerson":
                                                  {"ContactId":contact.getId(),
                                                  "ContactName":contact.getName(),
                                                  "ContactAddress":contact.getAddress(),
                                                  "ContactFullAddress":ContactFullAddress,
                                                  "ContactEmail":contact.getEmail(),
                                                  "ContactPhone1":contact.getPhone() }
                                        }
                              
                              
                              payload = dict(self._apiKey,**mvContactPerson)
                              print(json.dumps(payload))
                              print(payload)
                              # res= self.fetch(method,payload,endPoint)
                              # return res