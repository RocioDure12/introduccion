# Lists are used to store multiple items in a single variable.

List = ["paloma", "Aguila", "Agapornis", "Pavo", "Cuervo"]

# Changeable: the list is changeable, meaning that we can change, add,and remove items in a list
# after it has been created

# Loop through a list

for x in List:
    print(x)

# Loop through the index numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

numbers = [1, 5, 6, 9]
for i in range(len(numbers)):
    print(numbers[i], [i+1])

# The iterable created in the example above is [0,1,2]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

y = 0
while y < len(fruits):
    print(fruits[y])
    y = y+1

print(len(fruits))
print(y)

"""
RANGE FUNCTION

The range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default)
and stops before a specified number

SYNTAX: range(start, stop, step)
START optional (position to start)
STOP required (position to stop, not included)
STEP optional (specifying the incrementation. Default is 1)
"""
# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1

lolo = range(3, 19, 2)
for n in lolo:
    print(n)

listOfFruits = ["manzana", "banana", "anana"]
print(len(listOfFruits))

for j in range(len(listOfFruits)):
    print(listOfFruits[j])
