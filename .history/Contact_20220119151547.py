from Address import Address 


class Contact:

          def __init__(self, _name, _id,_address, _contactType, **contactdetails):
                    self.__name= _name
                    self.__type = _contactType
                    self.__id = _id
                   
                    if _contactType=='person':
                              self.address = Address(_address,"shipping")
                              
                    elif _contactType=='item':
                              self.address = Address(_address,'item location',contactdetails['abbrvn'])
                               
                    else:
                              pass
                    
                    for key,value in contactdetails.items():
                                       
                                        if key=='email':
                                                  self.__email = value
                                                  
                                        elif key=='phone':
                                                  self.__phone = value
                                                
                                        else:
                                                  continue           
                                          

          # getters
          def getAbbrvn(self):
                    if self.address.type=='item':
                              abbrvn = self.address.abbrvn
                              return abbrvn
                    else:
                              pass
                     
          def getAddressType(self):
                    return self.address.type
          
          def getName(self):
                    
                    return self.__name
          
          def getPhone(self):
                    return self.__phone
          
          def getAddress(self):
                    return self.address.location
          
          def getType(self):
                    return self.__type
          
          def getId(self):
                    return self.__id
          def getEmail(self):
                    return self.__email
          
          # setters
          # def setName(self,name):
          #           self.__name = name 
              
          # def setPhone(self,phone):
          #           self.__phone = phone

          # def setAddress(self,address):
          #           self.__address = address
                    
          # def setAddressType(self,addressType):
          #           self.__addressType = addressType
                    
          # def setEmail(self,email):
          #           self.__email = email
                    
                    