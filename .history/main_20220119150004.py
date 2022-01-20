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

print(item.address.abbrvn)
# print(babis.getPhone(),babis.getEmail())