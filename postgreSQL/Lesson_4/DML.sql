-- INSERT PRODUCTS
BEGIN;
INSERT INTO "money" VALUES(1, 2500, 'EUR');
INSERT INTO "products" VALUES(1, 'Product 1', 1);
INSERT INTO "stock" VALUES(1, 1, 100);
COMMIT;

BEGIN; -- START TRANSACTION
INSERT INTO "money" VALUES(2, 5100, 'EUR');
INSERT INTO "products" VALUES(2, 'Product 10', 2);
INSERT INTO "stock" VALUES(2, 2, 200);
COMMIT; -- END TRANSACTION

BEGIN;
INSERT INTO "money" VALUES(3, 15500, 'EUR');
INSERT INTO "products" VALUES(3, 'Product 10', 3);
INSERT INTO "stock" VALUES(3, 3, 150);
COMMIT;

/*
BEGIN; -- IF WE DONT USE CASCADE ON SETTING FOREIGN KEY
DELETE FROM "stock" WHERE product_id = 12;
DELETE FROM "products" WHERE price_id = 3;
DELETE FROM "money" WHERE id = 3;
COMMIT;

-- IF WE USE CASCADE ON SETTING FOREIGN KEY
DELETE FROM "money" WHERE id = 3;
*/

-- INSERT CLIENT
BEGIN;
INSERT INTO "clients" VALUES(1, 'John Doe', false);
INSERT INTO "contacts" VALUES(1, '', 'JohnDoe@gmail.com', 1);
COMMIT;

BEGIN;
INSERT INTO "clients" VALUES(2, 'Marry Poppins', false);
INSERT INTO "contacts" VALUES(2, '', 'MarryPoppins@gmail.com', 2);
INSERT INTO "contacts" VALUES(3, '+456789012', 'MarryPoppins@gmail.com', 2);
COMMIT;

BEGIN;
INSERT INTO "money" VALUES(14, 5100 * 5, 'EUR');
INSERT INTO "bags" VALUES(1, 14, 2);
INSERT INTO "bags_items" VALUES(1, 1, 2, 5);
UPDATE "stock" SET quantity = quantity - 5 WHERE product_id = 13; 
COMMIT;

BEGIN;
UPDATE "money" SET amount = amount + 15500 * 10 WHERE id = 1;
INSERT INTO "bags_items" VALUES(2, 1, 3, 10);
UPDATE "stock" SET quantity = quantity - 10 WHERE product_id = 3; 
COMMIT;

-- HW_1: emulate when client (id=2) decreases product (id=3) by 3
BEGIN;
UPDATE "money" SET amount = amount - 3 WHERE id = 1;
UPDATE "bags_items" SET quantity = quantity - 3 WHERE id = 2;
UPDATE "stock" SET quantity = quantity - 10 WHERE product_id = 3; 
COMMIT;

SELECT name, quantity, amount, amount * quantity, currency FROM "bags"
JOIN "bags_items" ON "bags_items".bag_id = "bags".id
JOIN "products" ON "bags_items".product_id = "products".id
JOIN "money" ON "products".price_id = "money".id
WHERE "bags".client_id = 2;

SELECT amount, currency FROM "bags"
JOIN "money" ON "bags".cost_id = "money".id
WHERE "bags".client_id = 2;

/*
SELECT * FROM "contacts";
SELECT * FROM "bags_items";
SELECT * FROM "bags";
SELECT * FROM "clients";
SELECT * FROM "stock";
SELECT * FROM "products";
SELECT * FROM "money";
*/
