from Address import Address 


class Contact:

          contactId = 0 
          def __init__(self, _name, _contactType,isPrimary=False, **contactdetails):
                    self.name= _name
                    self.contactType = _contactType
                    self.id = self.contactId
                    self.isPrimary= isPrimary
                    Contact.contactId += 1
                    
                    for key,value in contactdetails.items():
                                       
                                        if key=='email':
                                                  self.email = value
                                                  
                                        elif key=='phone':
                                                  self.phone = value
                                        elif key=='address':
                                                  self.address = Address(value,self.contactType)
                                        else:
                                                  continue           
                                          

          # getters
          def getContactAddress(self):
                    return self.address.getAddressLocation()
          def getContactName(self):
                    
                    return self.name
          
          def getContactPhone(self):
                    return self.phone
          
          def getContactType(self):
                    return self.contactType
          
          def getContactId(self):
                    return self.id
          
          def getContactEmail(self):
                    return self.email
          
         
       
