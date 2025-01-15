#Comprehension Lists - Listas por comprensión
#Listas por comprensión es una forma de crear listas de manera más rápida y sencilla.
#Ejemplo:

#Crear una lista con los cuadrados de los números del 1 al 10
squares = [i**2 for i in range(1,11)]
print(squares)

#Donde:
#squares: es la lista que se crea
#i**2: es el elemento que se agrega a la lista
#for i in range(1,11): es el ciclo que se realiza para agregar los elementos a la lista
#range(1,11): es el rango de números que se utilizan para

#Lista de grados celsius a fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

#Lista para obtener los números pares de una lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [num for num in numbers if num % 2 == 0]
print(even)

# El orden del for e if es importante porque:

# Primero se define qué elemento queremos (num en este caso)
# Luego especificamos de dónde vienen los elementos (for num in numbers)
# Finalmente filtramos con la condición (if num % 2 == 0)


#Transpuesta de una matriz
#Una transpuesta de una matriz es una matriz donde las filas se convierten en columnas y las columnas en filas.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
print(matrix)