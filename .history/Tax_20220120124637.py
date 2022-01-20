# Has 
# name 
# description
# value
from Surcharge import Surcharge
from MegavenApi import MegavenApi
import requests

class Tax(Surcharge):
          type = 'Tax'

          def __init__(self,name,value, descr=""):

                    self.descr = descr
                    Surcharge.__init__(self, name, value)
                    
          def setTaxDetails(self, searchByName=False)):
                    filters = {'filters':{
                               {
                                   "FieldName": "DiscountName",
                                   "SearchOperator": "Equals",
                                   "SearchValue": self.name
                               },
                    }}
                    MegavenApi.getTaxInfo()
                    
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


                    