class Figura:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.area = 0

    def obtener_area(self):
        print("Este metodo no esta disponible")

    def dibujar(self):
        print("Estoy en las coordenadas: " + str(self.x) + ", " + str(self.y)) 


class Circulo(Figura):
    def __init__(self, x, y,radio):
        super().__init__(x, y)
        self.radio = radio 

    def obtener_area(self):
        return 3.1416 * (self.radio * self.radio) 

    def dibujar(self):
        super().dibujar()
        print("El area que ocupo es de : ", self.obtener_area())

class Cuadrado(Figura):
    def __init__(self, x, y):
        super().__init__(x, y)

    def obtener_area(self):
        return self.x * self.y

    def dibujar(self):
        super().dibujar()
        print("El area que ocupo es de : ",self.obtener_area())       


circulo = Circulo(10,20,10)
circulo.dibujar() 
cuadrado = Cuadrado(5,5) 
cuadrado.dibujar()                           