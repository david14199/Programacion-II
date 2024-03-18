class animales():
    def __init__(self,num_patas,propietario,fecha_vacunas,nombre):
        self.num_patas=num_patas
        self.propietario=propietario
        self.fecha_vacunas=fecha_vacunas
        self.nombre=nombre
    def Fnombre(self):
        print (self.nombre)
    def Fnum_patas(self):
        print("la cantidad de patas es:",self.num_patas)
    def Fpropietario(self):
        print("la cantidad de patas es:",self.propietario)
    def Ffecha_vacunas(self):
        print("las vacunas fueron realizadas en las fechas:",self.fecha_vacunas)

x=animales("8","misael","15/06/2000","juancho")
x.Fnombre()
x.Ffecha_vacunas()
x.Fpropietario()
x.Fnum_patas()
