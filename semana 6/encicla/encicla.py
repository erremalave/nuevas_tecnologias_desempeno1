usuarios = []
viajes = []

# Función para desplegar el menú
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registro de usuario")
        print("2. Solicitar cicla")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registro_usuario()
        elif opcion == '2':
            solicitar_cicla()
        elif opcion == '3':
            print("Gracias por usar EnCicla. ¡Nos vemos pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función para el registro de usuarios
def registro_usuario():
    id_tarjeta = input("Ingrese el número de la tarjeta: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    correo = input("Ingrese correo electrónico: ")

    # Se crea un diccionario para almacenar los datos del usuario
    usuario = {
        'id_tarjeta': id_tarjeta,
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo
    }

    # Se agregan los usuarios a la lista
    usuarios.append(usuario)
    print("Usuario creado con éxito")

# Función para solicitar un viaje
def solicitar_cicla():
    id_t_viaje = input("Ingrese su número de cívica: ")

    id_valido = None
    for usuario in usuarios:
        if id_t_viaje == usuario.get('id_tarjeta'):
            id_valido = id_t_viaje
            break

    if id_valido:
        print("¡Bienvenido! Por favor, ingrese los detalles del viaje: ")
        inicio = input("Inicio del viaje: ")
        destino = input("Destino del viaje: ")

        # Se crea un diccionario para almacenar la información del viaje del usuario
        viaje = {
            'usuario': id_valido,  # Usamos el número de cívica como identificador
            'inicio_viaje': inicio,
            'destino_viaje': destino
        }

        # Se agregan los detalles del viaje a la lista de viajes
        viajes.append(viaje)
        print("Viaje registrado exitosamente.")
    else:
        print("Usuario no encontrado en la lista de usuarios. Validación fallida.")

if __name__ == "__main__":
    menu()
