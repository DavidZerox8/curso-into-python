# Errores de sintaxis
#print("Hola Mundo" <-- Error de sintaxis

# print("Hola Mundo") <-- Error debido al espacio en blanco

#Variables
saludo = "Hola Mundo"
print(saludo)

# Tipos de datos
# Enteros
numero = 10
print(numero)

# Flotantes
numero_flotante = 10.5
print(numero_flotante)

# Booleanos
verdadero = True
falso = False
print(verdadero)
print(falso)

# Cadenas
cadena = "Hola Mundo"
print(cadena)

# Listas
lista = [1, 2, 3, 4, 5]
print(lista)

# Tuplas
tupla = (1, 2, 3, 4, 5)
print(tupla)

# Diccionarios
diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30
}

print(diccionario)

# Operadores aritméticos
# Suma
suma = 5 + 5
print(suma)

# Resta
resta = 10 - 5
print(resta)

# Multiplicación
multiplicacion = 5 * 5
print(multiplicacion)

# División
division = 10 / 2
print(division)

# Módulo
modulo = 10 % 3
print(modulo)

# Potencia
potencia = 2 ** 3
print(potencia)

# Operadores de comparación
# Igualdad
igual = 5 == 5
print(igual)

# Diferencia
diferente = 5 != 5
print(diferente)

# Mayor que
mayor = 5 > 3
print(mayor)

# Menor que
menor = 5 < 3
print(menor)

# Mayor o igual que
mayor_igual = 5 >= 5
print(mayor_igual)

# Menor o igual que
menor_igual = 5 <= 3
print(menor_igual)

# Operadores lógicos
# AND
and_logico = True and False
print(and_logico)

# OR
or_logico = True or False
print(or_logico)

# NOT
not_logico = not True
print(not_logico)

# Estructuras de control
# Condicionales
# IF
if 5 > 3:
    print("5 es mayor que 3")

# IF ELSE
if 5 < 3:
    print("5 es menor que 3")
else:
    print("5 no es menor que 3")

# IF ELIF ELSE
if 5 < 3:
    print("5 es menor que 3")
elif 5 == 3:
    print("5 es igual a 3")
else:
    print("5 no es menor que 3 ni igual a 3")

# Ciclos
# FOR
for i in range(5):
    print(i)

# WHILE
i = 0
while i < 5:
    print(i)
    i += 1

# Funciones
def suma(a, b):
    return a + b
resultado = suma(5, 5)
print(resultado)

# Clases
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años")
    
persona = Persona("Juan", "Perez", 30)
persona.saludar()

# Manejo de excepciones
try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Importar módulos
import math
print(math.pi)

