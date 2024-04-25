SJF=[]
FIFO=[]
rafa=[]
hola=True
while (hola):
    print("1.FIFO")
    print("2.SJF")
    print("3.Mostrar cola de FIFO")
    print("4.Mostrar cola de SJF")
    print("5.cerrrar \n")
    opcion=int(input("Ingrese la opcion "))
    if(opcion==1):
        
        fifo=input("Ingrese los procesos a añadir a algoritmo de fifo en su orden ")
        FIFO.append(fifo)
        ra=int(input("Ingrese la rafa de cpu"))
        rafa.append(ra)
        
        print()
    if(opcion==2):
        print("SJF")
    
    if(opcion==3):
        for i in range (len(FIFO)):
            print(i,FIFO[i])
            
        print("-------",FIFO[0],"-----",FIFO[1])
        print(0,"_______",rafa[0],"_____",rafa[0]+rafa[1])

    if(opcion==4):
        print("")
    if(opcion==5):
        print("adios")
        hola=False