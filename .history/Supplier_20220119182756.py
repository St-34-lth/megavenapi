
# list of contact objects
class SupplierClient:

          def __init__(self, name, type, addresses, contacts):
                    self.contacts =contacts
                    print(contacts) 
                    self.addressess = addresses 
                    self.name = name 
                    self.type = type 
          
          
          def getSupplierClientName(self):
                    return self.name
          def getSupplierClientType(self):
                    return self.type
          
          def getSupplierClientContacts(self):
                    return self.contacts
                    
          def getSupplierClientAddresses(self):
                    return self.addressess

          def getSupplierBillingAddress(self):
                    for address in self.addresses:
                              if address.getAdressType()=='billing':
                                        return address.getAddress()
          def getSupplierShippingAddress(self):
                    for address in self.addresses:
                              if address.getAdressType()=='shipping':
                                        return address.getAddress()
