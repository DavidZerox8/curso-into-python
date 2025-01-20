#Funciones en python
#Una función es un bloque de código que sólo se ejecuta cuando es llamado. Puedes pasar datos, conocidos como parámetros, a una función.
#Una función puede devolver datos como resultado.
#Para definir una función en Python se utiliza la palabra clave def.

#Ejemplo
def my_function(name):
  print("Hola " + name)

my_function("David")

#Argumentos
#La información que la función recibe se llama argumento o parámetro.
#Puedes agregar tantos argumentos como desees, solo sepáralos con una coma.
#Ejemplo

def my_function(name, age):
    print("Hola " + name + ", tienes " + age + " años")

my_function("David", "25")

#Valores de retorno
#Para que una función devuelva un valor, se utiliza la palabra clave return:
#Ejemplo

def my_function(x):
    return 5 * x

print(my_function(3))

#Recursividad
#En Python una función puede llamarse a sí misma. Esto se conoce como recursividad.
#Ejemplo

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))