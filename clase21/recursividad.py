#Recursividad
#Una función es recursiva si se llama a sí misma.

#Ejemplo: Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # 120

#Ejemplo: Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30)) # 5

#Ejemplo: Sumatoria de numeros naturales
def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n-1)
    
print(sumatoria(5)) # 15