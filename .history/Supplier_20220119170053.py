
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
                    contactsDict = dict()
                    for i in range(len(self.contacts)-1):
                              print(self.contacts[i])
                              key = self.contacts[i].getName()
                              value = self.contacts[i]
                              contactsDict[key]=value
                    return contactsDict
          
          def getAddresses(self):
                    addressesDict = dict()
                    for i in range(len(self.contacts)-1):
                              print(self.addressess[i])
                              key = self.addressess[i].getAddressType()
                              value = self.addressess[i]
                              addressesDict[key] = value
                    return addressesDict
