from Model import Model
import psycopg2

class Client(Model):
    def __init__(self, id, fullName, isVip = False):
        Model.__init__(self, id)
        self.fullName = fullName
        self.isVip = isVip

    def findAllByEmail(keyword):
        sql = f"""
        SELECT * FROM "contacts"
        WHERE emailadress LIKE '%{keyword}%'; """
        
        result = Client.connectAndExecute(sql, True)[0]

        return Client.find(result[3])

    def findAllByName(keyword):
        sql = f"""
        SELECT * FROM "clients"
        WHERE fullname LIKE '%{keyword}%'; """
        
        n = []
        results = Client.connectAndExecute(sql, True)

        for row in results:
            n.append(Client(*row))

        return n

    def find(id):
        sql = f""" SELECT * FROM "clients" WHERE id = {id}; """

        result = Client.connectAndExecute(sql, True)[0]
    
        c = Client(*result)
        return c

    def save(self):
        sql = f""" 
        BEGIN;
        INSERT INTO "clients" VALUES ({self.id}, {self.fullName}, {self.isVip});
        COMMIT; """

        Client.connectAndExecute(sql)
    
    def delete(self):
        sql = f""" 
        BEGIN;
        DELETE FROM "clients" WHERE id = {self.id};
        COMMIT; """

        Client.connectAndExecute(sql)

    def update(self):
        sql = f""" 
        BEGIN;
        UPDATE "clients"
        SET fullName = '{self.fullName}', isvip = {self.isVip}
        WHERE id = {self.id};
        COMMIT; """

        Client.connectAndExecute(sql)

    def __str__(self):
        return f"Client <{self.id}, {self.fullName}, {self.isVip}>"

    def __repr__(self):
        return self.__str__()