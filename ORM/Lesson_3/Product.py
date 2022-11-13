from Money import Money
import psycopg2

class Product:
    def __init__(self, id, name, price_id):
        self.id = id
        self.name = name
        self.price_id = price_id
        self.price = Money.find(price_id)

    def connectAndExecute(sql, returns = False):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        cursor = conn.cursor()
        cursor.execute(sql)

        if returns:
            results = cursor.fetchall()
            return results

    def findAllByName(keyword):
        sql = f""" 
        SELECT * FROM "products"
        WHERE name LIKE '%{keyword}%'; """
        
        p = []
        results = Product.connectAndExecute(sql, True)

        for row in results:
            p.append(Product(row[0], row[1], row[2]))

        return p

    def findAllByPriceRange(min, max):
        sql = f""" 
        SELECT * FROM "products" JOIN "money"
        ON "products".price_id = "money".id
        WHERE amount >= {min} AND amount <= {max}; """

        p = []
        results = Product.connectAndExecute(sql, True)

        for row in results:
            p.append(Product(row[0], row[1], row[2]))

        return p

    def findAll():
        sql = f""" SELECT * FROM "products"; """

        p = []
        results = Product.connectAndExecute(sql, True)

        for row in results:
            p.append(Product(row[0], row[1], row[2]))

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

    def __str__(self):
        return f"Product <{self.id}, {self.name}, {self.price_id}, {self.price}>"

    def __repr__(self):
        return self.__str__()