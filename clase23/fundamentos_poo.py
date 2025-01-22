#Programación orientada a objetos
#La programación orientada a objetos (POO) es un paradigma de programación que utiliza objetos y clases.
#Un objeto es una instancia de una clase.
#Una clase es un modelo que define las propiedades y métodos de un objeto.
#Las propiedades de una clase se llaman atributos.
#Las funciones de una clase se llaman métodos.
#En Python, las clases se definen con la palabra clave class.
#Para crear un objeto de una clase, se utiliza la siguiente sintaxis: objeto = Clase()

#Ejemplo: Clase Persona
class Persona:
    def __init__(self, nombre, edad): #Constructor: Método que se ejecuta al crear un objeto de la clase que tiene como parametros los atributos de la clase que se desean inicializar y la palabra reservada self que hace referencia al objeto que se está creando.
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

#Crear un objeto de la clase Persona
persona = Persona("Juan", 30)
persona.saludar() # Hola, mi nombre es Juan y tengo 30 años

#Ejemplo: Cuenta de banco
class CuentaBanco:
    def __init__(self, propietario, saldo_inicial):
        self.saldo = saldo_inicial
        self.propietario = propietario

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes suficientes fondos")
        else:
            self.saldo -= cantidad

    def detallesCuenta(self):
        print(f"Propietario: {self.propietario}")
        print(f"Saldo: {self.saldo}")

    def consultar_saldo(self):
        print(f"Hola {self.propietario}, tu saldo es de {self.saldo}")

#Crear un objeto de la clase CuentaBanco
cuenta = CuentaBanco("Juan", 1000)
cuenta.depositar(500)
cuenta.detallesCuenta()
cuenta.retirar(200)
cuenta.detallesCuenta()
cuenta.consultar_saldo()
