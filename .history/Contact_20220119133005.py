class Contact:
                   
          contact_id = 0
          def __init__(self, _name, _address, _type, _phone="" ):
                    self._name= _name
                    self._phone = _phone 
                    self._address= _address
                    self._type = _type 
                    self._id = self.contact_id
                    self.contact_id+=1 

          
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
          