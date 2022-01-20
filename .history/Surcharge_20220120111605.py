class Surcharge:
         
          def __init__(self,_name,_value):
                    self._name = _name 
                    self._value = float(_value)


          def getSurchargedPrice(value,priceBeforeSurcharge):
              return priceBeforeSurcharge*(value/100)
       
