class Surcharge:
         
         
          def __init__(self,_name,_value):
                    self._name = _name 
                    self._value = _value
                    
          def getName(self):
                    return self._name
          
          def getValue(self):
                    return self._value
          
          def setValue(self,value):
                    self._value = value
          
          
          
          def getSurchargedPrice(self,priceBeforeSurcharge):
                    return priceBeforeSurcharge*(self.value/100)          
       
