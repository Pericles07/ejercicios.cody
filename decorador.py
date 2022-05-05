def funcion_a(funcion_b):

    def funcion_c():
        print('Antes del llamado.')

        funcion_b()

        print('Despues del llamado.')

    return funcion_c

@funcion_a
def saludar():
    print('Hola, nos encontramos en una funcion')

saludar()    
