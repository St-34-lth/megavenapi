# A product item has 
# id
# prices
# description

class Product:

          def __init__(self, name, description, purchasedPrice, salesPrice, sku, id, type):
                    self.name = name
                    self.description = str(description)
                    self.purchasePrice = float(purchasedPrice)
                    self.salesPrice = float(salesPrice)
                    self.sku = str(sku)
                    self.id= int(id)
                    self.type= str(type)
                    
          
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