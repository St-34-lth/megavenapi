# requires:
# orderId, orderno, orderstatus if orderInventorylocationID, clientid

class Sale:
         
          saleId=0
          SaleOrderNo=0

          def __init__(self, product, client, qty, tax, discount):
                    self.product = product 
                    self.client = client 
                    self.qty = qty
                    
                    self.id = self.saleId
                    Sale.saleId+=1
                    
                    self.saleOrderNo=str(self.SaleOrderNo)
                    Sale.SaleOrderNo+=1
          
          
                    
            
          
          
          