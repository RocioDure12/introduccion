"""resultado = 0
while True:
    letra = input("letra ?: ")
    if letra == "q":
        break
    elif letra == "a":
        for caracter in "Python":
            resultado = resultado+1
    elif letra == "b":
        for num in range(2,6):
            resultado=resultado+num
    else:
        resultado=-1
        print("Ingresa opcion valida")

print(f"Resultado:{resultado}")
"""
"""cadena="Hola como te va, que lindo dia"
letra="a"
cantidad=0
for l in cadena:
    if l == letra:
        cantidad=cantidad+1
print(cantidad)
"""

"""cadena="Hola como te va, que lindo dia"
vocales=0
for l in cadena:
    if l in "aeiou":
        vocales=vocales+1
print(vocales)
"""
"""
codigo="HGorLaac?isarsq!"
palabraSecreta=""
for i in range(len(codigo)):
    if i%2 ==1:
        palabraSecreta=palabraSecreta+ codigo[i]

print(palabraSecreta)
"""
"""codigo="HGorLa*c?isarsq!"
palabraSecreta=""
for i in range(len(codigo)):
    if codigo[i]=="*":
        break
    if i%2 ==1:
        palabraSecreta=palabraSecreta+ codigo[i]
print(palabraSecreta)


print(palabraSecreta)
"""
"""
nombre="Juana"
for i in nombre:
    print(i)
    
letra="a"
cantidad=0
for x in nombre:
    if x == letra:
        cantidad=cantidad+1
print(cantidad)   
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
