from urllib.error import HTTPError
from MegavenApi import MegavenApi
import requests 

# A class to hold all data related to a product in the megaventory API
# Its updateProduct method registers the product with the API, its setProductLocation, sets the product's location with an inventory in the API
class Product:

          product_id=0
          
          def __init__(self,description, purchasedPrice, salesPrice, sku):
                   
                    self.description = str(description)
                    self.purchasePrice = float(purchasedPrice)
                    self.salesPrice = float(salesPrice)
                    self.sku = str(sku)
                    self.product_id = Product.product_id
                    Product.product_id+=1
                    
          def updateProduct(self,action):
                    MegavenApi.insertProduct(self, action)
                    
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
         
          