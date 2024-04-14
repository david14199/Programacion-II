class Personas:
    def __init__(self) :
        global user
        user=[]
    
    def menu(self):
        while True:
            print("\nMENU PERSONAS")
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
        return f'\nagrego el dato',per

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for x in user:
            print(x)
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese el dato a eliminar: ")
        user.remove(elim)
        print("El Dato Eliminado Es:" , elim)
        print("Lista Actual" , user)
        
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        print("Datos Actualizados")
        for i in user:
            print(i)

#CLASE UNIVERSIDADES    
class universidades:
    def __init__(self) :
        global unis
        unis=[]
    
    def menu(self):
        while True:
            print("\nMENU UNIVERSIDADES")
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
        uni=input("ingrese la UNiversidad: ")
        unis.append(uni)
        return f'\nagrego el dato',uni

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for p in unis:
            print(p)
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese la universidad a eliminar: ")
        unis.remove(elim)
        print("Dato Eliminado", elim)
        print("Lista Actual", unis)
    
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        print("universidades Actualizadas")
        for l in unis:
            print(l)

#MENU RESTAURANTES
class restaurantes:
    def __init__(self) :
        global re
        re=[]
    
    def menu(self):
        while True:
            print("\nMENU RESTAURANTES")
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
        print("Agregaste El dato ", r)

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for p in re:
            print(p)
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese El Restaurante a eliminar: ")
        re.remove(elim)
        print("Dato Eliminado", elim)
        print("Lista Actual", re)
    
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        print("Restaurantes Actualizados")
        for l in re:
            print(l)

#MENU ANIMALES
class Animales:
    def __init__(self) :
        global ani
        ani=[]
    
    def menu(self):
        while True:
            print("\nMENU ANIMALES")
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
        return f'agrego el dato',a

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for p in ani:
            print(p)
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese El animal a eliminar: ")
        ani.remove(elim)
        print("Dato Eliminado", elim)
        print("Lista Actual", ani)
    
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        print("Animales Actualizados")
        for l in ani:
            print(l)


        
        #return f'Datos Ingresados: ',user
        #return print(user)