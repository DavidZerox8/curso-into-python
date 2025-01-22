#Ejercicio 1: Gestión de biblioteca
# Crear una clase llamada Biblioteca que tenga los siguientes atributos:
# - nombre
# - ubicacion
# - libros
# - socios
# Crear una clase llamada Libro que tenga los siguientes atributos:
# - titulo
# - autor
# - genero
# - prestado
# Crear una clase llamada Socio que tenga los siguientes atributos:
# - nombre
# - apellido
# - dni
# - libros_prestados
# Crear los métodos necesarios para:
# - Agregar un libro a la biblioteca
# - Eliminar un libro de la biblioteca
# - Prestar un libro a un socio

class Biblioteca:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.libros = []
        self.socios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def prestar_libro(self, libro, socio):
        if libro in self.libros:
            libro.prestado = True
            socio.libros_prestados.append(libro)
        else:
            print("El libro no se encuentra en la biblioteca")
    
    def devolver_libro(self, libro, socio):
        if libro in socio.libros_prestados:
            libro.prestado = False
            socio.libros_prestados.remove(libro)
        else:
            print("El libro no se encuentra en los libros prestados del socio")
    
    def agregar_socio(self, socio):
        self.socios.append(socio)
    
    def eliminar_socio(self, socio):
        self.socios.remove(socio)

    def libros_status(self):
        for libro in self.libros:
            if libro.prestado:
                print(f"{libro} - Prestado")
            else:
                print(f"{libro} - Disponible")
    
    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"
    
class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.prestado = False
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class Socio:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.libros_prestados = []
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
# Crear una biblioteca
biblioteca = Biblioteca("Biblioteca Nacional", "Av. Las Heras 2555")

# Crear libros
libro1 = Libro("El Aleph", "Jorge Luis Borges", "Ficción")
libro2 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Ficción")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Infantil")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear socios
socio1 = Socio("Juan", "Perez", 12345678)
socio2 = Socio("Maria", "Gonzalez", 87654321)

# Agregar socios a la biblioteca
biblioteca.agregar_socio(socio1)
biblioteca.agregar_socio(socio2)

# Prestar libros
biblioteca.prestar_libro(libro1, socio1)    
biblioteca.prestar_libro(libro2, socio2)
biblioteca.prestar_libro(libro3, socio1)

# Verificar estado de los libros
biblioteca.libros_status()

# Devolver libros
biblioteca.devolver_libro(libro1, socio1)
biblioteca.devolver_libro(libro2, socio2)
biblioteca.devolver_libro(libro3, socio1)

# Verificar estado de los libros
biblioteca.libros_status()

# Eliminar libros de la biblioteca
biblioteca.eliminar_libro(libro1)
biblioteca.eliminar_libro(libro2)
biblioteca.eliminar_libro(libro3)

# Eliminar socios de la biblioteca
biblioteca.eliminar_socio(socio1)
biblioteca.eliminar_socio(socio2)

print(biblioteca)


# Ejercicio 2: Concesionaria de vehículos
# Crear una clase llamada Vehiculo que tenga los siguientes atributos:
# - marca
# - modelo
# - precio
# - vendido
# Crear una clase llamada Concesionaria que tenga los siguientes atributos:
# - nombre
# - ubicacion
# - vehiculos
# - vendedores
# Crear una clase llamada Vendedor que tenga los siguientes atributos:
# - nombre
# - apellido
# - dni
# - vehiculos_vendidos
# Crear los métodos necesarios para:
# - Agregar un vehículo a la concesionaria
# - Eliminar un vehículo de la concesionaria
# - Vender un vehículo
# - Mostrar los vehículos en venta
# - Mostrar los vehículos vendidos
# - Mostrar los vendedores
# - Mostrar los vehículos vendidos por un vendedor

class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.vendido = False
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"
    
class Concesionaria:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.vehiculos = []
        self.vendedores = []
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
    
    def eliminar_vehiculo(self, vehiculo):
        self.vehiculos.remove(vehiculo)
    
    def vender_vehiculo(self, vehiculo, vendedor):
        if vehiculo in self.vehiculos:
            vehiculo.vendido = True
            vendedor.vehiculos_vendidos.append(vehiculo)
        else:
            print("El vehículo no se encuentra en la concesionaria")
    
    def mostrar_vehiculos_venta(self):
        print("Vehículos en venta:")
        for vehiculo in self.vehiculos:
            if not vehiculo.vendido:
                print(vehiculo)
    
    def mostrar_vehiculos_vendidos(self):
        print("Vehículos vendidos:")
        for vehiculo in self.vehiculos:
            if vehiculo.vendido:
                print(vehiculo)
    
    def mostrar_vendedores(self):
        print("Vendedores:")
        for vendedor in self.vendedores:
            print(vendedor)
    
    def mostrar_vehiculos_vendidos_vendedor(self, vendedor):
        print(f"Vehículos vendidos por {vendedor}:")
        for vehiculo in vendedor.vehiculos_vendidos:
            print(vehiculo)
    
    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"
    
class Vendedor:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.vehiculos_vendidos = []
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
# Crear una concesionaria
concesionaria = Concesionaria("Autos S.A.", "Av. Rivadavia 1234")

# Crear vehículos
vehiculo1 = Vehiculo("Ford", "Fiesta", 300000)
vehiculo2 = Vehiculo("Chevrolet", "Onix", 400000)
vehiculo3 = Vehiculo("Volkswagen", "Gol", 350000)

# Agregar vehículos a la concesionaria
concesionaria.agregar_vehiculo(vehiculo1)
concesionaria.agregar_vehiculo(vehiculo2)
concesionaria.agregar_vehiculo(vehiculo3)

# Crear vendedores
vendedor1 = Vendedor("Juan", "Perez", 12345678)
vendedor2 = Vendedor("Maria", "Gonzalez", 87654321)

# Agregar vendedores a la concesionaria
concesionaria.vendedores.append(vendedor1)
concesionaria.vendedores.append(vendedor2)

# Vender vehículos
concesionaria.vender_vehiculo(vehiculo1, vendedor1)

# Mostrar vehículos en venta
concesionaria.mostrar_vehiculos_venta()

# Mostrar vehículos vendidos
concesionaria.mostrar_vehiculos_vendidos()

# Mostrar vendedores
concesionaria.mostrar_vendedores()

# Mostrar vehículos vendidos por un vendedor
concesionaria.mostrar_vehiculos_vendidos_vendedor(vendedor1)

# Eliminar vehículos de la concesionaria
concesionaria.eliminar_vehiculo(vehiculo1)

# Eliminar vendedores de la concesionaria
concesionaria.vendedores.remove(vendedor1)
concesionaria.vendedores.remove(vendedor2)

print(concesionaria)