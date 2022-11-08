import psycopg2

class Money:
    def __init__(self, id, amount, curency):
        self.id = id
        self.amount = amount
        self.curency = curency

    def find(id):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" SELECT * FROM "money" WHERE id = {id}; """

        cursor = conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchone()
        m = Money(result[0], result[1], result[2])
        return m

    def save(self):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" 
        BEGIN;
        INSERT INTO "money" VALUES   ({self.id}, {self.amount}, '{self.curency}');
        COMMIT; """

        cursor = conn.cursor()
        cursor.execute(sql)
    
    def delete(self):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" 
        BEGIN;
        DELETE FROM "money" WHERE id = {self.id};
        COMMIT; """

        cursor = conn.cursor()
        cursor.execute(sql)

    def update(self):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        sql = f""" 
        BEGIN;
        UPDATE "money"
        SET amount = {self.amount}, curency = '{self.curency}'
        WHERE id = {self.id};
        COMMIT; """

        cursor = conn.cursor()
        cursor.execute(sql)

    def __str__(self):
        return f"Money <{self.id}, {self.amount}, {self.curency}>"