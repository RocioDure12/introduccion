pizza={
    "precio":800,
    "tipo":"de la casa",
    "toppins":["extra queso", "anana", "morrones"]
}

print("ordenaste una pizza" + pizza["tipo"] + "el costo es de " + str(pizza["precio"])) + " con los siguientes toppings:"
for topping in pizza["toppins"]:
    print(topping)