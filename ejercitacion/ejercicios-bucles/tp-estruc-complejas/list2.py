# Guest List
def invitaciones(list):
    for i in list:
        print(i, "queda invitado cordialmente")


invitados = ["Juan Ramirez", "Anahi Ducret", "Martin Osorio"]

invitaciones(invitados)

print("ATENCION! Lamentablemente Martin Osorio no puede asistir")

invitados.pop(-1)
invitados.append("Valentina Macus")

invitaciones(invitados)

print("ATENCION! Se encuentran disponibles mas lugares para el evento")

invitados.insert(0, "Florencia Vega")
invitados.insert(2, "Francisco Loro")
invitados.append("Joaquin Palo")
invitaciones(invitados)

print("ATENCION, SOLO HAY DOS LUGARES DISPONIBLES")
print(len(invitados))
while len(invitados) > 2:
    print("Lo lamento no podre invitarte a cenar", invitados.pop(-1))

invitaciones(invitados)

invitados.clear()
print(invitados)

