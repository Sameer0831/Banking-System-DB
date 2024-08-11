# Banking System Database Project

## Overview

This project involves designing and implementing a comprehensive banking system database, beginning with requirements gathering and culminating in the creation of a fully functional database. The project includes the identification of key entities, mapping of relationships, and generation of an Entity-Relationship (ER) diagram. This diagram serves as a blueprint for the database structure, ensuring a clear understanding of the data flow and relationships within the system.

## ER Diagram

The ER diagram was created using [draw.io](https://app.diagrams.net/), providing a visual representation of the database's conceptual structure. It helps in identifying entities, attributes, and relationships, laying the groundwork for the actual database creation. The ER diagram serves as a critical blueprint, guiding the development of a well-organized and scalable database.

## Project Objectives

- **Entity Identification:** Key entities such as `Customer`, `Account`, `Loan`, and `Branch` were identified.
- **Relationship Mapping:** Relationships between entities were established, ensuring accurate data representation and integrity.
- **Database Implementation:** A normalized database was created using MySQL, with appropriate constraints, foreign keys, and realistic dummy data.

## Steps to Run the Project

### 1. Set Up MySQL

- Install and configure MySQL on your system.
- Create a new database for the project:
  ```sql
  CREATE DATABASE BankingSystem;
  USE BankingSystem;
  ```

### 2. Create Tables

- Execute the SQL statements to create the necessary tables:
  - `Branch`
  - `Customer`
  - `Employee`
  - `Account` (generalized from `SavingsAccount` and `CurrentAccount`)
  - `Loan`
  - `Payment`
  - `CustomerAccount`
  - `CustomerLoan`
  - `CustomerBanker`
  - `EmployeeManager`
- Each table includes primary keys, foreign keys, and constraints to maintain data integrity and represent real-world relationships.

### 3. Insert Dummy Data

- Populate the tables with more than 100 dummy records for main entities such as `Customer`, `Employee`, `Account`, and `Loan`.
- Use the provided SQL scripts to insert this data, ensuring the relationships between entities are respected.

### 4. Query the Database

- Run SQL queries to explore the connections and interactions between different entities:
  - Retrieve loans associated with specific customers.
  - List accounts held by customers at a particular branch.
  - View all payments made for specific loans.

## Additional Notes

- This project establishes a basic structure of a banking system database, which can be connected to a frontend interface to build a fully functional application.
- The SQL queries demonstrate the interrelation between different activities in the banking system, emphasizing the importance of well-designed databases.
- Data is stored in its true storage form, ensuring the database's integrity and readiness for real-world applications.

## Conclusion

This project showcases the end-to-end process of creating a banking system database, from conceptual design with an ER diagram to the final implementation in MySQL. The focus on relationships and data integrity ensures a robust and scalable database, capable of supporting complex banking operations.
