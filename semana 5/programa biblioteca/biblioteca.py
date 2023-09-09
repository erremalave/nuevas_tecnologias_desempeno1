class Libro:
    def __init__(self, id_libro, nombre, autor, paginas, editorial, disponibles, prestados):
        self.id_libro = id_libro
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas
        self.editorial = editorial
        self.disponibles = disponibles
        self.prestados = prestados

libros = []

def agregar_libro():
    id_libro = input("Ingrese el ID del libro: ")
    nombre = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el autor del libro: ")
    paginas = int(input("Ingrese el número de páginas: "))
    editorial = input("Ingrese la editorial: ")
    disponibles = int(input("Ingrese la cantidad de libros disponibles: "))
    prestados = int(input("Ingrese la cantidad de libros prestados: "))

    libro = Libro(id_libro, nombre, autor, paginas, editorial, disponibles, prestados)
    libros.append(libro)
    print("Libro agregado con éxito.")

def consultar_libros():
    for libro in libros:
        print(f"ID: {libro.id_libro}, Nombre: {libro.nombre}, Autor: {libro.autor}, Páginas: {libro.paginas}, Editorial: {libro.editorial}, Disponibles: {libro.disponibles}, Prestados: {libro.prestados}")

def editar_libro():
    id_libro = input("Ingrese el ID del libro que desea editar: ")
    for libro in libros:
        if libro.id_libro == id_libro:
            print(f"Editar libro con ID: {libro.id_libro}")
            nombre = input(f"Nombre actual: {libro.nombre}. Ingrese el nuevo nombre o presione Enter para mantener el nombre actual: ")
            if nombre:
                libro.nombre = nombre
            autor = input(f"Autor actual: {libro.autor}. Ingrese el nuevo autor o presione Enter para mantener el autor actual: ")
            if autor:
                libro.autor = autor
            paginas = input(f"Páginas actuales: {libro.paginas}. Ingrese el nuevo número de páginas o presione Enter para mantener el número actual: ")
            if paginas:
                libro.paginas = int(paginas)
            editorial = input(f"Editorial actual: {libro.editorial}. Ingrese la nueva editorial o presione Enter para mantener la editorial actual: ")
            if editorial:
                libro.editorial = editorial
            disponibles = input(f"Disponibles actuales: {libro.disponibles}. Ingrese la nueva cantidad de libros disponibles o presione Enter para mantener la cantidad actual: ")
            if disponibles:
                libro.disponibles = int(disponibles)
            prestados = input(f"Prestados actuales: {libro.prestados}. Ingrese la nueva cantidad de libros prestados o presione Enter para mantener la cantidad actual: ")
            if prestados:
                libro.prestados = int(prestados)
            print("Libro editado con éxito.")
            return
    print(f"No se encontró ningún libro con el ID {id_libro}.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar libro")
        print("2. Consultar libros")
        print("3. Editar libro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            consultar_libros()
        elif opcion == '3':
            editar_libro()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
