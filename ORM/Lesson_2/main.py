from Product import Product
from Money import Money

p = []

p = Product.findAll()

for i in p:
    print(i)