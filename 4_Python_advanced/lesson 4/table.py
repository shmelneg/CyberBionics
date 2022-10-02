import sqlite3

connection = sqlite3.connect('Accounting.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Accounting")

table = """
CREATE TABLE Accounting (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    expenses REAL,
    income REAL,
    transaction_time NUMERIC NOT NULL
);
"""

cursor.execute(table)

print("Accounting table is created")

cursor.close()
connection.close()
