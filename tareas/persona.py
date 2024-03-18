class persona:
    
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        
    def obtenernombre(self):
        print( f'su nombre es: {self.nombre} su apellido es : {self.apellido}')
        return f'la primera letra de su nombre es: {self.nombre[0]} la primera letra de su apellido es: {self.apellido[0]}'


