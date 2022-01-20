from Discount import Discount
from Tax import Tax
from SupplierClient import SupplierClient
from Contact import Contact, Address
from MegavenApi import MegavenApi
from Product import Product
from SalesOrder import Sale


# create the API client instance
url = "https://api.megaventory.com/v2017a/"
apikey = '2795d72f4d21ccdf@m128003'
mtest = MegavenApi(apikey,url)


# insert new contact 
babis = Contact('babis2','person',isPrimary=True,
                phone='1235698967', email='Babis2@exampletest.com', address='Example 20, Athens')


#Make the tax & discount objects
t = Tax('vat', 24.0, 'Greek VAT')
d = Discount("Loyalty", 50.0, 'llt')


#Create addresses

billingAd = Address('Example 20, Athens', 'billing')
shippingAd = Address('Example 8, Athens','shipping')

s = SupplierClient('Babis2','client',[billingAd,shippingAd],[babis])
# s.makeSupplierClient('InsertOrUpdate')

p = Product('Nike shoes',44.99,99.99,'1112256')


# Insert product, product location and set inventory stock if required
 
# p.setProductLocation('Example 20, Athens', 'Test Project Location')
# p.updateProduct('Insert');
# MegavenApi.setInventoryLocationStock(p,10,'Insert')



# create the sale order 
sale = Sale(p,s,1,t,d,1,'Example 20, Athens','Test Project Location')
# register the sale
sale.makeSalesOrder('Insert')





