class paqueteria:
    def __init__(self,costo,iva):
        self.costo=costo
        self.iva=iva
    def calcular_resta(self):
        print(self.costo-self.iva)

class cosa(paqueteria):
    def __init__(self,costo,iva,apellido,nombre,direccion,cpaquete):
        super().__init__(costo,iva,)
        self.direccion=direccion
        self.cpaquete=cpaquete
        self.nombre=nombre
        self.apellido=apellido
    def printdireccion(self):
        print(self.direccion,self.nombre,self.apellido,self.costo,self.iva,self.cpaquete)
       

x = cosa(1500,50,"nataly","Rivera","5374467","7473633742")

x.calcular_resta()
x.printdireccion()