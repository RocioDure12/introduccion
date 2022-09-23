from ast import For, If

if 5 > 2:
    print("Five is greater than two!")

# This is a comment

"""
This is a comment
written in
more than just one line
"""

# A variable is created the moment you first assign a value to it.

nombre = "Luna"
print(nombre)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 8
x = "Juana"
print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
print(type(nombre))

# Variable names are case-sensitive

# Estructuras condicionales
sueldo = float(input("ingrese sueldo"))
if sueldo > 3000:
    print("La persona debe abonar impuestos")

# Estructuras repetitivas

numero = 1
while numero <= 5:
    print(numero)
    numero += 1
    