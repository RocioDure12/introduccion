def saludar():
    print("Hola mi gente")


saludar()


"""def sumando(num1,num2):
    print(num1+num2)


sumando(5,6)
"""


def saludar(nombre, apellido):
    print("Hola", nombre, apellido)


saludar("Rocio", "Dure")

# Funciones con parametros opcionales
#Los parametros opcionales van ultimo


def sumando(num1,num2, mensaje=False):
    if mensaje:
        print("Esta es la suma", num1+num2)
    else:
        print(sumando)

sumando(5,6, True)

