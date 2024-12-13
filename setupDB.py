import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
 
cursor.execute("DROP TABLE IF EXISTS Persons")
 
# Creating table
table = """ 
CREATE TABLE People (
	ID INTEGER PRIMARY KEY,
	FirstName TEXT NOT NULL,
	LastName TEXT,
    Age INTEGER
);
"""
 
cursor.execute(table)
 
print("Table People is Ready!")
 