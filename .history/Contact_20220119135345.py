class Contact:

          def __init__(self, _name, _id,_address,_addressType, _contactType, _phone="" ,_email=""):
                    self.__name= _name
                    self.__phone = _phone 
                    self.__address= _address
                    self.__addressType = _addressType
                    self.__type = _contactType
                    self.__id = _id
                    self.__email= _email
                         

          
          # getters
          def getAddressType(self):
                    return self.__addressType
          
          def getName(self):
                    return self.__name
          
          def getPhone(self):
                    return self.__phone
          
          def getAddress(self):
                    return self.__address
          
          def getType(self):
                    return self.__type
          
          def getId(self):
                    return self.__id
          def getEmail(self):
                    return self.__email
          
          # setters
          def setName(self,name):
                    self.__name = name 
              
          def setPhone(self,phone):
                    self.__phone = phone

          def setAddress(self,address):
                    self.__address = address
                    
          def setAddressType(self,addressType):
                    self.__addressType = addressType
                    
          def setEmail(self,email):
                    self.__email = email