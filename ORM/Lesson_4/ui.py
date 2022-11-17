from Product import Product
from Money import Money
from Stock import Stock
from Client import Client
from Contact import Contact
from Bag import Bag
from BagItems import BagItems
from Model import id

def printMainMenu():
    print('#' * 60)
    print("""
        1. show catalog
        2. add to bag
        3. show bag
    """)
    print('#' * 60)

    option = int(input('\n>>> '))
    return option

def addToBag(client_id):
    bag = Bag.findByClientId(client_id)
    
    if bag == None:
        cost = Money(id(), 0, 'EUR')
        cost.save()
        bag = Bag(id(), cost.id, client_id)
        bag.save()

    product_id = int(input("\nEnter Product id >>> "))
    bag_item_quantity = int(input("Enter how many of those products you want >>> "))

    s = Stock.findByProdId(product_id)
    if bag_item_quantity > s.quantity:
        print(f"We dont have as many products, we have only {s.quantity}")
        return 0

    bag_item = BagItems(id(), bag.id, product_id, bag_item_quantity)
    bag_item.save()

    bag.cost.amount += bag_item.product.price.amount * bag_item_quantity
    bag.cost.update()

    Stock.decreaseQuantityByProdId(product_id, bag_item_quantity)
    print("Product added successfully !")

    
def printBag(bag_id):
    bag_items = BagItems.findAllByBag(bag_id)
    
    print()
    print('#' * 120, '\n')
    for row in bag_items:
        row.printForClient()

    bag = Bag.find(bag_id)
    print("\nClient bag total cost =", bag.cost.amount, '\n')
    print('#' * 120)
    


def printCatalog():
    products = Product.findAll()

    print()
    print('#' * 120, '\n')
    for row in products:
        row.printForClient()
    print()
    print('#' * 120)
