import psycopg2

class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name

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
