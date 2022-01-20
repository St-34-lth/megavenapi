from Discount import Discount
from Tax import Tax
from Supplier import SupplierClient
from Contact import Contact, Address
from MegavenApi import MegavenApi
from Product import Product
# test = Discount('loyalty', 20, 'llt', 'for loyal')
# print(test.getName())
# print(test.getDiscountedPrice(200))


# create the API client instance
url = "https://api.megaventory.com/v2017a/"
apikey = '2795d72f4d21ccdf@m128003'
mtest = MegavenApi(apikey,url)


# insert new contact 
babis = Contact('babis', 3, 'person',
                phone='1235698967',email='babis@exampletest.com')

# output = mtest.contactPersonUpdate(babis)
# print(output.text)

# c. Inventory Location:

# Abbreviation: Test
# Name: Test Project Location
# Address: Example 20, Athens


item = Contact('Test Project Location', 1, 'item', abbrvn='Test')


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

s = SupplierClient('TestSupplier','supplier',[billingAd,shippingAd],[babis,item])
mtest