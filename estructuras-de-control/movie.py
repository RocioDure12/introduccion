"""
Movie Tickets: Un cine cobra diferentes precios de boletos dependiendo de la edad de una persona.
Si una persona es menor de 3 años, la entrada es gratuita; si ellos tienen entre 3 y 12, la entrada
cuesta $700; y si son mayores de 12 años, el boleto es $850. Escriba un ciclo en el que pregunte a los
usuarios su edad y luego dígales el costo de su entrada al cine.
"""

edad=1
while edad > 0 and edad < 100:
    edad=int(input("Ingresa tu edad")) 
    if edad < 3:
        print("La entrada es gratuita")
    elif edad == 3  or edad <= 12:
        print("La entrada cuesta $ 700")
    elif  edad > 12:
        print("La entrada cuesta $850")
    
    