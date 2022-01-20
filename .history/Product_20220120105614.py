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
                    
                   
          def setProductLocation(self,locationAddress):          
                    
                    try:
                              filters = {}
                              response = MegavenApi.getInventoryLocation(filters)

                              self.inventoryLocations = response.json()
                              for loc in self.inventoryLocations['mvInventoryLocations']:
                                        location = loc['InventoryLocationAddress']
                                        if location == locationAddress:
                                                 
                                                  self.inventoryLocationID = location['InventoryLocationID']
                                                  self.inventoryLocationName = location['InventoryLocationName']
                                                  self.inventoryLocationAddress = location['InventoryLocationAddress']
                                        else:
                                                  pass         
                                                  
                                                  # self.inventoryLocationID = self.inventoryLocations[
                                                  #           'mvInventoryLocations'][0]['InventoryLocationID']
                                                  # self.inventoryLocationName = self.inventoryLocations[
                                                  # 'mvInventoryLocations'][0]['InventoryLocationName']
                                                  # self.inventoryLocationAddress = self.inventoryLocations[
                                                  # 'mvInventoryLocations'][0]['InventoryLocationAddress']
                                        

                    except HTTPError or ConnectionError or ValueError:
                                        print('failed to get info from API')
                    
          

          
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
         
          