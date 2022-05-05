mensaje = input("Ingrese una oracion: ")
vocales = ["a","e","i","o","u"]


nuevo_mensaje = ""


for caracter in mensaje:
    if caracter.lower() in vocales[0]:
        caracter =  1
    elif caracter.lower() in vocales[1]:
        caracter = 2 
    elif caracter.lower() in vocales[2]:
        caracter = 3
    elif caracter.lower() in vocales[3]:
        caracter = 4
    elif caracter.lower() in vocales[4]:
        caracter = 5              

    nuevo_mensaje = nuevo_mensaje + str(caracter)
print(nuevo_mensaje)        
