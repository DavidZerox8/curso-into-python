# Variables globales y locales

variable_global = 5

def funcion():
    variable_local = 10
    print(variable_local)
    print(variable_global)

funcion()
print(variable_global)
# print(variable_local) # Error: variable_local no está definida

# Las variables globales y locales se refieren a la visibilidad de las variables en el código.
# Las variables globales son visibles en todo el código, mientras que las variables locales solo son visibles en la función donde se definen.
# Si se intenta acceder a una variable local fuera de la función donde se definió, se generará un error.
# Si se intenta acceder a una variable global dentro de una función, se podrá hacer sin problemas.