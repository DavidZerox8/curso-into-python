# Anotaciones de tipo
# Las anotaciones de tipo son una forma de especificar el tipo de los argumentos y el tipo de retorno de una función en Python.
# Las anotaciones de tipo no afectan el comportamiento de la función, pero pueden ser utilizadas por herramientas externas para hacer análisis de código.

# Para especificar el tipo de los argumentos y el tipo de retorno de una función, se utilizan los dos puntos (:) seguido del tipo.

# Ejemplo:
def sumar(a: int, b: int) -> int:
    return a + b

print (sumar(1, 2))  # 3

# En el ejemplo anterior, la función sumar recibe dos argumentos de tipo int y retorna un valor de tipo int.
# Las anotaciones de tipo son opcionales, pero se recomienda utilizarlas para mejorar la legibilidad del código.

# Ejemplo 2:

def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

print(saludar("Juan"))  # Hola Juan

# En el ejemplo anterior, la función saludar recibe un argumento de tipo str y retorna un valor de tipo str.

# Las anotaciones tambien pueden ser usadas en las clases y en las variables.

# Ejemplo 3:

class Persona:

    name: str
    age: int

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> str:
        return f"Hola {self.nombre}"
    
    def __str__(self) -> str: # Método especial que se llama cuando se convierte un objeto a string
        return f"{self.nombre} ({self.edad} años)"
    
p = Persona("Juan", 30)
print(p)  # Juan (30 años)


# Utilidades extra

# Libreria mypy
# mypy es una herramienta que permite hacer análisis estático de código Python y verificar las anotaciones de tipo.

# Para instalar mypy, se puede utilizar pip: pip install mypy
# Para ejecutar mypy, se puede utilizar el siguiente comando: mypy archivo.py

# Libreria optional
# La librería typing de Python incluye el tipo Optional, que se puede utilizar para indicar que un argumento o un retorno puede ser None.

# Ejemplo:
from typing import Optional

def dividir(a: int, b: int) -> Optional[float]:
    if b == 0:
        return None
    return a / b

print(dividir(10, 2))  # 5.0

# En el ejemplo anterior, la función dividir recibe dos argumentos de tipo int y retorna un valor de tipo Optional[float].

# Libreria Union
# La librería typing de Python incluye el tipo Union, que se puede utilizar para indicar que un argumento o un retorno puede ser de uno de varios tipos.

# Ejemplo:
from typing import Union

def sumar(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

print(sumar(1, 2))  # 3

# En el ejemplo anterior, la función sumar recibe dos argumentos de tipo Union[int, float] y retorna un valor de tipo Union[int, float].

