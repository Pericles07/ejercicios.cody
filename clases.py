class Alarma:
    
    def __unit__(self):
        self.fecha_de_alarma = '31-03-2022'

    def programar(self):
        print('Hola soy programar')

alarma = Alarma()
alarma_dos = Alarma()

alarma.fecha_de_alarma = '01-04-2022'

print(alarma.fecha_de_alarma)
print(alarma_dos.fecha_de_alarma)