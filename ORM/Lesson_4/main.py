from ui import *
from os import system

system('cls')

client_id = int(input("Enter client ID please >>> "))
client = Client.find(client_id)

while True:
    print("\nHello", client.fullName, '!\n')
    option = printMainMenu()
    
    if option == 1:
        printCatalog()
        input()
        system('cls')

    elif option == 2:
        addToBag(client.id)
        input()
        system('cls')
    
    elif option == 3:
        bag = Bag.findByClientId(client.id)
        printBag(bag.id)
        input()
        system('cls')