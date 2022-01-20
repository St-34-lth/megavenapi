#!./Surcharge.py
from Surcharge import Surcharge
          
# has
# name
# description
# value

class Discount(Surcharge):
          type = 'Discount'
          
          def __init__(self, name, value,descr=""):
                    
                    self.descr = descr
                    Surcharge.__init__(self, name, value)
          
             
          def getDiscountedPrice(self,priceBeforeDiscount):
                    discountedPrice = priceBeforeDiscount- super().getSurchargedPrice(self.getValue(),priceBeforeDiscount)
                    return discountedPrice
          
          def getName(self):
                    return super().name
    
          def getValue(self):
                    return super().value
          def getDescription(self):
                    return self.descr          
          
          