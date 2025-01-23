# Manejo de archivos txt
# Archivo de texto: archivo que contiene texto plano
# Archivo binario: archivo que contiene información en binario
# Modos de apertura de archivos:
# r: read, lectura

# with open('cuento.txt', 'r') as archivo: 'r' es el modo de apertura
#     for linea in archivo:
#         print(linea.strip()) # strip() elimina los espacios en blanco al inicio y al final de la línea

#Ejericio 1: Leer todas la lineas pero en una lista
# with open('cuento.txt', 'r') as archivo:
#     lineas = archivo.readlines()
#     print(lineas)

#Ejercicio 2: Agrergar una linea nueva al archivo
with open('cuento.txt', 'a') as archivo: # a: append, agregar
   archivo.write('\n\nHola mundo\n\n')

#Ejercicio 3: Reedcribir el archivo
with open('cuento.txt', 'w') as archivo: # w: write, escritura
    archivo.write('Hola mundo\n')
   