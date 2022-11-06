from Product import Product

prod = []

for i in range(0, 10):
    prod.append(Product(i+1, f"Product {i+1}"))
    prod[i].save()

prod[0].delete()

prod[1].name = "Product two"
prod[1].update()

p = prod[3] # acesta este find :)