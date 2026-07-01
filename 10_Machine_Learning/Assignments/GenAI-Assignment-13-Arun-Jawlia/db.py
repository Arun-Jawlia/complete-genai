
import sqlite3

# Create database
conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

conn.commit()

employees = [
    (1, "Alice", "HR", 50000),
    (2, "Bob", "IT", 65000),
    (3, "Charlie", "Finance", 60000)
]

cursor.executemany(
    "INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)",
    employees
)

conn.commit()
