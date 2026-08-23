#pylint: disable =all

import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()

table_info = '''CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)'''

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES('AMIT', 'Data Science', 'C', 96)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vivek', 'Data Analytics', 'B', 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Arun', 'Science', 'D', 76)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Keshav', 'Tech', 'A', 66)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Santosh', 'Engineering', 'E', 56)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Yuvi', 'Data Science', 'A', 46)''')

print('The inserted records are:')

data= cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

connection.commit()

connection.close()