to_do = [
    "Estudiar para el examen",
    "Hacer la tarea",
    "Comprar el regalo de cumpleaños",
    "Ir al supermercado",
    "Hacer ejercicio",
    2,3,2,2,34,3,'sf'
];

print(to_do[0]); #Primer elemento   
print(to_do[-1]); #Ultimo elemento

print(type(to_do)); #<class 'list'>

#Recorrer la lista
for i in to_do:
    print(i);

#Añadir un elemento al principio de la lista
to_do.insert(0, "Leer un libro");
print(to_do);

#Añadir un valor al final de la lista
to_do.append("Hacer la comida");
print(to_do);

#Añadir un valor en una posición específica
to_do.insert(2, "Hacer la cama");
print(to_do);

#Eliminar un valor de la lista
to_do.remove("Hacer la cama");
print(to_do);

#Eliminar un valor de la lista por su índice
to_do.pop(2);
print(to_do);

numbers = [11,1,2,3,4,5,6,7,8,9,10];
print(numbers);

#Ordenar la lista
numbers.sort();
print(numbers);

#Obtener el valor máximo
print(max(numbers));

#Obtener el valor mínimo
print(min(numbers));

#Ordenar la lista en orden descendente
numbers.sort(reverse=True);
print(numbers);

#Ordenar la lista sin modificar la original
numbers = [11,1,2,3,4,5,6,7,8,9,10];
print(sorted(numbers));
print(numbers);

#Invertir la lista
numbers.reverse();
print(numbers);

#Contar cuántas veces aparece un valor en la lista
print(numbers.count(2));

#Obtener el índice de un valor en la lista
print(numbers.index(2));

#Limpiar la lista
numbers.clear();
print(numbers);

#Eliminar la lista
del numbers;



