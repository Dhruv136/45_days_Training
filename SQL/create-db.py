import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

connection.commit()
connection.close()

print("Database Created Successfully!")