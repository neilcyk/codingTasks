from create_database_file import get_sql_cursor

usage_message = '''--------------------------------------------------
Welcome to our logging-in system.
We use the state-of-the-art passwordless login.

To log into your profile, enter into input2.txt the following details:
"email_address
student_id"

If you know your student ID, you will be logged into the system.
For an example, please look at input2_example.txt.
--------------------------------------------------
'''

print(usage_message)

# Create database and get cursor
cursor = get_sql_cursor()

with open("input2.txt", encoding="utf-8") as in_file:
    # Read input from input2.txt and trim unnecessary spaces
    credentials = in_file.read().strip().split("\n")

    # Ensure correct input format
    if len(credentials) != 2:
        print("Invalid input format. Ensure input2.txt contains email and student ID on separate lines.")
        exit(1)

    email_addr, stu_id = credentials
    print(f"Logging in for account {email_addr} . . .")

    # Adopt parameterized query
    cursor.execute("SELECT * FROM Student WHERE email = ? AND student_id = ?", (email_addr, stu_id))
    result_data = cursor.fetchall()

    print(f"Found {len(result_data)} entries.")

    if len(result_data) == 1:
        _, firstname, lastname, _, _ = result_data[0]
        print(f"Welcome {firstname} {lastname}.")
    else:
        print("Login Unsuccessful.")