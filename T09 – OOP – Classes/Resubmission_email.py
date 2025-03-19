# Class defination 
class Email():    
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    # Methods to tuggle an e-mail is read or not.
    def mark_as_read(self):
        self.has_been_read = True
    def mark_unread(self):
        self.has_been_read = False
# Function to generate objects as Email class.
def populate_inbox(email_address, subject_line, email_content):
    email=Email(email_address, subject_line, email_content)
    inbox.append(email)
# List all e-mails with index numbers.
def list_emails():
    print('======================================================')
    for index, email in enumerate(inbox):
        if email.has_been_read == False:
            print(f'{index} {email.subject_line} {email.has_been_read}')
    print('======================================================')
# show the e-mail detials and content. then ask for reading option.
def read_email(index):
    email = inbox[index]
    print('-----------------------------------------------------')
    print(f'From: {email.email_address}')
    print(f'Subject: {email.subject_line}')
    print(f'Content: {email.email_content}')
    print('-----------------------------------------------------')
    email.mark_as_read()  # Update the email as read
    print(f'\nEmail from {email.email_address} marked as read.({email.has_been_read})\n') # and display a message noticfication.
# function for asking user input for e-mail to read.
def asking():
    list_emails()
    indexread=int(input('Select number of an e-mail to read:'))
    read_email(indexread)
# Functon for exit the whole program.
def exit():
    exit()

# Initialise empty list
inbox=[]

# Generate three sample e-mails with details.
populate_inbox('neilcyk@gmail.com', 'Hello', 'Just to say hi!')
populate_inbox('neil@gmail.com', 'How are you?', 'Long time no see.')
populate_inbox('cyk@gmail.com', 'Happy New Year', 'Have a great New year!')

# user menu load up with options.
def menu():
    while True:
        print('******** Menu ********')
        print('1. Read an email')
        print('2. View unread emails')
        print('3. Quit application')
        print('**********************')

        choice = input('Enter your choice: ')

        # get the selected option from menu and execute associated function. Option '3' break the program and exit.
        if choice == '1':
            asking()
        elif choice == '2':
            list_emails()
        elif choice == '3':
            print('Goodbye!')
            break
        else: # check invalid number not in the menu.
            print('Invalid choice. Please select a valid option.')
menu()