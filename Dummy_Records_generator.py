from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Number of records to generate
num_customers = 100
num_contacts_per_customer = 2
num_employees = 50
num_dependents_per_employee = 2
num_branches = 10
num_accounts = 200
num_loans = 50
num_payments_per_loan = 5
num_bankers_per_customer = 2

# Open files to save the generated SQL queries
with open('insert_customers.sql', 'w') as customers_file, \
     open('insert_customer_contacts.sql', 'w') as contacts_file, \
     open('insert_employees.sql', 'w') as employees_file, \
     open('insert_employee_dependents.sql', 'w') as dependents_file, \
     open('insert_branches.sql', 'w') as branches_file, \
     open('insert_accounts.sql', 'w') as accounts_file, \
     open('insert_savings_accounts.sql', 'w') as savings_file, \
     open('insert_current_accounts.sql', 'w') as current_file, \
     open('insert_loans.sql', 'w') as loans_file, \
     open('insert_loan_payments.sql', 'w') as payments_file, \
     open('insert_customer_accounts.sql', 'w') as cust_accounts_file, \
     open('insert_customer_loans.sql', 'w') as cust_loans_file, \
     open('insert_customer_bankers.sql', 'w') as cust_bankers_file, \
     open('insert_employee_managers.sql', 'w') as emp_managers_file:

    # 1. Customers Table
    customers_file.write("INSERT INTO Customer (cust_id, first_name, last_name, address_street, address_city, address_state, dob) VALUES\n")
    for i in range(num_customers):
        cust_id = i + 1
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        address_street = fake.street_address().replace("'", "''")
        address_city = fake.city().replace("'", "''")
        address_state = fake.state().replace("'", "''")
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
        sql_values = f"({cust_id}, '{first_name}', '{last_name}', '{address_street}', '{address_city}', '{address_state}', '{dob}')"
        if i < num_customers - 1:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        customers_file.write(sql_values)

    # 2. CustomerContact Table
    contacts_file.write("INSERT INTO CustomerContact (cust_id, contact_no) VALUES\n")
    contact_id = 1
    for cust_id in range(1, num_customers + 1):
        for _ in range(num_contacts_per_customer):
            contact_no = fake.phone_number().replace("'", "''")
            sql_values = f"({cust_id}, '{contact_no}')"
            if contact_id < num_customers * num_contacts_per_customer:
                sql_values += ",\n"
            else:
                sql_values += ";\n"
            contacts_file.write(sql_values)
            contact_id += 1

    # 3. Employees Table
    employees_file.write("INSERT INTO Employee (emp_id, first_name, last_name, contact_no, start_date, manager_id) VALUES\n")
    for i in range(num_employees):
        emp_id = i + 1
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        contact_no = fake.phone_number().replace("'", "''")
        start_date = fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')
        manager_id = random.randint(1, emp_id) if emp_id > 1 else "NULL"
        sql_values = f"({emp_id}, '{first_name}', '{last_name}', '{contact_no}', '{start_date}', {manager_id})"
        if i < num_employees - 1:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        employees_file.write(sql_values)

    # 4. EmployeeDependent Table
    dependents_file.write("INSERT INTO EmployeeDependent (emp_id, dependent_name) VALUES\n")
    dependent_id = 1
    for emp_id in range(1, num_employees + 1):
        for _ in range(num_dependents_per_employee):
            dependent_name = fake.first_name().replace("'", "''")
            sql_values = f"({emp_id}, '{dependent_name}')"
            if dependent_id < num_employees * num_dependents_per_employee:
                sql_values += ",\n"
            else:
                sql_values += ";\n"
            dependents_file.write(sql_values)
            dependent_id += 1

    # 5. Branches Table
    branches_file.write("INSERT INTO Branch (branch_name, city, state) VALUES\n")
    for i in range(num_branches):
        branch_name = fake.company().replace("'", "''")
        city = fake.city().replace("'", "''")
        state = fake.state().replace("'", "''")
        sql_values = f"('{branch_name}', '{city}', '{state}')"
        if i < num_branches - 1:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        branches_file.write(sql_values)

    # 6. Accounts Table
    # 6. Accounts Table
    accounts_file.write("INSERT INTO Account (account_number, balance) VALUES\n")
    account_numbers = []  # List to store generated account numbers
    for i in range(num_accounts):
        account_number = fake.random_number(digits=10, fix_len=True)
        balance = round(random.uniform(100.00, 10000.00), 2)
        account_numbers.append(account_number)  # Store the account number
        sql_values = f"({account_number}, {balance})"
        if i < num_accounts - 1:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        accounts_file.write(sql_values)

    # 7. SavingsAccount Table
    # 7. SavingsAccount Table
    savings_file.write("INSERT INTO SavingsAccount (account_number, interest_rate, daily_withdrawal_limit) VALUES\n")
    for i in range(num_accounts // 2):
        account_number = account_numbers[i]  # Use the same account number from the Account table
        interest_rate = round(random.uniform(0.5, 5.0), 2)
        daily_withdrawal_limit = round(random.uniform(500, 5000), 2)
        sql_values = f"({account_number}, {interest_rate}, {daily_withdrawal_limit})"
        if i < num_accounts // 2 - 1:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        savings_file.write(sql_values)

    # 8. CurrentAccount Table
    # 8. CurrentAccount Table
    current_file.write("INSERT INTO CurrentAccount (account_number, percentage_charges, overdraft_amount) VALUES\n")
    for i in range(num_accounts // 2, num_accounts):
        account_number = account_numbers[i]  # Use the same account number from the Account table
        percentage_charges = round(random.uniform(0.1, 2.0), 2)
        overdraft_amount = round(random.uniform(500, 5000), 2)
        sql_values = f"({account_number}, {percentage_charges}, {overdraft_amount})"
        if i < num_accounts - 1:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        current_file.write(sql_values)

    # 9. Loan Table
    loans_file.write("INSERT INTO Loan (loan_no, amount, branch_name) VALUES\n")
    for i in range(num_loans):
        loan_no = i + 1
        amount = round(random.uniform(5000.00, 50000.00), 2)
        branch_name = fake.company().replace("'", "''")
        sql_values = f"({loan_no}, {amount}, '{branch_name}')"
        if i < num_loans - 1:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        loans_file.write(sql_values)

    # 10. LoanPayment Table
    payments_file.write("INSERT INTO LoanPayment (payment_no, loan_no, payment_date, amount) VALUES\n")
    payment_id = 1
    for loan_no in range(1, num_loans + 1):
        for _ in range(num_payments_per_loan):
            payment_date = fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
            amount = round(random.uniform(100.00, 1000.00), 2)
            sql_values = f"({payment_id}, {loan_no}, '{payment_date}', {amount})"
            if payment_id < num_loans * num_payments_per_loan:
                sql_values += ",\n"
            else:
                sql_values += ";\n"
            payments_file.write(sql_values)
            payment_id += 1

    # 11. CustomerAccount Table
    cust_accounts_file.write("INSERT INTO CustomerAccount (cust_id, account_number) VALUES\n")
    for cust_id in range(1, num_customers + 1):
        account_numbers = random.sample(range(1, num_accounts + 1), 2)
        for account_number in account_numbers:
            sql_values = f"({cust_id}, {account_number})"
            cust_accounts_file.write(sql_values + ",\n")

    # 12. CustomerLoan Table
    cust_loans_file.write("INSERT INTO CustomerLoan (cust_id, loan_no) VALUES\n")
    for cust_id in range(1, num_customers + 1):
        loan_numbers = random.sample(range(1, num_loans + 1), 1)
        for loan_no in loan_numbers:
            sql_values = f"({cust_id}, {loan_no})"
            cust_loans_file.write(sql_values + ",\n")

    # 13. CustomerBanker Table
    cust_bankers_file.write("INSERT INTO CustomerBanker (cust_id, emp_id) VALUES\n")
    for cust_id in range(1, num_customers + 1):
        banker_ids = random.sample(range(1, num_employees + 1), num_bankers_per_customer)
        for emp_id in banker_ids:
            sql_values = f"({cust_id}, {emp_id})"
            cust_bankers_file.write(sql_values + ",\n")

    # 14. EmployeeManager Table
    emp_managers_file.write("INSERT INTO EmployeeManager (emp_id, manager_id) VALUES\n")
    for emp_id in range(2, num_employees + 1):
        manager_id = random.randint(1, emp_id - 1)
        sql_values = f"({emp_id}, {manager_id})"
        if emp_id < num_employees:
            sql_values += ",\n"
        else:
            sql_values += ";\n"
        emp_managers_file.write(sql_values)
