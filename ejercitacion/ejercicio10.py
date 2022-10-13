"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
Pseudocodigo
Definir peso_muñ peso peso_pay peso total como real
Definir cant_pay cant_muñ como entero
Escribir ingrese la cantidad muñecos
Leer cant_muñ
Escribir ingrese la cantidad payasos
Leer cant_payasos
si cantpayasos > 0 hacer
    peso payasos<-sumar total(cant * peso)
si cantmuñecas > 0 hacer
    peso muñecas<-sumar total(cant * peso)

peso total= pesototalMuñecas+ pesototalPayasos
Print ("Tu paquete pesara", peso total)



"""

from ast import If


peso_payasos =75
peso_muñecas =112
cant_payasos=0
cant_muñecas=0
pesoTotalMuñecas=0
pesoTotalPayasos=0
pesoTotalEnvio=0
def sumarTotal(cant, peso):
    (cant * peso)
cant_payasos=(input("Ingrese la cantidad de payasos a enviar"))
cant_muñecas=(input("Ingrese la cantidad de muñecas a enviar"))
if int(cant_payasos) > 0 :
    pesoTotalPayasos=sumarTotal(cant_payasos,peso_payasos)
if int(cant_muñecas)>0:
    pesoTotalMuñecas=sumarTotal(cant_muñecas,peso_muñecas)   

print(pesoTotalMuñecas)


###CORREGIR ESTO PORQUE ESTA  MAL
