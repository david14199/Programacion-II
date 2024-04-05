#Punto 1

perro={}
#Punto 2
perro={'nombre':'misael',
       'color':'blanco',
       'raza':'albino',
       'patas':'2',
       'edad':'3'
       }
#Punto 3
estudiante={}

estudiante={'nombre':'camila',
            'apellido':'gonzalez',
            'sexo':'mujer',
            'edad':'18',
            'estado_civil':'soltera_solterisima',
            'habilidades':['el chisme'],
            'pais':'colombia',
            'ciudad':'cartagena',
            'direccion':'Cerezos'}
print(estudiante.get('nombre'))
#Punto 4
print("Punto 4")
print("el diccionario es de",len(estudiante))
#Punto 5
print("Punto 5")
print(estudiante.get('habilidades'))
print(type(estudiante['habilidades']))
#Punto 6
print("Punto 6")
habi=input("ingrese las habilidades a añadir: ")
estudiante['habilidades'].append(habi)
print(estudiante.get('habilidades'))
#Punto 7
print("Punto 7")
print(estudiante.keys()) 
print(perro.keys()) 
#Punto 8
print("Punto 8")
print(estudiante.values())
print(perro.values())
#Punto 9
print("Punto 9")
print(estudiante.items())
print(perro.items())
#Punto 10
print("Punto 10")
estudiante.pop('sexo')
print(estudiante.keys()) 
print(estudiante.values())

#Punto 11
print("Punto 11")
estudiante.clear()
print(estudiante.items())