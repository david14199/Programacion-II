class Lote:
    def __init__(self, largo, ancho,contructora):
        self.largo = largo
        self.ancho = ancho
        self.contructora=contructora
    def calculararea(self):
        print (self.largo * self.ancho)

class casa(Lote):
    def __init__(self,largo,ancho,contructora,propa,telefono):
        super().__init__(largo,ancho,contructora)
        self.propa=propa
        self.telefono=telefono
    def imprime(self):
        print (self.contructora,self.propa,self.telefono )
        

x =casa(56,45,"panamericana","marianito","3000056446464")
x.calculararea()
x.imprime()
        
