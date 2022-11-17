from Money import Money
from Client import Client
from Model import Model
import psycopg2

class Bag(Model):
    def __init__(self, id, cost_id, client_id):
        Model.__init__(self, id)
        self.cost_id = cost_id
        self.cost = Money.find(cost_id)
        self.client_id = client_id
        self.client = Client.find(client_id)

    def findByClientId(id):
        sql = f""" SELECT * FROM "bags" WHERE client_id = {id}; """

        results = Bag.connectAndExecute(sql, True)
        
        if(len(results) > 0):
            result = results[0]
            b = Bag(*result)

            cst = Money.find(result[1])
            b.cost = cst

            clnt = Client.find(result[2])
            b.client = clnt

            return b
        else:
            return None

    def count(self):
        sql = f""" SELECT COUNT(*) FROM "bags_items" WHERE bag_id = {self.id}; """
        
        result = Bag.connectAndExecute(sql, True)[0]
        return result[0]

    def find(id):
        sql = f""" SELECT * FROM "bags" WHERE id = {id}; """

        result = Bag.connectAndExecute(sql, True)[0]
    
        b = Bag(*result)

        cst = Money.find(result[1])
        b.cost = cst
        
        clnt = Client.find(result[2])
        b.client = clnt
        
        return b

    def save(self):
        sql = f""" 
        BEGIN;
        INSERT INTO "bags" VALUES ({self.id}, {self.cost_id}, {self.client_id});
        COMMIT; """

        Bag.connectAndExecute(sql)
    
    def delete(self):
        sql = f""" 
        BEGIN;
        DELETE FROM "bags" WHERE id = {self.id};
        COMMIT; """

        Bag.connectAndExecute(sql)

    def update(self):
        sql = f""" 
        BEGIN;
        UPDATE "bags"
        SET cost_id = '{self.cost_id}', client_id = {self.client_id}
        WHERE id = {self.id};
        COMMIT; """

        Bag.connectAndExecute(sql)

    def __str__(self):
        return f"Bag <id = {self.id}, {self.cost}, {self.client}>"

    def __repr__(self):
        return self.__str__()