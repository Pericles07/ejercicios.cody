from multiprocessing.sharedctypes import Value


def validar(message):
    while True:
        try:
            data = float(input("coloca "+message))
            return data
        except ValueError:
            print("El dato debe ser entero o decimal")


largo = validar(" el largo en metros: ")  
ancho = validar(" el ancho en metros: " )
m2xcaja = validar(" los metros cuadrados por caja: ")
precioXm2 = validar(" el precio por metro cuadrado: ")
precioXcaja = (m2xcaja * precioXm2)
m2cuarto = largo * ancho
cajas = m2cuarto/m2xcaja
preciototal = cajas * precioXcaja
print("Total de cajas que se necesitan: ",cajas)
print("precio total: ", preciototal)