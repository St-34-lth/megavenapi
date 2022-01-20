from Discount import Discount
from Tax import Tax
from Contact import Contact, Address
from MegavenApi import MegavenApi
from Product import Product
# test = Discount('loyalty', 20, 'llt', 'for loyal')
# print(test.getName())
# print(test.getDiscountedPrice(200))


# create the API client instance
mtest = MegavenApi('2795d72f4d21ccdf@m128003')


# insert new contact 
# babis = Contact('babis', 3, 'Example 8, Athens', 'person',
#                 phone=' 1235698967',email='babis@exampletest.com',)

# output = mtest.contactPersonUpdate(babis)
# print(output.text)

# c. Inventory Location:

# Abbreviation: Test
# Name: Test Project Location
# Address: Example 20, Athens


item = Contact('Test Project Location', 1,
               'Example 20, Athens', 'item', abbrvn='Test')


# print(babis.getPhone(),babis.getEmail())

# response = mtest.inventoryLoc(item)
# print(response.text)


#Make the tax object


# d. Tax:

# Name: VAT
# Description: VAT GR
# Value: 24%
t = Tax('vat',24,'VAT GR')
d = Discount('loyalty',10,'llt')
# print(t.getName(),t.getDescription(),t.getValue())
mtest.updateDiscount(d,'Insert')
mtest.updateTax(t,'Insert')