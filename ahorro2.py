def validar(mensaje):
    while True:
        try:
            data =  float(input("coloca" + mensaje+": "))
            return data;
        except ValueError:
            print("el dato debe ser un valor entero o decimal")    


producto = input("¿que compraras? ")
precio = validar("coloca el precio de lo deseado")
ahorroActual = 0

while precio > ahorroActual:
    mesada = validar("coloca tu mesada ")
    ahorroActual = ahorroActual + mesada
    restante = precio - ahorroActual
    tiempoTotal = precio / mesada
    tiempoActual = ahorroActual / mesada
    tiempoRestante = tiempoTotal - tiempoActual
    print("Actualmente tienes ahorrado :" , ahorroActual)
    print("El dinero que te falta es $ : ", restante)
    print("los meses que te faltan para cumplir tu meta son :", tiempoRestante)

print("Felicidades llegaste a tu meta")