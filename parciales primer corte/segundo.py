class factura:
    def __init__(self,vendedor,id2,fecha_compra):
        self.vendedor=vendedor
        self.id2=id2
        self.fecha_compra=fecha_compra
    def imprimir():
        print(self.vendedor,self.id2,self.fecha_compra)
class factura2(factura):
    def __init__(self,vendedor,id2,fecha_compra,productos,precio,cantidad):
        super().__init__(vendedor,id2,fecha_compra)
        self.productos=productos
        self.precio=precio
        self.cantidad=cantidad
    def total2(self):
        self.total=self.cantidad*self.precio
        print("su factura es",self.total)
    def muestra(self):
        print("su vendedor es:",self.vendedor,"su id es:",self.id2,"su producto es:",self.productos,"su precio es:",self.precio,"su total es:",self.total)


x=factura2("misael","5","2000","leche",5000,8)
x.total2()
x.muestra()
