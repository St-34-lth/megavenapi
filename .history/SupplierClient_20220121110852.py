from urllib.error import HTTPError
from MegavenApi import MegavenApi
import json 
import requests 
# A class to hold all data related to a SupplierClient in the megaventory API.
# Its makeSupplierClient method registers the client with the API and its setSupplierClientInfo gets the associated data from the API if required.
# On a side note, I could just save the response once the registry is performed. 
class SupplierClient:

          
          def __init__(self, name, type, addresses, contacts):
                    
                    self.contacts =contacts
                    self.addressess = addresses 
                    self.name = name 
                    self.type = type 
                    for contact in contacts:
                              if contact.isPrimary:
                                        self.primaryContact = contact 
                              else:
                                        self.primaryContact= contact[0] 
          
          def getSupplierPrimaryContact(self):
                    return self.primaryContact;        
          
          def makeSupplierClient(self,action):
                    MegavenApi.insertSupplierClient(self, action)
        
          def setSupplierClientInfo(self,searchByName=False):
                    if searchByName:
                              try:
                                        filters = {'Filters':
                                                  [
                                                            {
                                                                      'FieldName': "SupplierClientName",
                                                                      'SearchOperator': "Equals",
                                                                      "SearchValue": self.name
                                                            }
                                                  ]
                                        }
                                        response = MegavenApi.getSupplierClientInfo(self,filters)
                                        
                                        self.supplierClientInfo = response.json()
                                        self.supplierClientId = self.supplierClientInfo['mvSupplierClients'][0]['SupplierClientID']
                                        
                              except HTTPError or ConnectionError or ValueError:
                                        print('failed to get info from API')
                    else:
                         print('specify appropriate filters')     
                
          def getSupplierClientID(self):
                    return self.supplierClientId
          def getSupplierClientName(self):
                    return self.name
          def getSupplierClientType(self):
                    return self.type     
               
          def getSupplierClientContacts(self):
                    return self.contacts
                    
          def getSupplierClientAddresses(self):
                    return self.addressess

          def getSupplierBillingAddress(self):
                    for address in self.addressess:
                              if address.getAddressType()=='billing':
                                        return address.getAddressLocation()
          def getSupplierShippingAddress(self):
                    for address in self.addressess:
                              if address.getAddressType()=='shipping':
                                        return address.getAddressLocation()