from Model import Model
from Product import Product
import psycopg2

class Stock(Model):
    def __init__(self, id, prod_id, quantity):
        Model.__init__(self, id)
        self.prod_id = prod_id
        self.prod = Product.find(prod_id)
        self.quantity = quantity

    def increaseQuantityByProdId(id, nr):
        s = Stock.find(id)
        s.quantity += nr
        s.update()

    def decreaseQuantityByProdId(id, nr):
        s = Stock.find(id)
        s.quantity -= nr
        s.update()

    def findByProdId(id):
        sql = f""" SELECT * FROM "stock" WHERE product_id = {id}; """

        result = Stock.connectAndExecute(sql, True)[0]
    
        s = Stock(*result)
        p = Product.find(result[1])
        s.prod = p
        return s

    def find(id):
        sql = f""" SELECT * FROM "stock" WHERE id = {id}; """

        result = Stock.connectAndExecute(sql, True)[0]
    
        s = Stock(*result)
        p = Product.find(result[1])
        s.prod = p
        return s

    def save(self):
        sql = f""" 
        BEGIN;
        INSERT INTO "stock" VALUES ({self.id}, {self.prod_id}, {self.quantity});
        COMMIT; """

        Stock.connectAndExecute(sql)
    
    def delete(self):
        sql = f""" 
        BEGIN;
        DELETE FROM "stock" WHERE id = {self.id};
        COMMIT; """

        Stock.connectAndExecute(sql)

    def update(self):
        sql = f""" 
        BEGIN;
        UPDATE "stock"
        SET product_id = '{self.prod_id}', quantity = {self.quantity}
        WHERE id = {self.id};
        COMMIT; """

        Stock.connectAndExecute(sql)

    def __str__(self):
        return f"Stock <{self.id}, {self.prod_id}, {self.prod}, {self.quantity}>"

    def __repr__(self):
        return self.__str__()