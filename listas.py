#punto 1
lista=[]

#punto 2
lista2=["johana","18","169","soltera","los cerezos"]


#punto 3
print("la primera lista tiene")
print(len(lista))
print("la segunda lista tiene")
print(len(lista2))


#punto 4
print("el primer valor es")
print(lista2[0])

print("el ultimo valor es")
print(max(lista2))


#punto 5
datos_personales=[]
for i in range (5):
    datos=input("ingrese el datos ")
    datos_personales.append(datos)
print("sus datos son")
print(datos_personales)


#punto 6
empresa=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


#punto 7
print("las empresas actuales son: ", empresa )
n=input("Ingresa el nombre de una nueva empresa ")
empresa.insert(7,n)
print(empresa)


#punto 8
print("buscar en la lista")
busca=input("ingrese la empresa a buscar ")
try:
    print("se encontro en la posicion",empresa.index(busca))
except:
    print("no se encontro")
 
 
#punto10    
empresa.reverse()
print("la lista se invirtio",empresa)   
#punto9
empresa.sort()
print("la lista se ordeno",empresa)


#punto 11
print("se eliminaron las primeras empresas")
empresa.pop(0)

print("se elmino otra empresa de la primera lista ")
del empresa[3:5]


#punto 12
empresa.clear()
print("la lista se ha vaciado",empresa)