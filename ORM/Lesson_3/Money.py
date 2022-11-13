import psycopg2

class Money:
    def __init__(self, id, amount, curency):
        self.id = id
        self.amount = amount
        self.curency = curency

    def connectAndExecute(sql, returns = False):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        cursor = conn.cursor()
        cursor.execute(sql)

        if returns:
            results = cursor.fetchall()
            return results

    def find(id):
        sql = f""" SELECT * FROM "money" WHERE id = {id}; """

        result = Money.connectAndExecute(sql, True)[0]

        m = Money(result[0], result[1], result[2])
        return m

    def save(self):
        sql = f""" 
        BEGIN;
        INSERT INTO "money" VALUES   ({self.id}, {self.amount}, '{self.curency}');
        COMMIT; """

        Money.connectAndExecute(sql)
    
    def delete(self):
        sql = f""" 
        BEGIN;
        DELETE FROM "money" WHERE id = {self.id};
        COMMIT; """

        Money.connectAndExecute(sql)

    def update(self):
        sql = f""" 
        BEGIN;
        UPDATE "money"
        SET amount = {self.amount}, curency = '{self.curency}'
        WHERE id = {self.id};
        COMMIT; """

        Money.connectAndExecute(sql)

    def __str__(self):
        return f"Money <{self.id}, {self.amount}, {self.curency}>"