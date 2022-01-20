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

          def setDiscountDetails(self, searchByName=False):
                    if searchByName:
                              filters = {'Filters':
                                        [
                                        {
                                                  "FieldName": "DiscountName",
                                                  "SearchOperator": "Equals",
                                                  "SearchValue": self.name
                                        },
                                        ]
                                        }
                              self.discountDetails=MegavenApi.getDiscountInfo(filters)
                              self.discountDetails=self.discountDetails.json()
                              
                    # Could make a search conditional similar to setSupplierDetails method and set all values from the response object if required
                              self.discountID = self.discountDetails['mvDiscounts'][0]['DiscountID']
             
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
          
          