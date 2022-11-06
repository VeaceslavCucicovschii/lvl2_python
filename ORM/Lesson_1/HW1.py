import psycopg2
import random

# HW1: Insert 10 products with random values

conn = psycopg2.connect("dbname=e_shop_python user=postgres password=qazwsx")

for i in range(1, 11):
    product_id = i
    price_price = random.randint(100, 9900)
    product_quantity = random.randint(10, 200)

    sql = f""" 
    BEGIN;
    INSERT INTO "money" VALUES({product_id}, {price_price}, 'EUR');
    INSERT INTO "products" VALUES({product_id}, 'Product {product_id}', {product_id});
    INSERT INTO "stock" VALUES({product_id}, {product_id}, {product_quantity});
    COMMIT; """

    cursor = conn.cursor()
    cursor.execute(sql)
