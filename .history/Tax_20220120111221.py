# Has 
# name 
# description
# value
from Surcharge import Surcharge


class Tax(Surcharge):
          type = 'Tax'

          def __init__(self, _name, _value, _descr=""):
                    
                    self._descr = _descr
                    Surcharge.__init__(self, _name, _value)

          def getTaxedPrice(self, priceBeforetax):
                    taxedPrice = priceBeforetax + Surcharge.getSurchargedPrice(self.getValue(),priceBeforetax)
                    return taxedPrice

          def getName(self):
              return super().getName()
    
          def getValue(self):
              return super().getValue()
          
          def getDescription(self):
                    return self._descr


                    