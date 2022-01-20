
# list of contact objects
class SupplierClient:

          def __init__(self, name, type, addresses, contacts):
                    self.contacts =contacts 
                    self.addressess = addresses 
                    self.name = name 
                    self.type = type 
          
          
          def getName(self):
                    return self.name
          def getType(self):
                    return self.type
          
          def getContacts(self):
                    return self.contacts
                    
          def getAddresses(self):
                    return self.addressess
