from Helpers import id


class Identifiable:
    def __init__(self):
        self.id = id()


class Client (Identifiable):
    def __init__(self, fullName, physicalAdress):
        Identifiable.__init__(self)
        self.fullName = fullName
        self.physicalAdress = physicalAdress
        self.bag = None


class Product (Identifiable):
    def __init__(self, name, price, quantity):
        Identifiable.__init__(self)
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product (id: {self.id}, name: {self.name}, price: {self.price}, quantity: {self.quantity})"


class Stock:
    def __init__(self):
        self.products = []

    def add(self, product):
        if type(product) == Product:
            self.products.append(product)

    def __getitem__(self, key):
        return self.products[key]

    def __setitem__(self, key, new_value):
        self.products[key] = new_value


class Bag:
    def __init__(self):
        self.products = []
