import os  # Importamos el módulo os para interactuar con el sistema operativo

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """
    def __init__(self, s_titulo, s_autor, s_isbn):
        """
        Constructor de la clase Libro.
        :param s_titulo: Título del libro (str).
        :param s_autor: Autor del libro (str).
        :param s_isbn: ISBN del libro (str).
        """
        self.s_titulo = s_titulo  # Título del libro
        self.s_autor = s_autor    # Autor del libro
        self.s_isbn = s_isbn      # ISBN del libro
        self.b_disponible = True  # Estado de disponibilidad (True por defecto)

    def prestar(self):
        """
        Método para prestar un libro.
        Cambia el estado de disponibilidad a False si el libro está disponible.
        """
        if self.b_disponible:
            self.b_disponible = False
            print(f"Libro '{self.s_titulo}' prestado con éxito.")
        else:
            print(f"El libro '{self.s_titulo}' ya está prestado.")

    def devolver(self):
        """
        Método para devolver un libro.
        Cambia el estado de disponibilidad a True si el libro estaba prestado.
        """
        if not self.b_disponible:
            self.b_disponible = True
            print(f"Libro '{self.s_titulo}' devuelto con éxito.")
        else:
            print(f"El libro '{self.s_titulo}' ya estaba disponible.")

    def mostrar(self):
        """
        Método para mostrar los detalles del libro.
        :return: Cadena formateada con los detalles del libro.
        """
        s_estado = "Sí" if self.b_disponible else "No"  # Convertir booleano a "Sí" o "No"
        return f"- {self.s_titulo} ({self.s_autor}) - ISBN: {self.s_isbn} - Disponible: {s_estado}"

class Biblioteca:
    """
    Clase que representa una biblioteca y gestiona una colección de libros.
    """
    def __init__(self):
        """
        Constructor de la clase Biblioteca.
        Inicializa una lista vacía para almacenar los libros.
        """
        self.libros = []  # Lista para almacenar objetos de la clase Libro

    def agregar_libro(self):
        """
        Método para agregar un nuevo libro a la biblioteca.
        Solicita al usuario que ingrese el título, autor e ISBN del libro.
        """
        s_titulo = input("Título: ")
        s_autor = input("Autor: ")
        s_isbn = input("ISBN: ")
        nuevo_libro = Libro(s_titulo, s_autor, s_isbn)  # Crear un nuevo objeto Libro
        self.libros.append(nuevo_libro)  # Agregar el libro a la lista
        print("Libro agregado con éxito.")

    def prestar_libro(self):
        """
        Método para prestar un libro.
        Solicita al usuario que ingrese el ISBN del libro a prestar.
        """
        s_isbn = input("Ingresa el ISBN: ")
        libro = self.buscar_libro(s_isbn)  # Buscar el libro por ISBN
        if libro:
            libro.prestar()  # Prestar el libro si se encuentra
        else:
            print("Libro no encontrado.")

    def devolver_libro(self):
        """
        Método para devolver un libro.
        Solicita al usuario que ingrese el ISBN del libro a devolver.
        """
        s_isbn = input("Ingresa el ISBN: ")
        libro = self.buscar_libro(s_isbn)  # Buscar el libro por ISBN
        if libro:
            libro.devolver()  # Devolver el libro si se encuentra
        else:
            print("Libro no encontrado.")

    def mostrar_libros(self):
        """
        Método para mostrar todos los libros en la biblioteca.
        """
        if self.libros:
            for libro in self.libros:
                print(libro.mostrar())  # Mostrar los detalles de cada libro
        else:
            print("No hay libros en la biblioteca.")

    def buscar_libro(self, s_isbn):
        """
        Método para buscar un libro por su ISBN.
        :param s_isbn: ISBN del libro a buscar (str).
        :return: El libro si se encuentra, None si no se encuentra.
        """
        for libro in self.libros:
            if libro.s_isbn == s_isbn:  # Comparar ISBNs
                return libro
        return None  # Retornar None si no se encuentra el libro

    def buscar_libro_interactivo(self):
        """
        Método interactivo para buscar un libro por su ISBN.
        Muestra los detalles del libro si se encuentra.
        """
        s_isbn = input("Ingresa el ISBN: ")
        libro = self.buscar_libro(s_isbn)  # Buscar el libro por ISBN
        if libro:
            print(libro.mostrar())  # Mostrar los detalles del libro
        else:
            print("Libro no encontrado.")

class Menu:
    """
    Clase que representa el menú interactivo del sistema de gestión de biblioteca.
    """
    def __init__(self):
        """
        Constructor de la clase Menu.
        Inicializa una instancia de la clase Biblioteca.
        """
        self.biblioteca = Biblioteca()  # Crear una instancia de Biblioteca

    def mostrar_menu(self):
        """
        Método para mostrar el menú de opciones.
        """
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")

    def ejecutar(self):
        """
        Método principal para ejecutar el menú interactivo.
        """
        while True:
            self.mostrar_menu()  # Mostrar el menú
            opcion = input("Elige una opción: ")  # Solicitar una opción al usuario

            if opcion == "1":
                self.biblioteca.agregar_libro()  # Agregar un libro
            elif opcion == "2":
                self.biblioteca.prestar_libro()  # Prestar un libro
            elif opcion == "3":
                self.biblioteca.devolver_libro()  # Devolver un libro
            elif opcion == "4":
                self.biblioteca.mostrar_libros()  # Mostrar todos los libros
            elif opcion == "5":
                self.biblioteca.buscar_libro_interactivo()  # Buscar un libro
            elif opcion == "6":
                print("Saliendo del programa...")  # Salir del programa
                break
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    """
    Punto de entrada del programa.
    """
    menu = Menu()  # Crear una instancia de Menu
    menu.ejecutar()  # Ejecutar el menú interactivo