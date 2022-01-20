# Has 
# name 
# description
# value
from Surcharge import Surcharge


class Tax(Surcharge):
          type = 'Tax'

          def __init__(self, _name, _value, _descr=""):
                    self._abbrv = _abbrv
                    self._descr = _descr
                    Surcharge.__init__(self, _name, _value)

          def getTaxedPrice(self, priceBeforetax):
                    taxedPrice = priceBeforetax + super().getSurchargedPrice(priceBeforetax)
                    return taxedPrice



                    