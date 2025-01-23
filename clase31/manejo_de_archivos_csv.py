# Descripción: Ejemplo de manejo de archivos CSV en Python
# Importar la librería CSV
import csv

#Lectura de un archivo CSV
with open('products.csv', 'r') as archivo_csv:

    # Crear un objeto lector
    lector = csv.reader(archivo_csv)

    # Iterar sobre las filas del archivo
    for linea in lector:

        # Imprimir la fila
        print(f"Producto: {linea[0]}, Precio: {linea[1]}")


# Escritura de un archivo CSV

# Datos a escribir - Formato: name,price,quantity,brand,category,entry_date
productos = [
    ['Laptop Acer', 1000, 5, 'HP', 'Computers', '2021-10-01'],
    ['Smartphone Motorola', 500, 10, 'Samsung', 'Phones', '2021-10-01'],
    ['Tablet Lenovo', 300, 8, 'Apple', 'Tablets', '2021-10-01']
]

# Abrir el archivo en modo escritura
with open('products_new.csv', 'w', newline='') as archivo_csv:

    # Crear un objeto escritor
    escritor = csv.writer(archivo_csv)

    # Escribir los datos
    for producto in productos:
        escritor.writerow(producto)


# Copiar datos de un archivo a otro nuevo

# Definimos el archivo de origen y destino
archivo_origen = 'products.csv'
archivo_destino = 'products_new.csv'

# Abrir el archivo de origen en modo lectura
with open(archivo_origen, 'r') as archivo_csv_origen:

    # Crear un objeto lector
    lector_csv = csv.DictReader(archivo_csv_origen)

    # Obtenemos el nombre de los campos
    campos = lector_csv.fieldnames + ['total_value']

    # Abrir el archivo de destino en modo escritura
    with open(archivo_destino, 'w', newline='') as archivo_csv_destino:

        # Crear un objeto escritor
        escritor_csv = csv.DictWriter(archivo_csv_destino, fieldnames=campos)

        # Escribir los datos
        escritor_csv.writeheader()

        # Iterar sobre las filas del archivo de origen
        for fila in lector_csv:

            # Calcular el valor total
            total = float(fila['price']) * float(fila['quantity'])

            # Agregar el valor total a la fila
            fila['total_value'] = total

            # Escribir la fila en el archivo de destino
            escritor_csv.writerow(fila)