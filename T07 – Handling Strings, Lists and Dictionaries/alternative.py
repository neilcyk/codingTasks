# Ask for user input with proper instruction and store in variable 'text'
text=input('Task 7 Auto-graded task 1 - Input a string mixed with Upper and lower character:')

i=0
for i in range(len(text)): # Loop each character according the length of the text
    if i%2==0: print(text[i].upper(), end="") # Identify the odd position of character and transform it to upper character.
    if i%2!=0: print(text[i].lower(), end="") # Identify the even position of character and transform it to lower character.

print() # break two outputs in separate line

word_list=text.split() # convert the text string into a word list by deafult, space, as delimiter

i=0
for i in range(len(word_list)):  # Loop each word according the length of the list
    if i%2==0: print(word_list[i].lower(), end=" ") # Identify the odd position of word in list and transform it to lower character.
    if i%2!=0: print(word_list[i].upper(), end=" ") # Identify the even position of word in list and transform it to upper character.