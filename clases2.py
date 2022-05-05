class Usuario:

    def __unit__ (self):
        self.nombre = "Pedro"

    def presentarse(self):
        print("Hola mi nombre es ", self.nombre) 

    def asignar_apodo(self,apodo):
        self.nombre = apodo


Usuario = Usuario() 
Usuario.asignar_apodo("Perico") 
Usuario.presentarse()          
