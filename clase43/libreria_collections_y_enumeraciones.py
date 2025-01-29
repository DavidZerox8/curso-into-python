# Librerias Collections y Enums
# La librería collections proporciona contenedores especializados para almacenar datos.
# La librería enum proporciona una forma de crear enumeraciones en Python.

# Importamos las librerias
from collections import Counter # Importamos la clase Counter
from enum import Enum # Importamos la clase Enum

# Clase Enumeracion
class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2
    BLOQUEADO = 3

# Funcion principal

def main():

    # Ejemplo de la clase Counter
    # Creamos una lista de elementos
    lista = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    # Creamos un objeto de la clase Counter
    contador = Counter(lista)
    # Imprimimos el objeto contador
    print(contador)

    # Ejemplo de la clase Enum
    # Imprimimos los valores de la enumeracion
    print(Estado.ACTIVO)
    print(Estado.INACTIVO)
    print(Estado.BLOQUEADO)

# Llamamos a la funcion principal

if __name__ == "__main__":
    main()

# Salida esperada
# Counter({'a': 3, 'b': 3, 'c': 3, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1})

# Libreria defaultdict
# La clase defaultdict es una subclase de dict que permite definir un valor por defecto para las claves que no existen en el diccionario.

# Importamos la clase defaultdict
from collections import defaultdict

# Funcion principal
def main():

    # Creamos un objeto de la clase defaultdict
    d = defaultdict(int)
    # Agregamos un valor al diccionario
    d['a'] = 1
    # Imprimimos el diccionario
    print(d)
    # Imprimimos un valor que no existe en el diccionario
    print(d['b'])

# Llamamos a la funcion principal
if __name__ == "__main__":
    main()

# Salida esperada
# defaultdict(<class 'int'>, {'a': 1})

# Libreria deque
# La clase deque es una lista de doble extremo que permite agregar y quitar elementos de ambos extremos de la lista.

# Importamos la clase deque
from collections import deque

# Funcion principal

def main():
    
    # Creamos un objeto de la clase deque
    d = deque()
    # Agregamos elementos al deque
    d.append(1)
    d.append(2)
    d.append(3)
    #Añadimos un elemento al principio del deque
    d.appendleft(0)
    # Imprimimos el deque
    print(d)
    # Eliminamos un elemento del deque
    d.popleft()
    #Eliminamos un elemento del deque del final
    d.pop()
    # Imprimimos el deque
    print(d)

# Llamamos a la funcion principal

if __name__ == "__main__":
    main()

# Salida esperada
# deque([1, 2, 3])