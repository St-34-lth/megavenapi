# requires:
# orderId, orderno, orderstatus if orderInventorylocationID, clientid

class Sale:
         
          saleId=0
          SaleOrderNo=0

          def __init__(self, product, client, qty, tax, discount):
                    self.product = product 
                    self.client = client 
                    self.qty = qty
                    self.tax = tax 
                    self.discount = discount
                     
                    self.id = self.saleId
                    Sale.saleId+=1
                    
                    self.saleOrderNo=str(self.SaleOrderNo)
                    Sale.SaleOrderNo+=1
                    
                    self.client.setSupplierClientInfo(True)
                    
                    self.nominalSalePrice = self.product.getProductSalesPrice() * qty
                    
                    self.taxAmount =  tax.getTaxAmount(self.nominalSalePrice)
                    self.discountAmount = discount.getDiscountAmount(self.nominalSalePrice)
                    
                    self.finalPrice = (self.nominalSalePrice + self.taxAmount) - self.discountAmount
                    
          
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
          
          def getSaleOrderNo(self):
                    return str(self.saleOrderNo)
          
          def getSaleProductID(self):
                    return self.product.getProductID()
          
          def getSaleProductDescription(self):
                    return self.product.getProductDescription()
          
          def getSaleProductSKU(self):
                    return self.product.getProductSKU()
          
          def getNominalSalePrice(self):
                    return self.nominalSalePrice;
          
          def getTotalQty(self):
                    return self.qty
          
          def getSaleTaxAmount(self):
                    return self.taxAmount
           
          def getSaleDiscountAmount(self):
                    return self.discountAmount
          
          def getFinalPrice(self):
                    return self.finalPrice

          
          