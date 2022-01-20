from inspect import Attribute
import json
import requests

  
# apiKey = {"key": "2795d72f4d21ccdf@m128003"}
# url = "https://api.megaventory.com/v2017a/APIkey/APIkeyGet?APIKEY=&format=json"
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
                              try:
                                        ContactFullAddress = {"AddressType": contact.getAddressType()}
                                        
                                        mvContactPerson = {"mvContactPerson":
                                                            {
                                                                      "ContactId":contact.getId(),
                                                                      "ContactName":contact.getName(),
                                                                      "ContactAddress":contact.getAddress(),
                                                                      "ContactFullAddress":ContactFullAddress,
                                                                      "ContactEmail":contact.getEmail(),
                                                                      "ContactPhone1":contact.getPhone() 
                                                            }
                                                  }
                                        
                                        
                                        payload = dict(self._apiKey,**mvContactPerson)
                              
                                        print(payload)
                                        res= self.fetch(method,payload,endPoint)
                                        return res
                              except AttributeError:
                                        print('invalid contact')
                    else:
                              print('invalid contact')
          
#           "APIKEY": "string",
          #   "mvInventoryLocation": {
          #     "InventoryLocationID": "int",
          #     "InventoryLocationName": "string",
          #     "InventoryLocationAbbreviation": "string",
          #     "InventoryLocationAddress": "string",
          #     "Address": {
          #       "AddressType": "string",
          def inventoryLoc(self,contact,action):
                    method = 'post'
                    endPoint = "InventoryLocation/InventoryLocationUpdate"
                    
                    if contact.getType()=='item':
                              
                              try:
                                        Address = {"AddressType": contact.getAddressType()}
                                        mvInventoryLocation = {
                                                  "mvInventoryLocation":
                                                            {
                                                                      "InventoryLocationName":contact.getName(),
                                                                      "InventoryLocationAbbreviation": contact.getAbbrvn(),
                                                                      "InventoryLocationAddress":contact.getAddress()
                                                            },"Address": Address 
                                                  }
                                        mvRecordAction = {"mvRecordAction":action}
                                        
                                        payload = dict(
                                            self._apiKey, **mvInventoryLocation,**mvRecordAction)

                                        print(payload)
                                        res = self.fetch(
                                            method, payload, endPoint)
                                        return res
                              except AttributeError:
                                        print('invalid contact details')
                    else:
                              print('invalid contact details')
                    
          # {
          #     "APIKEY": "string",
          #     "mvTax": {
          #         "TaxID": "int",
          #         "TaxName": "string",
          #         "TaxDescription": "string",
          #         "TaxValue": "double"
          #     },
          #     "mvRecordAction": "string",
          #     "mvInsertUpdateDeleteSourceApplication": "string"
          # }
          def updateTax(self,tax,action):
                    method='post'
                    endPoint='Tax/TaxUpdate'
                    
                    try:
                              if tax.type=='Tax':
                                        
                                        mvTax = {
                                                  "mvTax":
                                                            {
                                                                      'TaxName':tax.getName(),
                                                                      'TaxDescription':tax.getDescription(),
                                                                      'TaxValue':tax.getValue()
                                                            }
                                                  }
                                        mvRecordAction = {'mvRecordAction': action}
                                        payload = dict(self._apiKey,**mvTax,**mvRecordAction)
                                        print(payload)
                              else:
                                        print('invalid tax object')
                    
                    except AttributeError:
                              print('invalid tax object') 
                    
          def updateDiscount(self,discount,action):
                    method = 'post'
                    endPoint = 'Discount/DiscountUpdate'

                    try:
                              if discount.type == 'Discount':

                                        mvDiscount = {
                                                  "mvDiscount":
                                                            {
                                                                      'DiscountName': discount.getName(),
                                                                      'DiscountDescription': discount.getDescription(),
                                                                      'DiscountValue': discount.getValue()
                                                            }
                                                  }
                                     
                                        mvRecordAction = {
                                           'mvRecordAction': action}
                                        payload = dict(
                                           self._apiKey, **mvDiscount, **mvRecordAction)
                                        print(payload)
                              else:
                                     print('invalid discount object')

                    except AttributeError:
                            print('invalid discount object')
