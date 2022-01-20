#!./Surcharge.py
import Surcharge
          
# has
# name
# description
# value

class Discount(Surcharge):
          type = 'Discount'
          
          def __init__(self, _name,_value, _abbrv="", _descr=""):
                    self._abbrv= _abbrv
                    self._descr = _descr
                    Surcharge.init(self,_name,_value)
          
             
          def getDiscountedPrice(self,priceBeforeDiscount):
                    discountedPrice = priceBeforeDiscount- super().getSurchargedPrice(priceBeforeDiscount)
                    return discountedPrice
          
          
          
          