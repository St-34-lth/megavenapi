from MegavenApi import MegavenApi

# A class to represent a sale order 
# Holds all relevant information that a sale requires when is inserted in the cloud
# Takes in product,client,tax and discount objects associated with the sale and a qty int/float, saleTypeId int and if available inventoryStock location and name.
# Once the object is created, it calls the setInfo methods of the associated object entities(discount,tax,client,product).
# On the improvements side, it could be the case that the objects store their 'cloud information'. It would make execution of a sale faster if that is preferrable.
class Sale:
         
          saleId=1
          SaleOrderNo=1

          def __init__(self, product, client, qty, tax, discount,saleTypeId,fromInventoryLocation='',fromInventoryName=''):
                    self.product = product 
                    self.client = client 
                    self.qty = float(qty)  
                    self.tax = tax 
                    self.discount = discount
                    self.salesOrderTypeId = saleTypeId
                    
                    self.id = self.saleId
                    Sale.saleId+=1
                    
                    self.saleOrderNo=str(self.SaleOrderNo)
                    Sale.SaleOrderNo+=1
                    
                    self.client.setSupplierClientInfo(True)
                    self.product.setProductLocation(fromInventoryLocation,fromInventoryName)
                    self.tax.setTaxDetails(True)
                    self.discount.setDiscountDetails(True)
                    
                    self.saleDiscountID = self.discount.getDiscountID()
                    self.saleTaxID = self.tax.getTaxID()
                    
                    self.nominalSalePrice = self.product.getProductSalesPrice() * qty
                    
                    self.taxAmount =  tax.getTaxAmount(self.nominalSalePrice)
                    self.discountAmount = discount.getDiscountAmount(self.nominalSalePrice)
                    
                    self.finalPrice = (self.nominalSalePrice + self.taxAmount) - self.discountAmount
                    
          def makeSalesOrder(self,action):
                    MegavenApi.makeSalesOrder(self,action)
                    
         
          def getSaleClientID(self):
                    return self.client.getSupplierClientID()
          def getSaleClientName(self):
                    return self.client.getSupplierClientName()
          
          def getSaleClientAddress(self,addressType):
                    if addressType == 'billing':
                              return self.client.getSupplierBillingAddress()
                    if addressType=='shipping':
                              return self.client.getSupplierShippingAddress()    
                    print('incorrect address type')
                    return 
          
          def getSaleID(self):
                    return self.saleId;
          
          def getSaleTaxID(self):
                    return self.saleTaxID
          
          def getSaleDiscountID(self):
                    return self.saleDiscountID
          
          def getSaleOrderNo(self):
                    return str(self.saleOrderNo)
          
          # Product data
          def getSaleProductID(self):
                    return self.product.getProductID()
          
          def getSaleProductDescription(self):
                    return self.product.getProductDescription()
          
          def getSaleProductSKU(self):
                    return self.product.getProductSKU()
          def getSaleProductLocationID(self):
                    return self.product.getProductLocationID()
          
          # Sale data
          def getSaleNominalPrice(self):
                    return self.nominalSalePrice;
          
          def getSaleTotalQty(self):
                    return self.qty
          
          def getSaleTaxAmount(self):
                    return self.taxAmount
           
          def getSaleDiscountAmount(self):
                    return self.discountAmount
          
          def getSaleFinalPrice(self):
                    return self.finalPrice
          def getSalesOrderTypeId(self):
                    return self.salesOrderTypeId
          
          