# requires:
# orderId, orderno, orderstatus if orderInventorylocationID, clientid

class Sale:
         
          saleId=0
          
          def __init__(self,product,client,qty):
                    self.product = product 
                    self.client = client 
                    self.qty = qty
                    Sale.saleId+=1  

          
                    
            
          
          
          