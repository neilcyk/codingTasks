

# Display the welcome message and ask for total number of students
print('Welcome to examination registration sytem.')
total_student=int(input('Please enter the number of students required to register for the exam:'))

i=0
with open("reg_form.txt", "a") as f: # create or append the file with the following loop input
    for i in range(total_student):  # loop according the total number of students
        student_id=input(f'Input the student#{i+1} ID number:')    # Ask for student ID one-by-one according total number of students
        f.write(student_id + '..........' +"\n") # write and append the inputted student ID in the data file 'reg_form.txt'