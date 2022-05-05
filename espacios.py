def Espacio(frase):
    contador = 0
    
    for caracter in frase:
        if caracter == " ":
            contador +=1
    return contador        




frase =input("ingrese una frase: ")

print("el numero de espacios es de ", Espacio(frase))






