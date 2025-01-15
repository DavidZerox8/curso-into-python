#Generadores e iteradores

#Iteradores
#Los iteradores son objetos que permiten recorrer un conjunto de elementos de a uno por vez.

#Ejemplo de iterador
lista = [1, 2, 3]

#Obtenemos un iterador de la lista
iterador = iter(lista)

#Imprimimos el primer elemento del iterador
# print(next(iterador))
#print(next(iterador))
#print(next(iterador))
#print(next(iterador)) #Este print va a dar error porque ya no hay mas elementos en el iterador

#Iteradores con cadena de texto
cadena = "Hola Mundo"

#Obtenemos un iterador de la cadena
iterador_cadena = iter(cadena)

#Imprimimos el primer elemento del iterador
# print(next(iterador_cadena))

#Iterar cadena de texto con for con su iterador
# for letra in iterador_cadena:
#     print(letra)

#Nota: Si el iterador fue imprimido con anterioridad, y se recorre con un ciclo, el ciclo no va a imprimir los elementos que ya fueron impresos con el next

#Iterador con range
limite = 10

#Obtenemos un iterador de range
iterador_range = iter(range(1, limite, 2))
#Donde, en el range, el primer parametro es el inicio, el segundo el limite y el tercero el paso

#Imprimimos el primer elemento del iterador
# for numero in iterador_range:
#     print(numero)

#Generadores
#Los generadores son una forma mas sencilla de crear iteradores en Python
#Para crear un generador, se utiliza la palabra reservada yield

#Ejemplo de generador
def generador():
    yield 1
    yield 2
    yield 3

#Usamos un ciclo for para recorrer el generador
# for numero in generador():
#     print(numero)

#Ejemplo de generador para crear la serie de fibonacci
def fibonacci(limite: int) -> int:
    """
    Genera la secuencia de Fibonacci hasta el límite especificado.
    Args:
        limite: Valor máximo hasta donde generar la secuencia.
    Yields:
        Números de la secuencia de Fibonacci.
    """
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b
    
#Usamos un ciclo for para recorrer el generador
for numero in fibonacci(30):
    print(numero)

#Test: Crear un generador para obtener los numeros pares e impares
def pares_impares(limite: int) -> int:
    """
    Genera los números pares e impares hasta el límite especificado.
    Args:
        limite: Valor máximo hasta donde generar la secuencia.
    Yields:
        Números pares e impares.
    """
    for numero in range(1, limite):
        if numero % 2 == 0:
            yield numero, "par"
        else:
            yield numero, "impar"
    
#Usamos un ciclo for para recorrer el generador
for numero, tipo in pares_impares(10):
    print(numero, tipo)