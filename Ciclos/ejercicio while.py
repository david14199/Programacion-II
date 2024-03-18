hola=True

def menu():
    print("1.persona")
    print("2.vehiculos")
    print("3.universidades")
    print("4.notas")
    print("5.salir")
while(hola):
    menu()
    a=int(input("ingrese su opcion "))
    if (a==1):
        print("usted ha seleccionado la opción persona")
       
    if(a==2):
        print("usted ha seleccionado la opción vehiculos")
      
    if(a==3):
        print("usted ha seleccionado la opcion universidades")
          
    if(a==4):   
        print("usted ha seleccionado la opción notas")
      
    if(a==5):
        print("Tenga buen día")
        exit()
    if(a>5 or a<1 ):
        print("usted no ha ingresado ninguna opción") 