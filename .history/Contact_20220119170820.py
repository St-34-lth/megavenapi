from Address import Address 


class Contact:

          def __init__(self, _name, _id, _contactType, **contactdetails):
                    self.name= _name
                    self.contactType = _contactType
                    self.id = _id

                    # if _contactType=='person':
                    #           self.address = Address(_address,"shipping")
                              
                    # elif _contactType=='item':
                    #           self.address = Address(_address,'item location',contactdetails['abbrvn'])
                               
                    # else:
                    #           pass
                    
                    for key,value in contactdetails.items():
                                       
                                        if key=='email':
                                                  self.email = value
                                                  
                                        elif key=='phone':
                                                  self.phone = value

                                        else:
                                                  continue           
                                          

          # getters

          def getName(self):
                    
                    return self.name
          
          def getPhone(self):
                    return self.phone
          
          def getContactType(self):
                    return self.contactType
          
          def getId(self):
                    return self.id
          
          def getEmail(self):
                    return self.email
          
         
                    
                    