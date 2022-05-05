#remplazar vocales
mensaje = "hOla mundo"
vocales = ["a","e","i","o","u"]

nuevo_mensaje = ""

for caracter in mensaje:
    if caracter.lower() in vocales:
        caracter = "@"

    nuevo_mensaje = nuevo_mensaje + caracter    
print(nuevo_mensaje)   