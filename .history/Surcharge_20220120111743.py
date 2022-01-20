class Surcharge:
         
          def __init__(self,name,value):
                    self.name = name 
                    self.value = float(value)

          @staticmethod
          def getSurchargedPrice(value,priceBeforeSurcharge):
              return priceBeforeSurcharge*(value/100)
       
