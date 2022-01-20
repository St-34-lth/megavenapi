
# list of contact objects
class Supplier:

          def __init__(self, name, type, addresses, contacts,):
                    self.contacts =contacts 
                    self.addressess = addresses 
                    self.name = name 
                    self.type = type 
          
          
          def getName(self);
                    return self.name
          def getType(self):
                    return self.type
          
          def getContacts(self):
                    contactsDict = dict()
                    for i in self.contacts:
                              key = self.contacts[i].getName()
                              value = self.contacts[i]
                              contactsDict[key]=value
                    return contactsDict
                    