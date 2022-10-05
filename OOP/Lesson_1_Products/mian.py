from os import system
from datetime import datetime
import random

system('cls')


def id():
    # date + time
    time_now = datetime.now()
    created_id = time_now.strftime("%Y-%m-%d-%H-%M-%S-")

    # rand number
    random_nr = random.randint(0, 999999)

    counter = 0
    aux = random_nr
    while(aux != 0):
        aux //= 10
        counter += 1

    nr_0 = 6 - counter
    created_id += '0'*nr_0
    created_id += str(random_nr)

    return created_id


class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name


products_list = []
name_list = ["pizza", "juice", "apple"]

# create 100 Products
for i in range(100):
    products_list.append(Product(id(), name_list[random.randint(0, 2)]))

# test if products id are different
test = True
for i in range(100):
    for j in range(i+1, 100):
        if products_list[i] == products_list[j]:
            test = False
            break

if test == True:
    print("ID generation test passed")
else:
    print("ID generation test failed")
