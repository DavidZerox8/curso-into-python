#Herencia
#La herencia es una de las características más importantes de la programación orientada a objetos.
#La herencia es una forma de crear una nueva clase utilizando una clase existente como base.
#La nueva clase se denomina clase derivada o subclase.
#La clase de la que se deriva la nueva clase se denomina clase base o superclase.
#La herencia es útil porque permite reutilizar el código de la clase base.
#La herencia también permite añadir nuevos métodos y atributos a la clase derivada.
#La clase derivada hereda todos los métodos y atributos de la clase base.

#Ejemplo de herencia
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo, color)
        self.puertas = puertas

    def abrir_puertas(self):
        print(f"{self.marca} {self.modelo} abriendo puertas")

    def cerrar_puertas(self):
        print(f"{self.marca} {self.modelo} cerrando puertas")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    def encender(self):
        print(f"{self.marca} {self.modelo} encendiendo")

    def apagar(self):
        print(f"{self.marca} {self.modelo} apagando")

auto = Auto("Ford", "Fiesta", "Rojo", 4)
auto.acelerar()

moto = Moto("Honda", "CBR", "Negra", 250)
moto.acelerar()