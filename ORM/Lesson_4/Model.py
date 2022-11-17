from datetime import datetime
import random
import psycopg2

class Model:
    def __init__(self, id):
        self.id = id

    def connectAndExecute(sql, returns = False):
        conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

        cursor = conn.cursor()
        cursor.execute(sql)

        if returns:
            results = cursor.fetchall()
            return results

def id():
    # rand number
    random_nr = random.randint(0, 999999)
    return random_nr