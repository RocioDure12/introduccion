#base * altura /2
def area(base, altura):
    print(base*altura / 2)


area(14, 4)

# Funciones con listas


def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")


def sumar(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


numeros = [-2, -8, -7, -9]
palabras = ["ave", "ballena", "luna"]
mostrar_lista(numeros)
mostrar_lista(palabras)
sumatoria = sumar(numeros)
print("sumatoria", sumatoria)
