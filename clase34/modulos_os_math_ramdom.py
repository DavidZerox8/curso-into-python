# Uso de los módulos OS, Math y Random

# Importar los módulos necesarios
import os
import math
import random

# Ejemplo de OS - Obtener el directorio actual
directorio_actual = os.getcwd() # Current Working Directory (CWD) y tambien existe PWD (Present Working Directory)

# Mostrar el directorio actual
print(f"Directorio actual: {directorio_actual}")

# Ejemplo de Math - Crear una lista de números
# Crear una lista vacía
numeros = []

# Generar 10 números aleatorios
for i in range(10):
    # Generar un número aleatorio entre 1 y 100
    numero = random.randint(1, 100)
    # Agregar el número a la lista
    numeros.append(numero)

# Mostrar la lista de números
print(f"Números generados: {numeros}")

# Ejemplo de math - Calcular la raíz cuadrada de un número
numero = 25
raiz_cuadrada = math.sqrt(numero)

# Mostrar la raíz cuadrada
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

# Ejemplo de math - Calcular el area de un circulo
radio = 5
area_circulo = math.pi * radio ** 2

# Mostrar el area del circulo
print(f"El área del círculo con radio {radio} es: {area_circulo}")

# Mostar el valor de pi
print(f"El valor de pi es: {math.pi}")