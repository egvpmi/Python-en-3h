# El programa comienza en la función main(), donde se inicializa una lista vacía libros.
# El bucle while True permite que el menú se muestre repetidamente hasta que el usuario elija salir.
# Cada opción del menú llama a una función específica para realizar la acción correspondiente.
# El usuario interactúa con el menú, dependiendo de la opción elegida, el programa:
# Agrega un libro.
# Presta un libro.
# Devuelve un libro.
# Muestra todos los libros.
# Busca un libro por ISBN.
# El programa valida las entradas y maneja errores (por ejemplo, si el ISBN no existe).
# El programa termina cuando el usuario elige la opción "Salir".

class Libro: # Constructor: Inicializa un objeto Libro con los valores proporcionados (s_titulo, s_autor, s_isbn).
    def __init__(self, s_titulo, s_autor, s_isbn): 
        self.s_titulo = s_titulo
        self.s_autor = s_autor
        self.s_isbn = s_isbn
        self.b_disponible = True  # Inicialmente, el libro está disponible.

    def prestar(self): # Cambia el estado de b_disponible a False si el libro está disponible.
        # Si el libro ya está prestado, muestra un mensaje indicando que no se puede prestar.
        if self.b_disponible:
            self.b_disponible = False
            print(f"Libro '{self.s_titulo}' prestado con éxito.")
        else:
            print(f"El libro '{self.s_titulo}' ya está prestado.")

    def devolver(self): # Cambia el estado de b_disponible a True si el libro estaba prestado.
        # Si el libro ya estaba disponible, muestra un mensaje indicando que no se puede devolver.
        if not self.b_disponible:
            self.b_disponible = True
            print(f"Libro '{self.s_titulo}' devuelto con éxito.")
        else:
            print(f"El libro '{self.s_titulo}' ya estaba disponible.")

    def mostrar(self): # Devuelve una cadena formateada con los detalles del libro (título, autor, ISBN) y su estado de disponibilidad.
        s_estado = "Sí" if self.b_disponible else "No"
        return f"- {self.s_titulo} ({self.s_autor}) - ISBN: {self.s_isbn} - Disponible: {s_estado}"

    @staticmethod # Definición del método estático buscar()
    # Busca un libro en una lista de libros por su ISBN.
    # Si encuentra el libro, lo devuelve; de lo contrario, devuelve None.
    def buscar(s_isbn, libros):
        for libro in libros:
            if libro.s_isbn == s_isbn:
                return libro
        return None

def agregar_libro(libros): # Definición de la función agregar_libro solicitando titulo, autor e isbn.
    s_titulo = input("Título: ")
    s_autor = input("Autor: ")
    s_isbn = input("ISBN: ")
    nuevo_libro = Libro(s_titulo, s_autor, s_isbn) # Crea un nuevo objeto Libro y lo agrega a la lista de libros.
    libros.append(nuevo_libro)
    print("Libro agregado con éxito.")

def prestar_libro(libros): # Definición de la función prestar_libro, solicita ISBN y verificaa si existe.
    # Solicita al usuario que ingrese el ISBN del libro que desea prestar.
    # Busca el libro en la lista y, si lo encuentra, llama al método prestar().
    # Si no lo encuentra, muestra el mensaje "Libro no encontrado.".
    s_isbn = input("Ingresa el ISBN: ")
    libro = Libro.buscar(s_isbn, libros)
    if libro:
        libro.prestar()
    else:
        print("Libro no encontrado.")

def devolver_libro(libros): # Definición de la función devolver_libro solicitando el ISBN.
    # Busca el libro en la lista y, si lo encuentra, llama al método devolver().
    # Si no lo encuentra, muestra el mensaje "Libro no encontrado.".
    s_isbn = input("Ingresa el ISBN: ")
    libro = Libro.buscar(s_isbn, libros)
    if libro:
        libro.devolver()
    else:
        print("Libro no encontrado.")

def mostrar_libros(libros): # Definición de la función mostrar_libros.
    # Muestra todos los libros en la lista, junto con su estado de disponibilidad.
    if libros:
        for libro in libros:
            print(libro.mostrar())
    else:
        print("No hay libros en la biblioteca.")

def buscar_libro(libros):# Definición de la función buscar_libro.
    # Solicita al usuario que ingrese el ISBN del libro que desea buscar.
    # Busca el libro en la lista y, si lo encuentra, muestra sus detalles.
    s_isbn = input("Ingresa el ISBN: ")
    libro = Libro.buscar(s_isbn, libros)
    if libro:
        print(libro.mostrar())
    else:
        print("Libro no encontrado.")

# Función main. Es el punto de entrada del programa. 
# Contiene un bucle infinito que muestra un menú interactivo al usuario.

def main():
    libros = []
    while True: # Menú de opciones.
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        # Según la opción elegida por el usuario, llama a la función correspondiente.
        if opcion == "1":
            agregar_libro(libros)
        elif opcion == "2":
            prestar_libro(libros)
        elif opcion == "3":
            devolver_libro(libros)
        elif opcion == "4":
            mostrar_libros(libros)
        elif opcion == "5":
            buscar_libro(libros)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")
            
# Asegura que el código dentro del bloque if solo se ejecute cuando el archivo se ejecuta directamente, no cuando se importa como un módulo.
if __name__ == "__main__":
    main()