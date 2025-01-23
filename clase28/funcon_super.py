# La función super() permite acceder a los métodos y atributos de la clase padre (superclase)
# desde una clase hija (subclase), facilitando la herencia y reutilización de código.

class Persona:
    def __init__(self, nombre, edad):
        # Constructor: Inicializa los atributos básicos de una persona
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        # Método para mostrar la información básica de la persona
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

    def __eq__(self, otro):
        # Método especial para comparar si dos personas son iguales (==)
        # Retorna True si tienen el mismo nombre y edad
        if isinstance(otro, Persona):
            return self.edad == otro.edad and self.nombre == otro.nombre
        return False

    def __lt__(self, otro):
        # Método especial para comparar si una persona es menor que otra (<)
        # Compara basándose en la edad
        if isinstance(otro, Persona):
            return self.edad < otro.edad
        return False

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # Constructor de Empleado que extiende el constructor de Persona
        # super() llama al constructor de la clase padre sin necesidad de referenciar self
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar(self):
        # Sobrescribe el método mostrar de Persona para incluir el sueldo
        # Primero llama al método mostrar de la clase padre
        super().mostrar()
        print(f'Sueldo: {self.sueldo}')

# Ejemplos de creación y uso de objetos
empleado1 = Empleado('Juan', 30, 5000)
empleado1.mostrar()  # Muestra toda la información del empleado

# Ejemplos de uso de los métodos de comparación
persona1 = Persona('Ana', 25)
persona2 = Persona('Ana', 25)
persona3 = Persona('Luis', 30)

print(f'\nComparaciones:')
# Demuestra el funcionamiento del método __eq__ (igualdad)
print(f'persona1 == persona2:', persona1 == persona2)  # True (mismo nombre y edad)
print(f'persona1 == persona3:', persona1 == persona3)  # False (diferente nombre y edad)
# Demuestra el funcionamiento del método __lt__ (menor que)
print(f'persona1 < persona3:', persona1 < persona3)    # True (25 < 30)
print(f'persona3 < persona1:', persona3 < persona1)    # False (30 < 25)