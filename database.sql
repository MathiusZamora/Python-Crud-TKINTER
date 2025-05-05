-- Create the pharmacy database
CREATE DATABASE IF NOT EXISTS pharmacydatabase;
USE pharmacydatabase;

-- Table for laboratories
CREATE TABLE IF NOT EXISTS labs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    status TINYINT NOT NULL CHECK (status IN (1, 2)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for suppliers
CREATE TABLE IF NOT EXISTS suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    status TINYINT NOT NULL CHECK (status IN (1, 2)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for items/products
CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    labs_id INT NOT NULL,
    suppliers_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    expiration_date VARCHAR(10) NOT NULL, -- Format: dd/mm/yyyy
    description TEXT,
    status TINYINT NOT NULL CHECK (status IN (1, 2)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (labs_id) REFERENCES labs(id) ON DELETE CASCADE,
    FOREIGN KEY (suppliers_id) REFERENCES suppliers(id) ON DELETE CASCADE
);
