person = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

print(person)
print(person["name"])

person["name"] = "James"
print(person)

#Eliminar un valor del diccionario
del person["country"]
print(person)

#Obtener las clave del diccionario
print(person.keys())
print(type(person.keys()))

#Obtener los valores del diccionario
print(person.values())
print(type(person.values()))

#Obtener los elementos del diccionario (clave, valor)
print(person.items())
print(type(person.items()))

#Recorrer un diccionario
for key, value in person.items():
    print(key, value)

#Copiar un diccionario
person2 = person.copy()
print(person2)

#Crear un diccionario con un constructor
person3 = dict(person)
print(person3)

#Crear un diccionario de diccionarios
person4 = {
    "person1": {
        "name": "John",
        "age": 36,
        "country": "Norway"
    },
    "person2": {
        "name": "James",
        "age": 25,
        "country": "USA"
    },
    "person3": person
}

print(person4)

#Limpiar un diccionario
person.clear()
print(person)