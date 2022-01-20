from Discount import Discount
from Tax import Tax
from Supplier import SupplierClient
from Contact import Contact, Address
from MegavenApi import MegavenApi
from Product import Product
from SalesOrder import Sale
# test = Discount('loyalty', 20, 'llt', 'for loyal')
# print(test.getName())
# print(test.getDiscountedPrice(200))


# create the API client instance
url = "https://api.megaventory.com/v2017a/"
apikey = '2795d72f4d21ccdf@m128003'
mtest = MegavenApi(apikey,url)


# insert new contact 
babis = Contact('notBabis2','person',
                phone='1235698967',email='notBabis2@exampletest.com')

# output = mtest.contactPersonUpdate(babis)
# print(output.text)




item = Contact('Test Project Location','item', abbrvn='Test')


# print(babis.getPhone(),babis.getEmail())

# response = mtest.inventoryLoc(item)
# print(response.text)


#Make the tax& discount objects


# d. Tax:

# Name: VAT
# Description: VAT GR
# Value: 24%
# t = Tax('vat',24,'VAT GR')

# # e. Discount

# # Name: Loyalty
# # Description: Loyalty Customer Discount
# # Value: 50%

# d = Discount('Loyalty', 50, 'Loyalty Customer Discount')


# tresponse = mtest.updateTax(t, 'Insert')

# dresponse = mtest.updateDiscount(d,'Insert')
billingAd  = Address('Example 20, Athens','billing')
shippingAd = Address('Example 8, Athens','shipping')

s = SupplierClient('Test3','Supplier',[billingAd,shippingAd],[babis,item])
# s.setSupplierClientInfo(True)
# print(s.getSupplierClientID())

# product
# SKU: 1112256
# Description: Nike shoes
# Sales Price: 99.99
# Purchase Price: 44.99

#Inventory Location:

# Abbreviation: Test
# Name: Test Project Location
# Address: Example 20, Athens

p = Product('Nike shoes',44.99,99.99,'1112256')
# p.setProductLocation('Example 20, Athens','Test Project Location')

t = Tax('vat',24.0,'Greek VAT')
d = Discount("Loyalty",50.0,'llt')
sale = Sale(p,s,1,t,d,1,'Example 20, Athens','Test Project Location')
# ins = mtest.insertSupplierClient(s,'Insert')
# print(ins)
# out = mtest.getSupplierClientInfo(s)
res = mtest.makeSalesOrder('Insert',sale)
res = res.json()
print(res)