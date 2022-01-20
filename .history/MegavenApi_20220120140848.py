from inspect import Attribute
import json
import requests
from pathlib import Path 

# getter = requests.get('https://api.megaventory.com/v2017a/APIkey/APIkeyGet',params=payload)

class MegavenApi:
          
          _apiKey = {'APIKEY':''}
          _url =''
          
          def __init__(self, _apiKey,_url):          
                    MegavenApi._apiKey['APIKEY'] = _apiKey
                    MegavenApi._url = _url
                              
          @staticmethod         
          def saveResponse(response,filename,format):
                    p = Path('./')

                    with open(p / f'{filename}.{format}', 'w') as file:
                   
                              json.dump(response,file)
                              file.write('\r\n')
          
          @staticmethod
          def fetch(method, payload=dict(), endPoint=""):
                    form = {'format': 'json'}
                   
                    if method=="post":
                              url = MegavenApi._url+endPoint
                              params= {'format':form['format']}
                              res = requests.post(url, json=payload,params=params)
                              print(res.status_code,res.text)
                              
                              return res
                    
                    
                    if method == "get":
                              payload = dict(MegavenApi._apiKey, **payload, **form)
                              res = requests.get(MegavenApi._url+endPoint, json=payload)
                              
                              return res
          
          @staticmethod
          def insertProduct(product,action):

                    endPoint = "Product/ProductUpdate"
                    method = 'post'
                    try:
                              mvRecordAction = {"mvRecordAction": action}
                              if action=='Insert':
                                        mvProduct = {'mvProduct':
                                                  {
                                                            'ProductID': product.getProductID(),
                                                            'ProductSKU':product.getProductSKU(),
                                                            'ProductDescription':product.getProductDescription(),
                                                            'ProductSellingPrice': product.getProductSalesPrice()
                                                  }
                                                  }
                                                  
                                        
                              
                                        
                                        payload = dict(
                                        MegavenApi._apiKey, ** mvProduct, **mvRecordAction)
                              
                              print(payload)
                              return MegavenApi.fetch(method, payload, endPoint)
                    
                    except AttributeError:
                              print('Invalid product entries')
                   
          def testKey(self,method):
                    endPoint = "APIkey/APIkeyGet"
                    method= method
                    payload = {'APIKEY':self._apiKey['APIKEY']}
                    
                    res = self.fetch(method,payload,'APIkey/APIkeyGet')
                    return res 
          
          @staticmethod
          def insertSupplierClient(supplier,action):
                    endPoint = "SupplierClient/SupplierClientUpdate"
                    method = 'post'
                    mvRecordAction= {'mvRecordAction':action}
                   
                    if supplier != None:
                              try:
                                       
                                        mvContacts =[]
                                        supplierContacts = supplier.getSupplierClientContacts()
                                       
                                        for contact in supplierContacts :
                                                  
                                                  
                                                  if contact.getContactType() =='person':
                                                            mvContact = {

                                                            "ContactName": contact.getContactName(),
                                                            "ContactEmail": contact.getContactEmail(),
                                                            "ContactPhone1": contact.getContactPhone()
                                                            }
                                                            mvContacts.append(mvContact)
                                        
                              
                                        
                                        mvSupplierClient ={ "mvSupplierClient":
                                                            {
                                                                      'SupplierClientType': supplier.getSupplierClientType(),
                                                                      'SupplierClientName': supplier.getSupplierClientName(),
                                                                      'mvContacts': mvContacts,
                                                                      'SupplierClientBillingAddress': None,
                                                                      'SupplierClientShippingAddress': None,
                                                            }}
                                        
                                        supplierAddresses = supplier.getSupplierClientAddresses()
                                        
                                        
                                        for address in supplierAddresses:
                                                  
                                                
                                                 
                                                  addressType = address.getAddressType()
                                                  
                                                  if addressType == 'shipping':
                                                            mvSupplierClient['mvSupplierClient']['SupplierClientShippingAddress'] = address.getAddressLocation()
                                                  
                                                  if addressType == 'billing':
                                                            mvSupplierClient['mvSupplierClient']['SupplierClientBillingAddress'] = address.getAddressLocation()
                                                  
                                                  
                                            
                                        payload = dict(MegavenApi._apiKey,**mvSupplierClient,**mvRecordAction)
                                       
                                        print(payload)
                                        res= MegavenApi.fetch(method,payload,endPoint)
                                        res = json.load(res.text)
                                        
                                        MegavenApi.saveResponse(res,'supplierClientsuccess'+f"{res['mvSupplierClient']['SupplierClientID']}",'json')
                                        
                                        return res
                              except AttributeError:
                                        print('invalid supplier')
                    else:
                              print('invalid supplier')
          
          @staticmethod
          def inventoryLoc(name,address,action):
                    method = 'post'
                    endPoint = "InventoryLocation/InventoryLocationUpdate"
                    
                    if address.getAddressType()=='item':
                              
                              try:
                                        Address = {"AddressType": address.getAddressType()}
                                        mvRecordAction = {
                                            "mvRecordAction": action}
                                        mvInventoryLocation = {
                                                  "mvInventoryLocation":
                                                            {
                                                                      "InventoryLocationName":name,
                                                                      "InventoryLocationAbbreviation": address.getAbbrvn(),
                                                                      "InventoryLocationAddress":address.getAddressLocation()
                                                            },"Address": Address 
                                                  }
                                        
                                        
                                        payload = dict(
                                            MegavenApi._apiKey, **mvInventoryLocation,**mvRecordAction)

                                        print(payload)
                                        res = MegavenApi.fetch(
                                            method, payload, endPoint)
                                        return res
                              except AttributeError:
                                        print('invalid contact details')
                    else:
                              print('invalid contact details')
          @staticmethod    
          def updateTax(tax,action):
                    method='post'
                    endPoint='Tax/TaxUpdate'
                    
                    try:
                              if tax.type=='Tax':
                                        mvRecordAction = {'mvRecordAction': action}
                                        mvTax = {
                                                  "mvTax":
                                                            {
                                                                      'TaxName':tax.getName(),
                                                                      'TaxDescription':tax.getDescription(),
                                                                      'TaxValue':tax.getValue()
                                                            }
                                                  }
                                        
                                        payload = dict(MegavenApi._apiKey,**mvTax,**mvRecordAction)
                                        print(payload)
                                        res = MegavenApi.fetch(
                                            method, payload, endPoint)
                                        return res
                              else:
                                        print('invalid tax object')
                    
                    except AttributeError:
                              print('invalid tax object') 
          
          @staticmethod
          def getTaxInfo(filters):
                    method = 'post'
                    endPoint='Tax/TaxGet'
                    filters = filters
                    
                    payload = dict(MegavenApi._apiKey,**filters)
                    response = MegavenApi.fetch(method,payload,endPoint)
                    MegavenApi.saveResponse(response.text,'taxesResponse','json')
                    return response
          
          @staticmethod
          def getDiscountInfo(filters):
                    method = 'post'
                    endPoint='Discount/DiscountGet'
                    filters = filters
                    
                    payload = dict(MegavenApi._apiKey,**filters)
                    response = MegavenApi.fetch(method,payload,endPoint)
                    MegavenApi.saveResponse(response.text,'discountsResponse','json')
                    return response
          
          @staticmethod
          def updateDiscount(discount,action):
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
                                           MegavenApi._apiKey, **mvDiscount, **mvRecordAction)
                                        print(payload)
                                        res = MegavenApi.fetch(
                                            method, payload, endPoint)
                                        return res
                                        
                              else:
                                     print('invalid discount object')

                    except AttributeError:
                            print('invalid discount object')
          
          @staticmethod
          def getSupplierClientInfo(supplier,filters):
                    
                    method='post'
                    endPoint='SupplierClient/SupplierClientGet'
                    filters = filters
                    
                    payload = dict(MegavenApi._apiKey,**filters)
                    response = MegavenApi.fetch(method,payload,endPoint)
                    MegavenApi.saveResponse(response.text,f'{supplier.getSupplierClientName()}','json')
                    return response
          
          @staticmethod
          def getInventoryLocation(filters):
                    method='post'
                    endPoint ='InventoryLocation/InventoryLocationGet'
                    
                    filters = filters

                    payload = dict(MegavenApi._apiKey, **filters)
                    response = MegavenApi.fetch(method, payload, endPoint)
                    MegavenApi.saveResponse(response.text, 'inventoryLocations', 'json')
                    return response
          @staticmethod  
          def makeSalesOrder(sale,action):
                    method='post'
                    endPoint = 'SalesOrder/SalesOrderUpdate'
                    mvRecordAction= {'mvRecordAction': action}
                    #  "SalesOrderTypeId": 3,
                    # "SalesOrderTypeAbbreviation": "SO",
                    # "SalesOrderTypeDescription": "Sales Order"
                    SalesOrderDetails = [
                              {
                              "SalesOrderRowProductID": sale.getSaleProductID(),
                              "SalesOrderRowProductSKU": sale.getSaleProductSKU(),
                              "SalesOrderRowProductDescription": sale.getSaleProductDescription(),
                              "SalesOrderRowQuantity": sale.getSaleTotalQty(),
                                  "SalesOrderRowUnitPriceWithoutTaxOrDiscount": sale.getSaleNominalPrice(),
                              "SalesOrderTotalTaxAmount": sale.getSaleTaxAmount(), 
                                  "SalesOrderRowTotalDiscountAmount": sale.getSaleDiscountAmount(),
                                  "SalesOrderRowTotalAmount": sale.getSaleFinalPrice(),
                              }
                    ]
                    
                    # SalesOrderId, SalesOrderNo, SalesOrderStatus
                    # SalesOrderStatus is mandatory if SalesOrderInventoryLocationID
                    # SalesOrderClientId, SalesOrderClientName
                    mvSalesOrder= {"mvSalesOrder": 
                              {  
                                        "SalesOrderId": sale.getSaleID(), 
                                        "SalesOrderTypeId":sale.getSalesOrderTypeId(),
                                        "SalesOrderNo": sale.getSaleOrderNo(),
                                        "SalesOrderClientID": sale.getSaleClientID(),
                                        "SalesOrderClientName": sale.getSaleClientName(),
                                        "SalesOrderInventoryLocationID":sale.getSaleProductLocationID(),
                                        "SalesOrderBillingAddress": sale.getSaleClientAddress('billing'),
                                        "SalesOrderShippingAddress": sale.getSaleClientAddress('shipping'),
                                        "SalesOrderTotalQuantity": sale.getSaleTotalQty(),
                                        "SalesOrderAmountSubtotalWithoutTaxAndDiscount": sale.getSaleNominalPrice(),
                                        "SalesOrderAmountTotalDiscount": sale.getSaleDiscountAmount(),
                                        "SalesOrderAmountTotalTax": sale.getSaleTaxAmount(),
                                        "SalesOrderAmountGrandTotal":sale.getSaleFinalPrice(),
                                        "SalesOrderDetails":SalesOrderDetails,
                                        "SalesOrderStatus": "verified",
                              }
                    }
                    payload = dict(MegavenApi._apiKey,**mvSalesOrder,**mvRecordAction)
                    # print(payload)
                    response = MegavenApi.fetch(method,payload,endPoint)
                    return response 