-- drop database if exists
DROP DATABASE IF EXISTS winery;
-- drop database user if exists
DROP USER IF EXISTS 'winery_user'@'localhost';

-- Create a new user and grant privileges
CREATE USER 'winery_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'popcorn';

GRANT ALL PRIVILEGES ON winery.* TO 'winery_user'@'localhost';


-- Create the database
CREATE DATABASE winery;
USE winery;

-- Create Departments table
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    ManagerID INT
);

-- Create Employees table
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    DepartmentID INT,
    ManagerID INT,
    HoursWorked INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
);

-- Create Products table
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    InventoryQuantity INT
);

-- Create Suppliers table
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    SupplyType VARCHAR(50) NOT NULL,
    DeliverySchedule VARCHAR(50)
);

-- Create SupplyInventory table
CREATE TABLE SupplyInventory (
    SupplyID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierID INT,
    Type VARCHAR(50),
    Quantity INT,
    ExpectedDate DATE,
    DeliveryDate DATE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create Distributors table
CREATE TABLE Distributors (
    DistributorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

-- Create Distribution table
CREATE TABLE Distribution (
    DistributionID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    DistributorID INT,
    SalesQuantity INT,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (DistributorID) REFERENCES Distributors(DistributorID)
);

-- Insert sample data into Departments
INSERT INTO Departments (Name, ManagerID) VALUES 
('Finance', NULL), 
('Marketing', NULL), 
('Production', NULL), 
('Distribution', NULL);

-- Insert sample data into Employees
INSERT INTO Employees (Name, DepartmentID, ManagerID, HoursWorked) VALUES 
('Janet Collins', 1, NULL, 160), 
('Roz Murphy', 2, NULL, 160), 
('Bob Ulrich', 2, 2, 160), 
('Henry Doyle', 3, NULL, 160), 
('Maria Costanza', 4, NULL, 160);

-- Insert sample data into Products
INSERT INTO Products (Name, InventoryQuantity) VALUES 
('Merlot', 1000), 
('Cabernet', 800), 
('Chablis', 600), 
('Chardonnay', 1200);

-- Insert sample data into Suppliers
INSERT INTO Suppliers (Name, SupplyType, DeliverySchedule) VALUES 
('Supplier1', 'Bottles and Corks', 'Monthly'), 
('Supplier2', 'Labels and Boxes', 'Monthly'), 
('Supplier3', 'Vats and Tubing', 'Monthly');

-- Insert sample data into SupplyInventory
INSERT INTO SupplyInventory (SupplierID, Type, Quantity, ExpectedDate, DeliveryDate) VALUES 
(1, 'Bottles', 1000, '2024-07-05', '2024-07-01'), 
(1, 'Corks', 1000, '2024-07-05', '2024-07-01'), 
(2, 'Labels', 1000, '2024-06-29', '2024-07-01'), 
(2, 'Boxes', 1000, '2024-06-29', '2024-07-01'), 
(3, 'Vats', 5, '2024-07-03', '2024-07-01'), 
(3, 'Tubing', 200, '2024-07-03', '2024-07-01');

-- Insert sample data into Distributors
INSERT INTO Distributors (Name) VALUES 
('Distributor1'), 
('Distributor2'), 
('Distributor3');

-- Insert sample data into Distribution
INSERT INTO Distribution (ProductID, DistributorID, SalesQuantity) VALUES 
(1, 1, 500), 
(2, 1, 300), 
(3, 2, 200), 
(4, 3, 700);

-- Verify privileges
SHOW GRANTS FOR 'winery_user'@'localhost';