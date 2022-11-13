from Product import Product
from Money import Money
from Stock import Stock
from Client import Client
from Contact import Contact
from Bag import Bag
from BagItems import BagItems
from os import system

system('cls')

b = Bag.findByClientId(2)
print(b)