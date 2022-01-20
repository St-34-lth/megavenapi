# A product item has 
# id
# prices
# description
from urllib.error import HTTPError
from MegavenApi import MegavenApi
import requests 

class Product:

          product_id=0
          
          def __init__(self,description, purchasedPrice, salesPrice, sku):
                   
                    self.description = str(description)
                    self.purchasePrice = float(purchasedPrice)
                    self.salesPrice = float(salesPrice)
                    self.sku = str(sku)
                   
                    
                    self.product_id = Product.product_id
                    Product.product_id+=1
                    
                   
          def setProductLocation(self,locationAddress,locationName):          
                    
                    try:
                              filters = {}
                              response = MegavenApi.getInventoryLocation(filters)

                              self.inventoryLocations = response.json()
                              for loc in self.inventoryLocations['mvInventoryLocations']:
                                        
                                        if loc['InventoryLocationAddress'] == locationAddress and loc['InventoryLocationName'] == locationName:

                                                  self.inventoryLocationID = loc['InventoryLocationID']
                                                  self.inventoryLocationName = loc['InventoryLocationName']
                                                  self.inventoryLocationAddress = loc['InventoryLocationAddress']
                                                  return
                                        else:
                                                  pass         
                                                  
                                                  # self.inventoryLocationID = self.inventoryLocations[
                                                  #           'mvInventoryLocations'][0]['InventoryLocationID']
                                                  # self.inventoryLocationName = self.inventoryLocations[
                                                  # 'mvInventoryLocations'][0]['InventoryLocationName']
                                                  # self.inventoryLocationAddress = self.inventoryLocations[
                                                  # 'mvInventoryLocations'][0]['InventoryLocationAddress']
                              self.inventoryLocationID = ''
                              self.inventoryLocationName = ''
                              self.inventoryLocationAddress = ''
                              print('Could not be found')

                    except HTTPError or ConnectionError or ValueError:
                                        print('failed to get info from API')
                 
          def getProductLocationName(self):
                    return self.inventoryLocationName
          def getProductLocationID(self):
                    return self.inventoryLocationID
          def getProductLocationAddress(self):
                    return self.inventoryLocationAddress
          def getProductDescription(self):
                    return self.description
          
          def getProductPurchasePrice(self):
                    return self.purchasePrice
          def getProductSalesPrice(self):
                    return self.salesPrice
          
          def getProductID(self):
                    return self.product_id
          def getProductSKU(self):
                    return self.sku
         
          