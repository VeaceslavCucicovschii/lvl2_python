from Money import Money
import psycopg2

class Product:
    def __init__(self, id, name, price_id):
        self.id = id
        self.name = name
        self.price_id = price_id
        self.price = Money.find(price_id)

    def findAll():
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" SELECT * FROM "products"; """

        cursor = conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        p = []

        for row in result:
            p.append(Product(row[0], row[1], row[2]))

        return p

    def find(id):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" SELECT * FROM "products" WHERE id = {id}; """

        cursor = conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchone()
        p = Product(result[0], result[1], result[2])
        m = Money.find(result[2])
        p.price = m
        return p

    def save(self):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" 
        BEGIN;
        INSERT INTO "products" VALUES   ({self.id}, '{self.name}', 1);
        COMMIT; """

        cursor = conn.cursor()
        cursor.execute(sql)
    
    def delete(self):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" 
        BEGIN;
        DELETE FROM "products" WHERE id = {self.id};
        COMMIT; """

        cursor = conn.cursor()
        cursor.execute(sql)

    def update(self):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" 
        BEGIN;
        UPDATE "products"
        SET name = '{self.name}'
        WHERE id = {self.id};
        COMMIT; """

        cursor = conn.cursor()
        cursor.execute(sql)

    def __str__(self):
        return f"Product <{self.id}, {self.name}, {self.price_id}, {self.price}>"