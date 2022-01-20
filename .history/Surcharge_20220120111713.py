class Surcharge:
         
          def __init__(self,_name,_value):
                    self.name = _name 
                    self.value = float(_value)


          def getSurchargedPrice(value,priceBeforeSurcharge):
              return priceBeforeSurcharge*(value/100)
       
