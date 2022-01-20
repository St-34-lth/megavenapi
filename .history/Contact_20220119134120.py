class Contact:
          
          
          
         
          def __init__(self, _name, _id,_address, _type, _phone="" ):
                    self.__name= _name
                    self.__phone = _phone 
                    self.__address= _address
                    self.__type = _type 
                    self.__id = _id
                         

          
          # getters
          def getName(self):
                    return self._name
          
          def getPhone(self):
                    return self._phone
          
          def getAddress(self):
                    return self._address
          
          def getType(self):
                    return self._type
          
          # setters
          def setName(self,name):
                    self._name = name 
              

          def setPhone(self,phone):
                    self._phone = phone

          def setAddress(self,address):
                    self._address = address
          