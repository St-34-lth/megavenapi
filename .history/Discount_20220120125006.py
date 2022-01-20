#!./Surcharge.py
from Surcharge import Surcharge
from MegavenApi import MegavenApi
import requests
# has
# name
# description
# value

class Discount(Surcharge):
          type = 'Discount'
          
          def __init__(self, name, value,descr=""):
                    
                    self.descr = descr
                    Surcharge.__init__(self, name, value)

          def setTaxDetails(self, searchByName=False)):
                    if searchByName:
                              filters={'filters': {
                              {
                                        "FieldName": "DiscountName",
                                        "SearchOperator": "Equals",
                                        "SearchValue": self.name
                              },
                              }}
                              self.discountDetails=MegavenApi.getTaxInfo(filters)
                              self.discountDetails=self.discountDetails.json()
                              self.discountDetails=self.taxDetails['DiscountID']
             
          def getDiscountedPrice(self,priceBeforeDiscount):
                    discountedPrice = priceBeforeDiscount- super().getSurchargedPrice(self.getValue(),priceBeforeDiscount)
                    return discountedPrice
          
          def getDiscountAmount(self, priceBeforeDiscount):
                    return Surcharge.getSurchargedPrice(self.getValue(), priceBeforeDiscount)
          
          def getName(self):
                    return self.name
    
          def getValue(self):
                    return self.value
          
          def getDescription(self):
                    return self.descr          
          
          