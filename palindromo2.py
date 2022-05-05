def Palindromo(frase):
    frase = frase.lower() 
    frase = frase.replace(" ", "") 
    frase = frase.replace("a","à") 
    frase = frase.replace("e","è") 
    frase = frase.replace("i","ì") 
    frase = frase.replace("o","ò") 
    frase = frase.replace("u","ù") 

    a = 0
    b = len(frase) - 1

    for i in range(0, len(frase)):
        if frase[a] == frase[b]:
            a += 1
            b -= 1
        else:
            return False 

    return True

frase = input("ingrese una palabra o una frase: ") 
print(Palindromo(frase))
if Palindromo(frase):
    print("Es un palindromo") 
else:
    print("No es un palindromo")      

