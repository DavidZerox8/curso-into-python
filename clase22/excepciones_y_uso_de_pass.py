#Excepciones y uso de pass
#En Python, las excepciones son errores que ocurren durante la ejecución de un programa.
#Las excepciones son manejadas por bloques try-except.
#El bloque try-except se utiliza para manejar excepciones.
#El bloque try-except se compone de dos bloques:
#try: Aquí se coloca el código que puede lanzar una excepción.
#except: Aquí se coloca el código que se ejecuta si se lanza una excepción.
#Las excepciones tienen jerarquia, es decir, una excepción puede ser una subclase de otra excepción.

#Ejemplo: División por cero
try:
    x = 1 / 0
except ZeroDivisionError:
    print("División por cero")

#Raise
#La instrucción raise se utiliza para lanzar una excepción.

#Ejemplo: Lanzar una excepción
# x = 10
# if x > 5:
#     raise Exception("x no debe ser mayor a 5")

#Pass
#La instrucción pass se utiliza para evitar errores.

#Ejemplo: Evitar errores
try:
    x = 1 / 0
except ZeroDivisionError:
    pass

#En el ejemplo anterior, la excepción ZeroDivisionError se ignora y el programa continúa su ejecución

#Ejemplo: Multiples excepciones
try:
    x = 1 / 0
except ZeroDivisionError:
    print("División por cero")
except:
    print("Ocurrió un error")

#En el ejemplo anterior, se manejan dos excepciones: ZeroDivisionError y cualquier otra excepción.

#Ver el listado de excepciones y su jerarquía:

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)