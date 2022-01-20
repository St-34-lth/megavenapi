# Has 
# name 
# description
# value
from Surcharge import Surcharge


class Tax(Surcharge):
          type = 'Tax'

          def __init__(self, name, value, descr=""):

                    self.descr = descr
                    Surcharge.__init__(self, name, value)

          def getTaxAmount(self, priceBeforetax):
                    return  Surcharge.getSurchargedPrice(self.getValue(),priceBeforetax)

          def getTaxedPrice(self, priceBeforetax):
                    taxedPrice = priceBeforetax + Surcharge.getSurchargedPrice(self.getValue(),priceBeforetax)
                    return taxedPrice

          def getName(self):
                    return self.name

          def getValue(self):
                    return self.value

          def getDescription(self):
                    return self.descr


                    