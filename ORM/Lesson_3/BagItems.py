from Bag import Bag
from Product import Product
import psycopg2

class BagItems:
    def __init__(self, id, bag_id, product_id, quantity):
        self.id = id
        self.bag_id = bag_id
        self.bag = Bag.find(bag_id)
        self.product_id = product_id
        self.product = Product.find(product_id)
        self.quantity = quantity

    def connectAndExecute(sql, returns = False):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        cursor = conn.cursor()
        cursor.execute(sql)

        if returns:
            results = cursor.fetchall()
            return results

    def find(id):
        sql = f""" SELECT * FROM "bags_items" WHERE id = {id}; """

        result = BagItems.connectAndExecute(sql, True)[0]
    
        b = Bag(*result)

        bg = Bag.find(result[1])
        b.bag = bg
        
        prd = Product.find(result[2])
        b.product = prd
        
        return b

    def save(self):
        sql = f""" 
        BEGIN;
        INSERT INTO "bags_items" VALUES ({self.id}, {self.bag_id}, {self.product_id}, {self.quantity});
        COMMIT; """

        BagItems.connectAndExecute(sql)
    
    def delete(self):
        sql = f""" 
        BEGIN;
        DELETE FROM "bags_items" WHERE id = {self.id};
        COMMIT; """

        BagItems.connectAndExecute(sql)

    def update(self):
        sql = f""" 
        BEGIN;
        UPDATE "bags_items"
        SET bag_id = '{self.bag_id}', product_id = {self.product_id}, quantity {self.quantity}
        WHERE id = {self.id};
        COMMIT; """

        BagItems.connectAndExecute(sql)

    def __str__(self):
        return f"Bag <{self.id}, {self.bag_id}, {self.bag}, {self.product_id}, {self.product}, {self.quantity}>"

    def __repr__(self):
        return self.__str__()