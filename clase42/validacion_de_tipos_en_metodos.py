# Validación de tipos en métodos
# En Python, se pueden utilizar anotaciones de tipo para validar los tipos de los argumentos y los retornos de los métodos de una clase.

# Ejemplo:

def dividir(a: int, b: int) -> float:

    # Se valida que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        print("Los argumentos deben ser enteros")
        return None
    
    # Se valida que el segundo parametro sea distinto de cero
    if b == 0:
        print("El segundo argumento no puede ser cero")
        return None

    return a / b

print(dividir(0, 0))  # 5.0

# En el ejemplo anterior, la función dividir recibe dos argumentos de tipo int y retorna un valor de tipo float.
# Las anotaciones de tipo son opcionales en Python, pero pueden ser útiles para documentar el código y detectar errores en tiempo de desarrollo.

# Ejemplo con raise:

def dividir(a: int, b: int) -> float:
    
    # Se valida que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los argumentos deben ser enteros")
    
    # Se valida que el segundo parametro sea distinto de cero
    if b == 0:
        raise ValueError("El segundo argumento no puede ser cero")

    return a / b

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # ValueError: El segundo argumento no puede ser cero
print(dividir(10.5, 2))  # TypeError: Los argumentos deben ser enteros

# En el ejemplo anterior, se utiliza la función raise para lanzar una excepción en caso de que los argumentos no cumplan con los tipos esperados.

# Ejemplo con try-except:

def dividir(a: int, b: int) -> float:
    
    try:
        # Se valida que ambos parametros sean enteros
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Los argumentos deben ser enteros")
        
        # Se valida que el segundo parametro sea distinto de cero
        if b == 0:
            raise ValueError("El segundo argumento no puede ser cero")

        return a / b
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None
    
print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # Error: El segundo argumento no puede ser cero
print(dividir(10.5, 2))  # Error: Los argumentos deben ser enteros