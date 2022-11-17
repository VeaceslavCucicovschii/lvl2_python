from Bag import Bag
from Product import Product
from Model import Model
import psycopg2

class BagItems(Model):
    def __init__(self, id, bag_id, product_id, quantity):
        Model.__init__(self, id)
        self.bag_id = bag_id
        self.bag = Bag.find(bag_id)
        self.product_id = product_id
        self.product = Product.find(product_id)
        self.quantity = quantity

    def findAllByBag(id):
        sql = f""" SELECT * FROM "bags_items" WHERE bag_id = {id}; """

        b = []
        results = BagItems.connectAndExecute(sql, True)

        for row in results:
            b.append(BagItems(*row))

        return b

    def find(id):
        sql = f""" SELECT * FROM "bags_items" WHERE id = {id}; """

        result = BagItems.connectAndExecute(sql, True)[0]
    
        b = BagItems(*result)

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

    def printForClient(self):
        print(f"""Bag_item < owner = {self.bag.client.fullName:15} product name = {self.product.name:15} quantity = {self.quantity:<5} product cost = {self.product.price.amount * self.quantity:<10} currency = {self.bag.cost.currency:3} >""")

    def __str__(self):
        return f"Money <id = {self.id}, bag = {self.bag}, product = {self.product}, quantity = {self.quantity}>"

    def __repr__(self):
        return self.__str__()