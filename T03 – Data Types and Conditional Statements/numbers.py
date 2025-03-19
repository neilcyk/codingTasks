
num1=input('Please input integer 1: ')
num2=input('Please input integer 2: ')
num3=input('Please input integer 3: ')
num_list=[int(num1),int(num2),int(num3)]

# The sum of all the numbers
print(sum(num_list))

# The first number minus the second number
print(int(num1)-int(num2))

# The third number multiplied by the first number
print(int(num3)*int(num1))

# The sum of all three numbers divided by the third number
print(sum(num_list)/int(num3))