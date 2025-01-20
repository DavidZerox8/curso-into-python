#Funciones lambda
#Una función lambda es una pequeña función anónima definida con la palabra clave lambda.
#Pueden tener cualquier número de argumentos pero solo una expresión.
#Sintaxis

#lambda arguments : expression
#Ejemplo

#A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:
#A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b : a * b
print(x(5, 6))

#Obtener el cuadrado de los numeros de una lista con lambda
#Ejemplo

#A lambda function that returns the square of its argument:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#Usar lambda con filter
#Ejemplo

#A lambda function that returns True if the argument is even, and False otherwise:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda x: x%2 == 0, numbers))
print(filtered)
