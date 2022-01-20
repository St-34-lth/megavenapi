from inspect import Attribute
import json
import requests


# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)

class MegavenApi:
          
          def __init__(self, _apiKey,url):
                    self._apiKey ={'APIKEY':_apiKey}
                    self._url = url
          
          
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
          
          def insertSupplierClient(self,supplier,action):
                    endPoint = "SupplierClient/SupplierClientUpdate"
                    method = 'post'
                    mvRecordAction= {'mvRecordAction':action}
                   
                    if supplier != None:
                              try:
                                       
                                        mvContacts =[]
                                        supplierContacts = supplier.getSupplierClientContacts()
                                       
                                        for i in range(len(supplierContacts)-1) :
                                                  
                                                  contact = supplierContacts[i]
                                                  if contact.getContactType() =='person':
                                                            mvContact = {

                                                            "ContactName": contact.getContactName(),
                                                            "ContactEmail": contact.getContactEmail(),
                                                            "ContactPhone1": contact.getContactPhone()
                                                            }
                                                            mvContacts.append(mvContact)
                                        
                                        # print(mvContacts)
                                        
                                        mvSupplierClient ={ "mvSupplierClient":
                                                            {
                                                                      'SupplierClientType': supplier.getSupplierClientType(),
                                                                      'SupplierClientName': supplier.getSupplierClientName(),
                                                                      'mvContacts': mvContacts,
                                                                      'SupplierClientBillingAddress': None,
                                                                      'SupplierClientShippingAddress': None,
                                                            }}
                                        
                                        supplierAddresses = supplier.getSupplierClientAddresses()
                                        
                                        
                                        for i in range(len(supplierAddresses)-1):
                                                  address=supplierAddresses[i]

                                                  addressType = address.getAddressType()
                                                  
                                                  if addressType == 'shipping':
                                                            mvSupplierClient['mvSupplierClient']['SupplierClientShippingAddress'] = address.getAddressLocation()
                                                  
                                                  elif addressType == 'billing':
                                                            mvSupplierClient['mvSupplierClient']['SupplierClientBillingAddress'] = address.getAddressLocation()
                                                  else:
                                                            continue 
                                            
                                        # payload = dict(self._apiKey,**mvSupplierClient,**mvRecordAction)
                                        print(mvContacts)
                                        # print(mvSupplierClient)
                                        # print(payload)
                                        # res= self.fetch(method,payload,endPoint)
                                        # return res
                              except AttributeError:
                                        print('invalid supplier')
                    else:
                              print('invalid supplier')
          
          def inventoryLoc(self,name,address,action):
                    method = 'post'
                    endPoint = "InventoryLocation/InventoryLocationUpdate"
                    
                    if address.getAddressType()=='item':
                              
                              try:
                                        Address = {"AddressType": address.getAddressType()}
                                        
                                        mvInventoryLocation = {
                                                  "mvInventoryLocation":
                                                            {
                                                                      "InventoryLocationName":name,
                                                                      "InventoryLocationAbbreviation": address.getAbbrvn(),
                                                                      "InventoryLocationAddress":address.getAddress()
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
                                        res = self.fetch(
                                            method, payload, endPoint)
                                        return res
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
                                        res = self.fetch(
                                            method, payload, endPoint)
                                        return res
                                        
                              else:
                                     print('invalid discount object')

                    except AttributeError:
                            print('invalid discount object')
          # {
          #     "mvSalesOrder": {
          #         "SalesOrderClientId": 5358,
          #         "SalesOrderTypeId": 3,
          #         "SalesOrderStatus": "Pending",
          #         "SalesOrderDetails": [
          #             {
          #                 "SalesOrderRowProductSKU": "product",
          #                 "SalesOrderRowQuantity": "10",
          #                 "SalesOrderRowShippedQuantity": "0",
          #                 "SalesOrderRowInvoicedQuantity": "0",
          #                 "SalesOrderRowUnitPriceWithoutTaxOrDiscount": "0.93"
          #             }
          #         ]
          #     },
          #     "mvRecordAction": "Insert"
          # def makeSalesOrder(self,client,product,)