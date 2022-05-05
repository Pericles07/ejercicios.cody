mensaje = "Hola mundo desde Python en su version 3.10"

contador = 0

for caracter in mensaje:
    if caracter in "1234567890":
       contador = contador + 1

if contador == 1:
    print("El string solo posee un numero entero.")
elif contador > 1:
    print("El string posee "  + str(contador) + " numeros enteros.")
   
else:
    print("Lo sentimos,el string no posee numeros enteros.")
        
