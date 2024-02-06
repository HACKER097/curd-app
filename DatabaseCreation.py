import sqlite3

# Define connection and cursor
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Create table
c = """CREATE TABLE IF NOT EXISTS CONTACTS(
NAME TEXT,
NUM TEXT
);"""

cursor.execute(c)
