#pylint: disable =all

import sqlite3

connection = sqlite3.connect('company.db')

cursor = connection.cursor()
print("Database created successfully")

employee_table = '''
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    department TEXT,
    salary INTEGER)
'''

cursor.execute(employee_table)

sales_table = """
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    amount INTEGER,
    sale_date TEXT
)
"""
cursor.execute(sales_table)

print("Tables created successfully")

employees = [
    (1, "Rahul", "IT", 70000),
    (2, "Priya", "HR", 60000),
    (3, "Amit", "Sales", 80000),
    (4, "Neha", "IT", 75000),
    (5, "Rohan", "Finance", 90000),
    (6, "Anjali", "HR", 65000),
    (7, "Vikas", "Sales", 85000),
    (8, "Sneha", "Finance", 95000),
    (9, "Karan", "IT", 72000),
    (10, "Pooja", "Sales", 88000)
]

cursor.executemany("""INSERT INTO employees (id, name, department, salary)VALUES (?, ?, ?, ?)""", employees)

connection.commit()

print("10 employees inserted")

sales = [
    (1, 1, 50000, "2026-01-10"),
    (2, 2, 60000, "2026-01-12"),
    (3, 3, 90000, "2026-01-15"),
    (4, 4, 70000, "2026-01-18"),
    (5, 5, 80000, "2026-01-20"),
    (6, 6, 55000, "2026-01-22"),
    (7, 7, 95000, "2026-01-25"),
    (8, 8, 85000, "2026-01-27"),
    (9, 9, 65000, "2026-02-01"),
    (10, 10, 100000, "2026-02-05")
]

cursor.executemany("""
INSERT INTO sales (sale_id, employee_id, amount, sale_date)
VALUES (?, ?, ?, ?)
""", sales)

connection.commit()

print("10 Sales data inserted")

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("SELECT * FROM sales")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
print('DAtabase connection closed')