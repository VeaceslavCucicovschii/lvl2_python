from Client import Client
import psycopg2

class Contact:
    def __init__(self, id, phonenumber, emailadress, client_id):
        self.id = id
        self.phonenumber = phonenumber
        self.emailadress = emailadress
        self.client_id = client_id
        self.client = Client.find(client_id)

    def connectAndExecute(sql, returns = False):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        cursor = conn.cursor()
        cursor.execute(sql)

        if returns:
            results = cursor.fetchall()
            return results

    def find(id):
        sql = f""" SELECT * FROM "contacts" WHERE id = {id}; """

        result = Contact.connectAndExecute(sql, True)[0]
    
        co = Contact(*result)
        cl = Client.find(result[3])
        co.client = cl
        return co

    def save(self):
        sql = f""" 
        BEGIN;
        INSERT INTO "contacts" VALUES ({self.id}, {self.phonenumber}, {self.emailadress}, {self.client_id});
        COMMIT; """

        Contact.connectAndExecute(sql)
    
    def delete(self):
        sql = f""" 
        BEGIN;
        DELETE FROM "contacts" WHERE id = {self.id};
        COMMIT; """

        Contact.connectAndExecute(sql)

    def update(self):
        sql = f""" 
        BEGIN;
        UPDATE "contacts"
        SET phonenumber = '{self.phonenumber}', emailadress = {self.emailadress}, client_id = {self.client_id}
        WHERE id = {self.id};
        COMMIT; """

        Contact.connectAndExecute(sql)

    def __str__(self):
        return f"Contact <{self.id}, {self.phonenumber}, {self.emailadress}, {self.client_id}, {self.client}>"

    def __repr__(self):
        return self.__str__()