import re # Adopt re module aim for search a number in the middle of each line in file (Approach to split each line in two by day)

# Initialise lists
name_list=[]
birthday_list=[]

with open('DOB.txt', 'r') as file:
    for line in file:
        line = line.strip()  # reading line by line until reach the end of file
        if line:  # ensure there is no empty line
            match = re.search('\d', line) # find the first number (day in this case)
            if match:
                # Split the line into 'name' and 'birthday' based on the position of the date
                split_index = match.start() # locate the exact postion of the day...
                name = line[:split_index].strip()  # The name is before the day (first and last name)
                birthday = line[split_index:].strip()  # The birthday is from the day onwards (day, month and year)
                name_list.append(name) # build up the name list for all names
                birthday_list.append(birthday) # build up the birthday list for all days

# Print the results as required format
print("Names")
for i in range(len(name_list)):
    print(name_list[i])

print()

print("Birthdate")
for i in range(len(birthday_list)):
    print(birthday_list[i])
