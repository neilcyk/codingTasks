import sqlite3

#Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

#Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
''')

#Insert the rows into the table
students = [
    (55, "Carl Davis", 61),
    (66, "Dennis Fredrickson", 88),
    (77, "Jane Richards", 78),
    (12, "Peyton Sawyer", 45),
    (2, "Lucas Brooke", 99)
]

cursor.executemany("INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)", students)
conn.commit()

#Select all records with grade between 60 and 80
cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
print("Students with grade between 60 and 80:")
for row in cursor.fetchall():
    print(row)

#Change Carl Davis's grade
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")
conn.commit()

#Delete row
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")
conn.commit()

#Change all grades greater than 55 to 80
cursor.execute("UPDATE python_programming SET grade = 80 WHERE id > 55")
conn.commit()

#Display final data table
cursor.execute("SELECT * FROM python_programming")
print("\nFinal Table Data:")
for row in cursor.fetchall():
    print(row)

conn.close()
