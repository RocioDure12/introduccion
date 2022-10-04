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



