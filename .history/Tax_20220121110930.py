# Has 
# name 
# description
# value
from Surcharge import Surcharge
from MegavenApi import MegavenApi
import requests

# A class to hold all data related to a Tax in the megaventory API. Derived from Surcharge class. Its insertTax method registers the tax with the API.
class Tax(Surcharge):
          type = 'Tax'

          def __init__(self,name,value, descr=""):

                    self.descr = descr
                    Surcharge.__init__(self, name, value)
          
          def insertTax(self):
                    MegavenApi.updateTax(self, 'Insert')
                    
          def setTaxDetails(self, searchByName=False):
                    if searchByName:
                              filters = {'Filters':
                                        [
                                                  {
                                                  "FieldName": "TaxName",
                                                  "SearchOperator": "Equals",
                                                  "SearchValue": self.name
                                                  },
                                        ]
                              }
                              self.taxDetails = MegavenApi.getTaxInfo(filters)
                              self.taxDetails = self.taxDetails.json()
                              # Could make a search conditional similar to setSupplierDetails method and set all or as required values from the response object
                              self.taxID = self.taxDetails['mvTaxes'][0]['TaxID']
                              
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

          def getTaxID(self):
                    return self.taxID 

                    