matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
print(matriz) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0]) # [1, 2, 3]
print(matriz[1][0]) # 4

#Las matrices son listas de listas que comparten los mismo métodos y propiedades de las listas

#Recorrer una matriz
 
for i in matriz:
    for j in i:
        print(j);

#Tuplas 
#Las tuplas son listas inmutables, es decir, no se pueden modificar una vez creadas
#Se crean con paréntesis
tupla = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tupla) # (1, 2, 3, 4, 5)
print(tupla2) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(tupla)) # <class 'tuple'>
print(tupla[0]) # 1