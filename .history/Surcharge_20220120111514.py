class Surcharge:
         
          def __init__(self,_name,_value):
                    self._name = _name 
                    self._value = float(_value)
              
          def getName(self):
                    return self._name
          
          def getValue(self):
                    return self._value
          
          def setValue(self,value):
                    self._value = value
          
          
         
          def getSurchargedPrice(value,priceBeforeSurcharge):
              return priceBeforeSurcharge*(value/100)
       
