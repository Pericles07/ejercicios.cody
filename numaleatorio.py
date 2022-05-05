import random

n = int(input('cuantos numeros random quieres?:'))

numeros = []

for numero in range (n):
    numeros.append(random.randint(0,100))

for numero in numeros:
    print(numero)    

