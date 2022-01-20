# A product item has 
# id
# prices
# description
from urllib.error import HTTPError
from MegavenApi import MegavenApi
import requests 

class Product:

          product_id=0
          
          def __init__(self, name, description, purchasedPrice, salesPrice, sku, type):
                    self.name = name
                    self.description = str(description)
                    self.purchasePrice = float(purchasedPrice)
                    self.salesPrice = float(salesPrice)
                    self.sku = str(sku)
                    self.type = type
                    
                    self.product_id = Product.product_id
                    Product.product_id+=1
                    
                   
          def setProductLocation(self,location):          
                    
                    try:
                              filters = {}
                              response = MegavenApi.getInventoryLocation(filters)

                              self.inventoryLocation = response.json()
                              self.inventoryLocationID = self.supplierClientInfo[
                                        'mvInventoryLocations'][0]['InventoryLocationID']
                              self.inventoryLocationName = self.supplierClientInfo[
                                  'mvInventoryLocations'][0]['InventoryLocationName']
                              self.inventoryLocationAddress = self.supplierClientInfo[
                                  'mvInventoryLocations'][0]['InventoryLocationAddress']

                    except HTTPError or ConnectionError or ValueError:
                                        print('failed to get info from API')
                    
          
          
          def getProductName(self):
                    return self.name
          
          def getProductDescription(self):
                    return self.description
          
          def getProductPurchasePrice(self):
                    return self.purchasePrice
          def getProductSalesPrice(self):
                    return self.salesPrice
          
          def getProductID(self):
                    return self.id
          def getProductSKU(self):
                    return self.sku
          def getProductType(self):
                    return self.type 
          