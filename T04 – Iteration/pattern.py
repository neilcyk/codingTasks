row=5
#row = int(input("Enter the number of row: "))

for i in range(1, row + 1):
    print('*' * i)
for i in range(row-1, 0, -1):
    print('*' * i)