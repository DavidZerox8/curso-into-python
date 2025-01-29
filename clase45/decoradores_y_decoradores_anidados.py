# Decoradores
# Los decoradores en Python son funciones que permiten modificar el comportamiento de otras funciones o métodos. Se utilizan para agregar funcionalidades de manera sencilla, sin cambiar el código de la función original. Un decorador toma una función como argumento, la envuelve (o "envuelve") en otra función y puede ejecutar código antes y después de la función original. Son especialmente útiles para tareas como la autenticación, el registro de actividad o la medición de tiempo de ejecución.

# Ejemplo de decorador

# Para crear un decorador en Python, simplemente definimos una función que toma otra función como argumento y devuelve una nueva función que envuelve la función original. Por ejemplo, supongamos que queremos crear un decorador que imprima un mensaje antes y después de la ejecución de una función. Podemos hacerlo de la siguiente manera:

# Definimos el decorador
def decorador(func):
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")

    return wrapper

# Aplicamos el decorador
@decorador
def funcion():
    print("Ejecutando la función")

# Llamamos a la función decorada
funcion()

# Decoradores anidados

# En Python, los decoradores pueden ser anidados, es decir, un decorador puede envolver a otro decorador. Esto permite crear decoradores más complejos y reutilizables. En este tutorial, veremos cómo crear y utilizar decoradores anidados en Python.

# Creación de decoradores anidados

# Para crear un decorador anidado en Python, simplemente definimos un decorador dentro de otro decorador. Por ejemplo, supongamos que queremos crear un decorador que imprima un mensaje antes y después de la ejecución de una función. Podemos hacerlo de la siguiente manera:

# Definimos el decorador interior
def decorador_interno(func):
    def wrapper():
        print("Antes de ejecutar la función interno")
        func()
        print("Después de ejecutar la función interno")
    return wrapper

# Definimos el decorador exterior

def decorador_externo(func):
    def wrapper():
        print("Antes de ejecutar la función externo")
        func()
        print("Después de ejecutar la función externo")
    return wrapper

# Aplicamos los decoradores

@decorador_externo
@decorador_interno
def funcion():
    print("Ejecutando la función")

# Llamamos a la función decorada
funcion()

# En este ejemplo, hemos definido dos decoradores, decorador_interno y decorador_externo, y los hemos aplicado a la función funcion. El decorador_interno imprime un mensaje antes y después de la ejecución de la función, y el decorador_externo hace lo mismo. Al aplicar ambos decoradores a la función funcion, el mensaje se imprimirá dos veces antes y después de la ejecución de la función.


# Decoradores con parametros
# Los decoradores en Python también pueden aceptar argumentos. Para crear un decorador con argumentos, simplemente definimos una función que acepta los argumentos del decorador y devuelve el decorador real. Por ejemplo, supongamos que queremos crear un decorador que acepte un mensaje personalizado como argumento. Podemos hacerlo de la siguiente manera:

# Definimos el decorador
def decorador(mensaje):
    def decorador_real(func):
        def wrapper():
            print(f"Antes de ejecutar la función: {mensaje}")
            func()
            print(f"Después de ejecutar la función: {mensaje}")
        return wrapper
    return decorador_real

# Aplicamos el decorador
@decorador("Mensaje personalizado")
def funcion():
    print("Ejecutando la función")

# Llamamos a la función decorada

funcion()