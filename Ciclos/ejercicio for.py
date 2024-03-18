x={'Aerolinea':'Avianca',
'Vuelo':'AV3102',
'Origen': 'CTG',
'Destino': 'MDE',
'Tipo_Maleta': ['Cabina', 'Mano','Bodega']}

print("imprime toda la lista")
for id,valor in x.items():
    print(f"{id}:{valor}")
    
    
print("\nValores de tipo de maleta:")
for maleta in x["Tipo_Maleta"]:
    print(maleta)
    if (maleta=="Cabina"):
        print("su precio de cabina es incluido con su boleto basico")
    if (maleta=="Mano"):
        print("su maximo equipaje de mano no debe pesar mas de 4 kilos")
    if(maleta=="Bodega"):
        print("su maximo peso por bodega es de 21 kilos el cual tiene un costo de 60000")
        print("si se pasa de este peso tiene que pagar 15000 por cada kilo que se pase")

