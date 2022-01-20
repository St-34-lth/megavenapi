
# list of contact objects
class SupplierClient:

          
          def __init__(self, name, type, addresses, contacts):
                    
                    self.contacts =contacts
                    self.addressess = addresses 
                    self.supplierClientInfo
                    
                    self.name = name 
                    self.type = type 
                    
                    self.supplierClientId
                    
                    
          
          def setSupplierClientInfo(self,response):
                    self.supplierClientInfo = response
                    self.supplierClientId = response['mvSupplierClients'][0]['SupplierClientID']
                    
                    
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
