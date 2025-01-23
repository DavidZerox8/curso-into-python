# Pilares de la POO: Abstracción, Encapsulamiento, Polimorfismo
# Abstracción: Es el proceso de identificar las características más importantes de un objeto y eliminar los detalles que no son relevantes.
# Encapsulamiento: Es el proceso de ocultar los detalles de implementación de un objeto y exponer solo los detalles que son necesarios para interactuar con él.
# Polimorfismo: Es la capacidad de un objeto para comportarse de diferentes maneras según el contexto en el que se encuentre.
# Ejemplo de abstracción:

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass # Este método será implementado en las clases hijas

class Perro(Animal):
    def hablar(self):
        return "Guau!"
    
class Gato(Animal):
    def hablar(self):
        return "Miau!"

perro = Perro("Firulais")
gato = Gato("Garfield")

print(perro.hablar()) # Guau!
print(gato.hablar()) # Miau!

# Ejemplo de encapsulamiento:
# Las variables de instancia de una clase pueden ser privadas, es decir, solo accesibles desde dentro de la clase.
# Para hacer una variable privada, se debe anteponer dos guiones bajos al nombre de la variable.
# Por ejemplo, __saldo
# Las variables protegidas se definen con un guion bajo al principio del nombre de la variable.
# Por ejemplo, _saldo
# La diferencia entre una variable privada y una protegida es que la variable privada no puede ser accedida desde una clase hija.

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        self.__saldo -= cantidad

    def obtener_saldo(self):
        return self.__saldo
    
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.obtener_saldo()) # 1300
#print(cuenta.__saldo) # AttributeError: 'CuentaBancaria' object has no attribute '__saldo'

# Ejemplo de polimorfismo:

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        pass # Este método será implementado en las clases hijas

class Coche(Vehiculo):
    def acelerar(self):
        return "Acelerando coche..."
    
class Moto(Vehiculo):
    def acelerar(self):
        return "Acelerando moto!"
    
coche = Coche("Toyota")
moto = Moto("Yamaha")

print(coche.acelerar()) # Acelerando coche...
print(moto.acelerar()) # Acelerando moto!

# Ejemplo de polimorfismo con funciones:

def acelerar_vehiculo(vehiculo):
    return vehiculo.acelerar()

print(acelerar_vehiculo(coche)) # Acelerando coche...
print(acelerar_vehiculo(moto)) # Acelerando moto!