from Address import Address 


class Contact:

          def __init__(self, _name, _id,_address, _contactType, _phone="" ,_email="",_abbrvn=''):
                    self.__name= _name
                    self.__phone = _phone 
                    if _contactType=='person':
                              self.__address = Address(_address,"shipping")
                    elif _contactType=='item':
                              self.__address = Address(_address,'item location',_abbrvn) 
                    else:
                              pass
                    self.__type = _contactType
                    self.__id = _id
                    self.__email= _email

          # getters
          def getAbbrvn(self):
                    if _contactType=='item':
                              return self.__address.abbrvn
                    else:
                              pass 
          def getAddressType(self):
                    return self.__address.type
          
          def getName(self):
                    return self.__name
          
          def getPhone(self):
                    return self.__phone
          
          def getAddress(self):
                    return self.__address.location
          
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
                    
                    