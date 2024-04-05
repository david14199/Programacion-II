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
            print("4. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Personas.agregar())
            elif opcion == "2":
                print(Personas.listar())
            elif opcion == "3":
                print(Personas.eliminar())
            elif opcion == "4":
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
        return f'Los datos en la base Datos de usuario son:',user
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese el dato a eliminar")
        user.remove(elim)
        
        return f'el dato eliminado es',elim,'La lista actual es',user