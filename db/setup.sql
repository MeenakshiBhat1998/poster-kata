-- Connect to the database
\c test

DROP TABLE IF EXISTS source;

-- Create the source table
CREATE TABLE source(
    poster_content VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    email VARCHAR(255) NOT NULL,
    sales_rep VARCHAR(255) NOT NULL,
    promo_code VARCHAR(100)
);

-- Create the dw table
CREATE TABLE dw(
    poster_content VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    sales_rep VARCHAR(255) NOT NULL,
    promo_code VARCHAR(100),
    starship_name VARCHAR(255) NOT NULL,
    film_name VARCHAR(255),
    release_date DATE,
    starship_class VARCHAR(255) NOT NULL
);
