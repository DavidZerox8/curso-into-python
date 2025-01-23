# Manejo de archivos JSON
# JSON: JavaScript Object Notation
# Es un formato ligero de intercambio de datos

# Importar el módulo json
import json

# Abrir un archivo JSON
with open('products.json') as archivo_json:
    # Cargar el contenido del archivo JSON
    productos = json.load(archivo_json)

# Mostrar el contenido del archivo JSON
# print(productos)

# Mostrar uno por uno los productos
for producto in productos:
    # print(producto)
    print(f"Producto: {producto['name']}")

# Añadir contenido a un archivo JSON
# Crear un nuevo producto - Estructura name price quantity brand category entry_date
nuevo_producto = {
    "name": "Café",
    "price": 2.50,
    "quantity": 100,
    "brand": "Nescafé",
    "category": "Bebidas",
    "entry_date": "2021-10-13"
}
    
# Añadir el producto nuevo
productos.append(nuevo_producto)

# Guardar los cambios en el archivo JSON
with open('products.json', 'w') as archivo_json:
    json.dump(productos, archivo_json, indent=4)


# Reto: Convertir CSV a JSON