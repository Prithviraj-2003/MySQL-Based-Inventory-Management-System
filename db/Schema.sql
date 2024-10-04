-- Create the database
CREATE DATABASE inventory_system;

-- Use the created database
USE inventory_system;

-- Create items table
CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);
-- Insert sample items
INSERT INTO items (name, quantity, price) VALUES ('Laptop', 10, 999.99);
INSERT INTO items (name, quantity, price) VALUES ('Mouse', 50, 25.99);
