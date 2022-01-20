class Address:

          def __init__(self,address,addressType,abbrvn=''):
                    self.address = address 
                    self.addressType = addressType
                    self.abbrvn = abbrvn 
          
          def getAddressLocation(self):
                    return self.address
          
          def getAddressType(self):
                    return self.addressType
                     
          def getAbbrvn(self):
                    return self.abbrvn 