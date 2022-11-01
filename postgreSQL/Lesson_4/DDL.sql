CREATE TABLE money (
    id integer PRIMARY KEY,
    amount integer NOT NULL,
    currency character varying NOT NULL
);

CREATE TABLE products (
    id integer PRIMARY KEY,
    name character varying NOT NULL,
    price_id integer NOT NULL,

    CONSTRAINT fk_products_money FOREIGN KEY (price_id)
    REFERENCES "money" (id) ON DELETE CASCADE
);

CREATE TABLE stock (
    id integer PRIMARY KEY,
    product_id integer NOT NULL,
    quantity integer NOT NULL,

    CONSTRAINT fk_stock_products FOREIGN KEY (product_id)
    REFERENCES "products" (id) ON DELETE CASCADE
);

CREATE TABLE clients (
    id integer PRIMARY KEY,
    fullName character varying NOT NULL,
    isVIP boolean DEFAULT false
);

CREATE TABLE bags (
    id integer PRIMARY KEY,
    cost_id integer NOT NULL,
    client_id integer NOT NULL,

    CONSTRAINT fk_bags_client FOREIGN KEY (client_id)
    REFERENCES "clients" (id) ON DELETE CASCADE,

    CONSTRAINT fk_bags_money FOREIGN KEY (cost_id)
    REFERENCES "money" (id) ON DELETE CASCADE
);

CREATE TABLE bags_items (
    id integer PRIMARY KEY,
    bag_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL,

    CONSTRAINT fk_bags_items_bag FOREIGN KEY (bag_id)
    REFERENCES "bags" (id) ON DELETE CASCADE,

    CONSTRAINT fk_bags_items_product FOREIGN KEY (product_id)
    REFERENCES "products" (id) ON DELETE CASCADE
);

CREATE TABLE contacts (
    id integer PRIMARY KEY,
    phoneNumber character varying,
    emailAdress character varying NOT NULL,
    client_id integer,

    CONSTRAINT fk_contacts_client FOREIGN KEY (client_id)
    REFERENCES "clients" (id) ON DELETE CASCADE
);

/*
DROP TABLE "contacts";
DROP TABLE "bags_items";
DROP TABLE "bags";
DROP TABLE "clients";
DROP TABLE "stock";
DROP TABLE "products";
DROP TABLE "money";
*/