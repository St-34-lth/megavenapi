class Contact:
          
          
          def __init__(self, _name, _address, _type, _phone="" ):
                    self.name= _name
                    self.phone = _phone 
                    self.address= _address
                    self.type = _type 
                   
          def getName(self):
                    return self.name
          
          def getPhone(self):
                    return self.phone
          
          def getAddress(self):
                    return self.address
          
         
          # define setters
          def setName(self,name):
              self.name = name 
              

          def setPhone(self,phone):
                    self.phone = phone

          def setAddress(self,address):
                    self.address = address
          