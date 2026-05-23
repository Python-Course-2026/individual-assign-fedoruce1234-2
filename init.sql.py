CREATE TABLE categories (
    id   SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

INSERT INTO categories(name)
VALUES
    ('apple'),
    ('pencil');

SELECT *FROM categories;

DROP TABLE products;
CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    category_id INTEGER REFERENCES categories(id),
    in_stock BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT now()
);
INSERT INTO products (name, price, category_id)
VALUES ('Iphone', 1300.99, 2);

SELECT * FROM products;

SELECT JOIN
     products.name,
    products.price,
    categories.name AS category,
    products.in_stock
FROM products
JOIN categories ON products.category_id = categories.id;