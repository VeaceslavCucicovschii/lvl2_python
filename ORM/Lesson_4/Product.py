from Money import Money
from Model import Model
import psycopg2

class Product(Model):
    def __init__(self, id, name, price_id):
        Model.__init__(self, id)
        self.name = name
        self.price_id = price_id
        self.price = Money.find(price_id)

    def findAllByName(keyword):
        sql = f""" 
        SELECT * FROM "products"
        WHERE name LIKE '%{keyword}%'; """
        
        p = []
        results = Product.connectAndExecute(sql, True)

        for row in results:
            p.append(Product(*row))

        return p

    def findAllByPriceRange(min, max):
        sql = f""" 
        SELECT * FROM "products" JOIN "money"
        ON "products".price_id = "money".id
        WHERE amount >= {min} AND amount <= {max}; """

        p = []
        results = Product.connectAndExecute(sql, True)

        for row in results:
            p.append(Product(*row))

        return p

    def findAll():
        sql = f""" SELECT * FROM "products"; """

        p = []
        results = Product.connectAndExecute(sql, True)

        for row in results:
            p.append(Product(*row))

        return p

    def find(id):
        sql = f""" SELECT * FROM "products" WHERE id = {id}; """

        result = Product.connectAndExecute(sql, True)[0]

        p = Product(*result)
        m = Money.find(result[2])
        p.price = m
        return p

    def save(self):
        sql = f""" 
        BEGIN;
        INSERT INTO "products" VALUES   ({self.id}, '{self.name}', 1);
        COMMIT; """

        Product.connectAndExecute(sql)
    
    def delete(self):
        sql = f""" 
        BEGIN;
        DELETE FROM "products" WHERE id = {self.id};
        COMMIT; """

        Product.connectAndExecute(sql)

    def update(self):
        sql = f""" 
        BEGIN;
        UPDATE "products"
        SET name = '{self.name}', price_id = {self.price_id}
        WHERE id = {self.id};
        COMMIT; """

        Product.connectAndExecute(sql)

    def printForClient(self):
        from Stock import Stock
        s = Stock.findByProdId(self.id)
        print(f"Product < name = {self.name:15} stock quantity = {s.quantity:<10} price = {self.price.amount:<10} currency = {self.price.currency:3} >")

    def __str__(self):
        return f"Product <id = {self.id}, name = {self.name}, {self.price}>"

    def __repr__(self):
        return self.__str__()