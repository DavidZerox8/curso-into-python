lista = [1,2,3,4,5,6,7,8,9,10]
lista_alt = lista;

print(lista);
print(lista_alt);


del lista[0]
print(lista);
print(lista_alt);

print(id(lista));
print(id(lista_alt)); # id() returns the memory address of the object

# Slice
# lista[start:stop:step]
# start: index to start slicing
# stop: index to stop slicing
# step: step of slicing

lista_nueva = lista_alt[0:5:2] # [2,4,6]
print(lista_nueva)
print(id(lista_nueva))

lista.append(11)
print(lista)
print(lista_alt)
print(lista_nueva)