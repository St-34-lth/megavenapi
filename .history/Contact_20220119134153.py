class Contact:
          
          
          
         
          def __init__(self, _name, _id,_address, _type, _phone="" ):
                    self.__name= _name
                    self.__phone = _phone 
                    self.__address= _address
                    self.__type = _type 
                    self.__id = _id
                         

          
          # getters
          def getName(self):
                    return self.__name
          
          def getPhone(self):
                    return self.__phone
          
          def getAddress(self):
                    return self.__address
          
          def getType(self):
                    return self.__type
          def getId(self)
                    return self.__id
          # setters
          def setName(self,name):
                    self.__name = name 
              
          def setPhone(self,phone):
                    self.__phone = phone

          def setAddress(self,address):
                    self.__address = address
          