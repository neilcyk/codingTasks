# =========== Python list Methods  ===========
# There are many useful built-in list methods available for you to use.
# Some other list methods can be found below:
#   extend()    - Adds all elements of a list to the another list
#   insert()    - Inserts an item at the defined index
#   remove()    - Removes an item from the list
#   pop()       - Removes and returns an element at the given index
#   index()     - Returns the index of the first matched item
#   count()     - Returns the count of number of items passed as an argument
#   sort()      - Sorts items in a list in ascending order
#   reverse()   - Reverses the order of items in the list

# =========== The Copy Module  ===========
# Let's take a closer look at the copy module.
# There are several ways to make a copy of a list.
# The simplest way to make a copy is to use the copy() method.
# Using the copy() method ensures that if you modify the copied list,
# the original list remains the same.
# However, if your list contains other lists as items, those inner lists in
# the original list can still be modified
# if the corresponding inner list in the copied list is modified.
# This is called a shallow copy.
# Slicing lists also creates a shallow copy of a list.
# Therefore, when the list contains other lists as items, the inner lists
# have to be copied as well.
# You could do this manually but Python already contains a method to do it,
# the deepcopy() method.
# In order to use the deepcopy() and copy() methods you must import the
# copy module.

# ************ Example 1 ************
print("Example 1:")

import copy  # Imports are typically placed at the top of the file.

a = [[1, 2, 3], [4, 5, 6]]
b = copy.copy(a)  # Shallow copy using copy.copy()
c = a[:]  # Shallow copy using slicing
d = copy.deepcopy(a)  # Deep copy using copy.deepcopy()

b[1][0] = 10
c[1][1] = 11
d[1][2] = 12

print("List a:")
print(a)
print("List b:")
print(b)
print("List c:")
print(c)
print("List d:")
print(d)  # Only d[1][2] is changed due to deep copy

# =========== List Comprehension ===========
# List comprehension offers an elegant way to create lists based on
# existing lists.
# It applies an operation to each element and collects results in a new list.

# ************ Example 2 ************
print("\nExample 2:")

num_list = ["1", "5", "8", "14", "25", "31"]
print(num_list)

# Convert string elements to integers using list comprehension
new_num_list_ints = [int(element) for element in num_list]
print(new_num_list_ints)  # Prints converted integers

# Sum of integers in new_num_list_ints using built-in sum() function as
# new_num_list_ints now contains integer elements instead of string elements.
print(sum(new_num_list_ints))  # Output: 84

# ************ Example 3 ************
# You can do many operations with list comprehensions.
print("\nExample 3:")

# Create a new list where each element in new_num_list_ints is doubled
double_list = [2 * element for element in new_num_list_ints]
print(double_list)

# Create a new list where each element in new_num_list_ints is halved
half_list = [0.5 * element for element in new_num_list_ints]
print(half_list)

# =========== Dictionaries ===========

# =========== Creating a Dictionary ===========
# Dictionaries store key-value pairs enclosed in curly braces {}.
# Keys must be immutable (strings, numbers), values can be any data type.

# ************ Example 4 ************
print("\nExample 4:")

empty_dict = {}  # Empty dictionary

int_key_dict = {1: "apple", 2: "banana", 3: "orange"}  # Integer keys

string_key_dict = {
    "name": "John",
    "surname": "Doe",
    "gender": "male",
}  # String keys

mix_key_dict = {"word": "Python", 2: [1, 3, 4, 5]}  # Mixed keys

# =========== Accessing Elements from a Dictionary ===========
# Access values using keys in square brackets [] or with the get() method.

# ************ Example 5 ************
print("\nExample 5:")

profile_dict = {
    "name": "Chris",
    "surname": "Smith",
    "age": 28,
    "cell": "083 233 3242",
}

print(profile_dict["surname"])  # Accessing 'surname' using []
print(profile_dict.get("cell"))  # Accessing 'cell' using get()

# =========== Changing Elements in a Dictionary ===========
# Modify existing values or add new key-value pairs using assignment (=).

# ************ Example 6 ************
print("\nExample 6:")

profile_dict["age"] = 29  # Changing value for 'age'
print(profile_dict)

profile_dict["gender"] = "male"  # Adding new key-value pair
print(profile_dict)

# =========== Dictionary Membership Test ===========
# Check if a key exists in a dictionary using the 'in' keyword.

# ************ Example 7 ************
print("Example 7:")

doubles = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

print(1 in doubles)  # True, '1' is a key in 'doubles'
print(8 in doubles)  # False, '8' is not a key in 'doubles'

# ****************** END OF EXAMPLE CODE ********************* #
