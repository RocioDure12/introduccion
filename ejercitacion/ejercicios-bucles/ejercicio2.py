# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
Algoritmo
Algoritmo LALA
	Definir i Como Entero;
	Definir edad como Entero;
	Escribir "Ingresa edad"
	Leer edad;
	Para i<-edad hasta 1 Con Paso -1
		Escribir i
	FinPara
FinAlgoritmo

"""
#Otra solucion#
edad = int(input("Ingresa tu edad"))
for i in range(edad):
    print("has cumplido", i+1)
