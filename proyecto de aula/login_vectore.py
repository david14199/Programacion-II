# Lista de usuarios y contraseñas
usuarios = []
contraseñas = []

# Función para registrar un nuevo usuario
def registrar_usuario(username, password):
    # Verificar si el usuario ya existe
    if username in usuarios:
        print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        return False
    # Guardar el nombre de usuario y contraseña en las listas
    usuarios.append(username)
    contraseñas.append(password)
    print("Usuario registrado exitosamente.")
    return True

# Función para iniciar sesión
def iniciar_sesion(username, password):
    # Verificar si el usuario existe
    if username in usuarios:
        # Verificar la contraseña
        index = usuarios.index(username)
        if contraseñas[index] == password:
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
    else:
        print("Usuario no encontrado.")
        return False

# Función para actualizar información del usuario
def actualizar_informacion(username, new_password):
    # Verificar si el usuario existe
    if username in usuarios:
        # Actualizar la contraseña en la lista de contraseñas
        index = usuarios.index(username)
        contraseñas[index] = new_password
        print("Información actualizada exitosamente.")
        return True
    else:
        print("Usuario no encontrado.")
        return False

# Función para el menú principal
def menu():
    print("Bienvenido al sistema de inicio de sesión.")
    while True:
        print("\nSeleccione una opción:")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Actualizar información de usuario")
        print("4. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            iniciar_sesion(username, password)
        elif opcion == "2":
            username = input("Ingrese un nombre de usuario: ")
            password = input("Ingrese una contraseña: ")
            registrar_usuario(username, password)
        elif opcion == "3":
            username = input("Ingrese su nombre de usuario: ")
            new_password = input("Ingrese su nueva contraseña: ")
            actualizar_informacion(username, new_password)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú principal
menu()