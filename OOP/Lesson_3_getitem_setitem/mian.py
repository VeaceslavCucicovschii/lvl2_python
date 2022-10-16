from os import system
import Classes

system('cls')

stock = Classes.Stock()

stock.add(Classes.Product("Iphone XV", 1000.00, 15))
stock.add(Classes.Product("Iphone XIV", 900.00, 10))
stock.add(Classes.Product("Iphone XIII", 800.00, 5))

stock[2] = Classes.Product("Iphone XIV", 950.00, 20)
print(stock[2])

# # test the initial stock
# for p in stock.products:
#     print(p)
# print()

# client = Classes.Client("John Doe", "Unknown Str. 99")
# client.bag = Classes.Bag()

# p1 = Classes.Product("Iphone XV", 1000.00, 2)
# p1.id = stock.products[0].id

# client.bag.products.append(p1)
# stock.products[0].quantity -= 2

# # test the stock after purchase
# for p in stock.products:
#     print(p)
# print()

# # test the bag after purchase
# for p in client.bag.products:
#     print(p)
# print()
