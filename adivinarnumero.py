from random import randint

def adivina_numero():#parametros = variables de los ()
    numero_secreto = randint(0,10)

    ganador = False

    for intento in range(0,5):
        numero_pensado = input("En que numero estoy pensando? ")
        numero_pensado = int(numero_pensado)

        if numero_pensado == numero_secreto:
            ganador = True
            print("Felicidades, el numero es correcto.")
            break
        elif numero_pensado > numero_secreto:
            print("Mas bajo.")
        else:
            print("Mas alto.")  

    if ganador == False:
        print("El numero secreto es: " + str(numero_secreto)) 
    print("Gracias por jugar.")
adivina_numero()                 