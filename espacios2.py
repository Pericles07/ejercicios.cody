from xmlrpc.client import Boolean


def Espacios(frase):
    contador = 0
    
    for caracter in frase:
        if caracter == " ":
            contador +=1
    
    return contador     
    
frase = input("ingrese una frase: ")

if Espacios(frase):
    print("contiene espacios")
else:
    print("no contiene espacios")                   