count=0
total=0
num=0
while num!=-1:
    num=int(input('Enter a number: '))
    if (num!=-1 and num!=0):
        total+=num
        count+=1
    elif num==0: print('Note 0 is not a valid input.')
print(total/count)