from os import system
from Helpers import id
import Classes

system('cls')

client = Classes.Client(id(), "John Doe", "Chisinau, Mateevici 101")

pizza = Classes.Product(id(), "pizza", 120)
juice = Classes.Product(id(), "juice", 25)
burger = Classes.Product(id(), "burger", 45)

JhonDoe_bug = Classes.Bag(id(), client.getFullName, [pizza, juice, burger])

print(JhonDoe_bug.getPrice())
