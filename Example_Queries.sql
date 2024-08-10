-- Question 1: How many customers have at least one savings account?

SELECT COUNT(DISTINCT CA.cust_id) AS total_customers_with_savings
FROM CustomerAccount CA
JOIN SavingsAccount SA ON CA.account_number = SA.account_number;

-- Question 2: What is the total balance of all savings accounts across all branches?

SELECT SUM(A.balance) AS total_savings_balance
FROM Account A
JOIN SavingsAccount SA ON A.account_number = SA.account_number;

-- Question 3: List all customers who have a loan and are also assigned a banker (employee).

SELECT DISTINCT C.cust_id, C.first_name, C.last_name
FROM Customer C
JOIN CustomerLoan CL ON C.cust_id = CL.cust_id
JOIN CustomerBanker CB ON C.cust_id = CB.cust_id;

-- Question 4: What is the average interest rate of savings accounts?

SELECT AVG(SA.interest_rate) AS average_interest_rate
FROM SavingsAccount SA;

-- Question 5: How many employees have at least one dependent?

SELECT COUNT(DISTINCT ED.emp_id) AS employees_with_dependents
FROM EmployeeDependent ED;

-- Question 6: Which branch has issued the highest total amount in loans?

SELECT L.branch_name, SUM(L.amount) AS total_loan_amount
FROM Loan L
GROUP BY L.branch_name
ORDER BY total_loan_amount DESC
LIMIT 1;

-- Question 7: What is the total amount paid towards loans so far?

SELECT SUM(LP.amount) AS total_loan_payments
FROM LoanPayment LP;

-- Question 8: Which customer has the highest combined balance across all their accounts (savings + current)?

SELECT CA.cust_id, SUM(A.balance) AS total_balance
FROM CustomerAccount CA
JOIN Account A ON CA.account_number = A.account_number
GROUP BY CA.cust_id
ORDER BY total_balance DESC
LIMIT 1;

-- Question 9: List the names of employees who manage more than 5 other employees.

SELECT E.emp_id, E.first_name, E.last_name, COUNT(EM.manager_id) AS number_of_employees_managed
FROM Employee E
JOIN EmployeeManager EM ON E.emp_id = EM.manager_id
GROUP BY E.emp_id, E.first_name, E.last_name
HAVING COUNT(EM.manager_id) > 5;

-- Question 10: What is the total loan amount approved for each customer?

SELECT C.cust_id, SUM(L.amount) AS total_loan_amount
FROM CustomerLoan CL
JOIN Loan L ON CL.loan_no = L.loan_no
JOIN Customer C ON CL.cust_id = C.cust_id
GROUP BY C.cust_id
ORDER BY C.cust_id;



























































-- Question 10: Which employee has the highest number of customers assigned to them as bankers?

SELECT E.emp_id, E.first_name, E.last_name, COUNT(CB.cust_id) AS number_of_customers
FROM Employee E
JOIN CustomerBanker CB ON E.emp_id = CB.emp_id
GROUP BY E.emp_id, E.first_name
ORDER BY number_of_customers DESC
LIMIT 1;
