class Client:
    def __init__(self, id, fullName, physicalAdress):
        self.id = id
        self.setFullName(fullName)
        self.setPhysicalAdress(physicalAdress)

    def getFullName(self):
        return self.__fullName

    # "fullName" ENCAPSULATION:
    def setFullName(self, fullName):
        space_counter = 0

        if fullName[0] != ' ' and fullName[len(fullName)-1] != ' ':
            if len(fullName) > 3:
                for i in range(len(fullName)):
                    if fullName[i] == ' ' and i > 0 and i < len(fullName)-1:
                        space_counter += 1

        if space_counter == 1:
            self.__fullName = fullName
        else:
            print("ERROR: fullName doesn't satisfy the conditions")

    def getPhysicalAdress(self):
        return self.__physicalAdress

    # "physicalAdress" ENCAPSULATION:
    def setPhysicalAdress(self, physicalAdress):
        space_counter = 0

        if physicalAdress[0] != ' ' and physicalAdress[len(physicalAdress)-1] != ' ':
            for i in range(len(physicalAdress)):
                if i > 0 and i < len(physicalAdress)-1:
                    if physicalAdress[i] == ' ' and physicalAdress[i-1] != ',':
                        space_counter += 1

        if space_counter == 1:
            self.__physicalAdress = physicalAdress
        else:
            print("ERROR: physicalAdress doesn't satisfy the conditions")


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Bag:
    def __init__(self, id, client, products):
        self.id = id
        self.client = client
        self.products = products
        self.setPrice(products)

    def getPrice(self):
        return self.__price

    def setPrice(self, products):
        price = 0

        for i in range(len(products)):
            price += products[i].price

        self.__price = price
