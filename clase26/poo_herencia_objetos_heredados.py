## Herencia de objetos
# Ejercicio: Concesionaria de vehículos (Autos, Camiones, Bicicletas, Motos) con clientes y sus compras
# Crear una clase Vehiculo con los atributos: marca, modelo, año, precio
# Crear una clase Cliente con los atributos: nombre, apellido, dni, email
# Crear una clase Compra con los atributos: vehiculo, cliente, fecha
# Crear una clase Concesionaria con los atributos: nombre, vehiculos, clientes, compras

class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.available = True  # Nuevo campo
    
    def __str__(self):
        status = "disponible" if self.available else "vendido"
        return f'{self.marca} {self.modelo} {self.anio} ${self.precio} ({status})'
    
class Cliente:
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.dni} {self.email}'
    
class Compra:
    def __init__(self, vehiculo, cliente, fecha):
        if not vehiculo.available:
            raise ValueError(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ya fue vendido")
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.fecha = fecha
        vehiculo.available = False  # Marcar como vendido
    
    def __str__(self):
        return f'{self.cliente} {self.vehiculo} {self.fecha}'
    
class Concesionaria:
    def __init__(self, nombre, vehiculos, clientes, compras):
        self.nombre = nombre
        self.vehiculos = vehiculos
        self.clientes = clientes
        self.compras = compras
    
    def __str__(self):
        return f'{self.nombre}'
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_compra(self, compra):
        self.compras.append(compra)

    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def mostrar_compras(self):
        for compra in self.compras:
            print(compra)

# Crear objetos
# Ejemplo de uso con las nuevas funcionalidades
vehiculo1 = Vehiculo('Ford', 'Fiesta', 2019, 200000)
vehiculo2 = Vehiculo('Chevrolet', 'Onix', 2020, 250000)
vehiculo3 = Vehiculo('Toyota', 'Corolla', 2021, 300000)
cliente1 = Cliente('Juan', 'Perez', 12345678, 'correo@mail.com')
cliente2 = Cliente('Maria', 'Gomez', 87654321, 'mail@correo.com')

# Primera compra (exitosa)
compra1 = Compra(vehiculo1, cliente1, '2021-06-01')

# Segunda compra con otro vehículo (exitosa)
compra2 = Compra(vehiculo2, cliente2, '2021-06-02')

concesionaria = Concesionaria('Concesionaria', [], [], [])

concesionaria.agregar_vehiculo(vehiculo1)
concesionaria.agregar_vehiculo(vehiculo2)

concesionaria.agregar_cliente(cliente1)
concesionaria.agregar_cliente(cliente2)

concesionaria.agregar_compra(compra1)
concesionaria.agregar_compra(compra2)

concesionaria.mostrar_vehiculos()
concesionaria.mostrar_clientes()
concesionaria.mostrar_compras()

# Intentar comprar el mismo vehículo (generará error)
try:
    compra_invalida = Compra(vehiculo1, cliente2, '2021-06-02')
except ValueError as e:
    print(f"Error: {e}")

# Salida
# Ford Fiesta 2019 $200000
# Chevrolet Onix 2020 $250000
# Juan Perez 12345678
# Maria Gomez 87654321
# Juan Perez 12345678 Ford Fiesta 2019 $200000 2021-06-01
# Maria Gomez 87654321 Chevrolet Onix 2020 $250000 2021-06-02
