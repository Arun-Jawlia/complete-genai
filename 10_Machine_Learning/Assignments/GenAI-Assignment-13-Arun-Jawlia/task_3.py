# pylint: disable=all

"""
Task 3: Load Data from SQLite Database
"""

import sqlite3
import pandas as pd

# Create database
conn = sqlite3.connect("sample.db")

# Create cursor
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

# Sample Data
employees = [
    (1, "Alice", "HR", 50000),
    (2, "Bob", "IT", 65000),
    (3, "Charlie", "Finance", 60000),
    (4, "David", "Marketing", 55000),
    (5, "Eva", "Sales", 58000)
]

# Insert Data
cursor.executemany("""
INSERT OR REPLACE INTO employees
VALUES (?, ?, ?, ?)
""", employees)

# Save changes
conn.commit()

# Read SQL Table into DataFrame
df = pd.read_sql_query("SELECT * FROM employees", conn)

# Display DataFrame
print("Employee Data")
print(df)

print("\nFirst 5 Rows")
print(df.head())

print("\nData Types")
print(df.dtypes)

print("\nShape")
print(df.shape)

# Close connection
conn.close()