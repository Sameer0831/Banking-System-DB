-- DROPPING THE DATABASE, IF IT ALREADY EXISTS
DROP database banking_system;

-- CREATING THE DATABASE
CREATE DATABASE banking_system;

-- USE DATABASE
USE BANKING_SYSTEM;

-- VERIFY THE DATABASE;
SELECT DATABASE();

-- CREATE ALL REQUIRED TABLES WITH THEIR SCHEMAS
-- Multi-Valued Attributes: Handled through separate tables (e.g., CustomerContact, EmployeeDependent).
-- Many-to-Many Relationships: Implemented using associative tables (e.g., CustomerAccount, CustomerLoan).

-- 1. Customer Table
CREATE TABLE Customer (
    cust_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    address_street VARCHAR(100),
    address_city VARCHAR(100),
    address_state VARCHAR(100),
    dob DATE
);

--  2. CustomerContact Table
CREATE TABLE CustomerContact (
    cust_id INT,
    contact_no VARCHAR(100),
    PRIMARY KEY (cust_id, contact_no),
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE
);

-- 3. Employee Table
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    contact_no VARCHAR(100),
    start_date DATE,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employee(emp_id) ON DELETE SET NULL
);

-- 4. EmployeeDependent Table
CREATE TABLE EmployeeDependent (
    emp_id INT,
    dependent_name VARCHAR(100),
    PRIMARY KEY (emp_id, dependent_name),
    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id) ON DELETE CASCADE
);

-- 5. Branch Table
CREATE TABLE Branch (
    branch_name VARCHAR(100) PRIMARY KEY,
    city VARCHAR(100),
    state VARCHAR(100)
);

-- 6. Account Table (Generalization)
CREATE TABLE Account (
    account_number BIGINT PRIMARY KEY,
    balance DECIMAL(20,2)
);

-- 7. SavingsAccount Table (Specialization of Account)
CREATE TABLE SavingsAccount (
    account_number BIGINT PRIMARY KEY,
    interest_rate DECIMAL(5,2),  -- Adjusted precision for interest rate
    daily_withdrawal_limit DECIMAL(15,2),
    FOREIGN KEY (account_number) REFERENCES Account(account_number)
);

-- 8. CurrentAccount Table (Specialization of Account)
CREATE TABLE CurrentAccount (
    account_number BIGINT PRIMARY KEY,
    percentage_charges DECIMAL(5,2),  -- Adjusted precision for percentage charges
    overdraft_amount DECIMAL(15,2),
    FOREIGN KEY (account_number) REFERENCES Account(account_number)
);

-- 9. Loan Table
CREATE TABLE Loan (
    loan_no INT PRIMARY KEY,
    amount DECIMAL(20,2),
    branch_name VARCHAR(100),
    FOREIGN KEY (branch_name) REFERENCES Branch(branch_name)
);

-- 10. LoanPayment Table (Weak Entity)
CREATE TABLE LoanPayment (
    payment_no INT PRIMARY KEY,
    loan_no INT,
    payment_date DATE,
    amount DECIMAL(20,2),
    FOREIGN KEY (loan_no) REFERENCES Loan(loan_no) ON DELETE CASCADE
);

-- 11. CustomerAccount Table (Many-to-Many Relationship)
CREATE TABLE CustomerAccount (
    cust_id INT,
    account_number BIGINT,
    PRIMARY KEY (cust_id, account_number),
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE,
    FOREIGN KEY (account_number) REFERENCES Account(account_number) ON DELETE CASCADE
);

-- 12. CustomerLoan Table (Many-to-Many Relationship)
CREATE TABLE CustomerLoan (
    cust_id INT,
    loan_no INT,
    PRIMARY KEY (cust_id, loan_no),
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE,
    FOREIGN KEY (loan_no) REFERENCES Loan(loan_no) ON DELETE CASCADE
);

-- 13. CustomerBanker Table (Relationship between Customer and Employee)
-- If a customer is deleted, all related records in CustomerBanker are deleted.
-- If an employee is deleted, all related records in CustomerBanker are also deleted.
CREATE TABLE CustomerBanker (
    cust_id INT,
    emp_id INT,
    PRIMARY KEY (cust_id, emp_id),
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE,
    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id) ON DELETE CASCADE
);

-- 14. EmployeeManager Table (Unary Relationship)
-- if either an employee or their manager is deleted, the related records in the "EmployeeManager" table are also deleted.
CREATE TABLE EmployeeManager (
    emp_id INT,
    manager_id INT,
    PRIMARY KEY (emp_id, manager_id),
    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id) ON DELETE CASCADE,
    FOREIGN KEY (manager_id) REFERENCES Employee(emp_id) ON DELETE CASCADE
);