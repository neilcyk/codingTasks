import sqlite3

def create_database():
    Conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS students;')
    cursor.execute(
        """
        CREATE TABLE student(
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCAHR(50) NOT NULL,
            last_name VARCAHR(50) NOT NULL,
            email VARCAHR(50) NOT NULL UNIQUE,
        )
        """
    )

    cursor.executemany(
        """
        INSERT INTO student
        VALUES (?,?,?)""", (('John','Doe','john@doe.com')
                            ('Peter','Parker','peter@gmail.com')
                            ('Tina','Johnson','tina@gmail.com')
                            ('Neil','Cheung','neil@gmail.com')))
    
    conn.commit()


    def user_search():
        cursor = conn.cursor()

        user_input = input('Enter the first name: ')

        quer = f'SELECT * FROM students WHERE first_name = {user_input}'
        print(f'Query: {query}')
              
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            if results:
              for record in results:
                print(Record)
            else:
              print('No results!')
        except sqlite3.Error as e:
            print(f'Error: {e}')
            