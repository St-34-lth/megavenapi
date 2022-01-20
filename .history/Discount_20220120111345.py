#!./Surcharge.py
from Surcharge import Surcharge
          
# has
# name
# description
# value

class Discount(Surcharge):
          type = 'Discount'
          
          def __init__(self, _name,_value,_descr=""):
                    
                    self._descr = _descr
                    Surcharge.__init__(self,_name,_value)
          
             
          def getDiscountedPrice(self,priceBeforeDiscount):
                    discountedPrice = priceBeforeDiscount- super().getSurchargedPrice(self.getValue(),priceBeforeDiscount)
                    return discountedPrice
          
          def getName(self):
                    return super().getName()
    
          def getValue(self):
                    return super().getValue()
          
          def getDescription(self):
                    return self._descr          
          
          