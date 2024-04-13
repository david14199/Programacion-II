class Personas:
    def __init__(self) :
        global user
        user=[]
    
    def menu(self):
        while True:
            print("MENU PERSONAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print(Personas.agregar())
            elif opcion == "2":
                print(Personas.listar())
            elif opcion == "3":
                 print(Personas.eliminar())
            elif opcion =="4":
                print(Personas.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
            
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        per=input("ingrese la persona: ")
        user.append(per)
        tel=input("Ingrese Telefono: ")
        user.append(tel)
        adress=input("Ingrese Su Direccion: ")
        user.append(adress)
        gs=input("Ingrese Grupo Sanguineo: ")
        user.append(gs)
        Estcil=input("Ingrese Estado Civil: ")
        user.append(Estcil)
        return f'Dato Agregado: ',per

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        return f"Lista De Datos Ingresados:", user
            
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese el dato a eliminar: ")
        user.remove(elim)
        print(f"El Dato Eliminado Es: ", elim)
        return f"Lista Actual: ", user
        
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        pera=input("Ingrese la Dato A Actualizar ") 
        si=pera in user   
        if(si==True):
            actu=input("Ingrese El Dato Nuevo ")
            posicion=user.index(pera)
            user[posicion]=actu
        

        
#CLASE UNIVERSIDADES    
class universidades:
    def __init__(self) :
        global unis
        unis=[]
    
    def menu(self):
        while True:
            print("MENU UNIVERSIDADES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(universidades.agregar())
            elif opcion == "2":
                print(universidades.listar())
            elif opcion == "3":
                print(universidades.eliminar())
            elif opcion =="4":
                print(universidades.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        uni=input("ingrese la Universidad: ")
        unis.append(uni)
        tel=input("Ingrese Telefono: ")
        unis.append(tel)
        calidad=input("Ingrese Calidad Del Servicio: ")
        unis.append(calidad)
        Ubicacion=input("Ingrese Ubicacion: ")
        unis.append(Ubicacion)
        Dueño=input("Ingrese Propietario: ")
        unis.append(Dueño)
        return f'Dato Agregado: ',uni

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        return F"Lista De Datos Ingresados:", unis
            
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese la universidad a eliminar: ")
        unis.remove(elim)
        print("Dato Eliminado", elim)
        return "Lista Actual: ", unis
    
    def  actualizar():
        pera=input("Ingrese EL Universidad A actualizar ") 
        si=pera in unis   
        if(si==True):
            actu=input("Ingrese El Dato Nuevo: ")
            posicion=unis.index(pera)
            unis[posicion]=actu


#MENU RESTAURANTES
class restaurantes:
    def __init__(self) :
        global re
        re=[]
    
    def menu(self):
        while True:
            print("MENU RESTAURANTES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(restaurantes.agregar())
            elif opcion == "2":
                print(restaurantes.listar())
            elif opcion == "3":
                print(restaurantes.eliminar())
            elif opcion =="4":
                print(restaurantes.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        r=input("ingrese El Resturante: ")
        re.append(r)
        tel=input("Ingrese Telefono: ")
        re.append(tel)
        adress=input("Ingrese Su Direccion: ")
        re.append(adress)
        Servicio=input("Ingrese Numero De Estrellas: ")
        re.append(Servicio)
        Emplaño=input("Ingrese Trabajor Del Año: ")
        re.append(Emplaño)
        return "Dato Agregado:", r

        
    def listar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')  
        return f"Lista De Datos Ingresados:", re
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese El Restaurante a eliminar: ")
        re.remove(elim)
        print("Dato Eliminado", elim)
        return "Lista Actual: ", re
    
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        pera=input("Ingrese El Restaurante A Actualizar ") 
        si=pera in re   
        if(si==True):
            actu=input("Ingrese El Dato Nuevo: ")
            posicion=re.index(pera)
            re[posicion]=actu


#MENU ANIMALES
class Animales:
    def __init__(self) :
        global ani
        ani=[]
    
    def menu(self):
        while True:
            print("MENU ANIMALES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Animales.agregar())
            elif opcion == "2":
                print(Animales.listar())
            elif opcion == "3":
                print(Animales.eliminar())
            elif opcion =="4":
                print(Animales.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        a=input("ingrese El Animal: ")
        ani.append(a)
        Npatas=input("Ingrese Numero De Patas: ")
        ani.append(Npatas)
        Fvacu=input("Ingrese Fecha De Vacunacion Del Animal: ")
        ani.append(Fvacu)
        Dueño=input("Ingrese Tutor Del Animal: ")
        ani.append(Dueño)
        Color=input("Ingrese Color Del Animal: ")
        ani.append(Color)
        return f'Dato Agregado: ',a

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        return f"Lista De Datos Ingresados" , ani
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese El animal a eliminar: ")
        ani.remove(elim)
        print("Dato Eliminado", elim)
        return "Lista Actual:", ani
    
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        pera=input("Ingrese Animal A Actualizar ") 
        si=pera in ani   
        if(si==True):
            actu=input("Ingrese El Dato Nuevo: ")
            posicion=ani.index(pera)
            ani[posicion]=actu


        
        